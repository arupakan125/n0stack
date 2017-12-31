import time
from typing import Any  # NOQA
import libvirt

from n0library.logger import Logger

from n0core.target.vm.base import QemuOpen
from n0core.target import Target
from n0core.model.resource.vm import VMState
from n0core.target.vm.xml_generator import (define_vm_xml,
                                            define_volume_xml,
                                            define_interface_xml,
                                            build_volume,
                                            build_network)


logger = Logger()


class LibvirtKVM(QemuOpen, Target):  # NOQA
    """
    manage vm status
    """
    def __init__(self):
        # type: () -> None
        super().__init__("resource/vm/libvirt_kvm")

    def apply(self, model):
        # type: (Model) -> Tuple[Model, bool, str]
        # Create VM
        is_exist = True
        vm_name = model.name + model.id
        try:
            self.conn.lookupByName(vm_name)
        except libvirt.libvirtError:
            is_exist = False

        if not is_exist:
            cpu = {"arch": model.arch, "vcpus": model.vcpus}

            nic_type = model.dependencies[0].model.type.split("/")[-1]
            nic_name = model.dependencies[0].model.name
            hw_addr = model.dependencies[0].model.hw_addr

            disk_path = model.dependencies[1].model.url.replace("file:///", "")
            iso_path = "/var/lib/n0stack/ubuntu-16.04.3-server-amd64.iso"

            if not self.create(vm_name,
                               cpu,
                               int(model.memory / 1024),
                               disk_path,
                               iso_path,
                               nic_type,
                               nic_name,
                               hw_addr,
                               model.vnc_password):
                return model, False, "failed to create VM"

            return model, True, "succeeded"

        if model.state is VMState.POWEROFF:
            if not self.force_stop(vm_name):
                return model, False, "failed"
            return model, True, "succeeded"

        elif model.state is VMState.RUNNING:
            if not self.start(vm_name):
                return model, False, "failed"
            return model, True, "succeeded"

        #  TODO: SAVED process

        # Delete VM
        if model.state is VMState.DELETED:
            if not self.delete(vm_name):
                return model, False, "failed"
            return model, True, "succeeded to delete VM"

        return model, True, "nothing to change"

    def start(self, name):
        # type: (str) -> bool
        domain = self.conn.lookupByName(name)
        domain.create()

        # fail if over 120 seconds
        s = time.time()
        while True:
            if domain.info()[0] == 1:
                break
            if time.time() - s > 120:
                logger.error("Failed to start VM")
                return False

        return True

    def stop(self, name):
        # type: (str) -> bool
        domain = self.conn.lookupByName(name)
        domain.shutdown()

        # fail if over 120 seconds
        s = time.time()
        while True:
            if domain.info()[0] != 1:
                break
            if time.time() - s > 120:
                logger.error("Failed to stop VM")
                return False

        return True

    def force_stop(self, name):
        # type: (str) -> bool
        domain = self.conn.lookupByName(name)
        domain.destroy()

        # fail if over 60 seconds
        s = time.time()
        while True:
            if domain.info()[0] != 1:
                break
            if time.time() - s > 60:
                logger.error("Failed to stop VM")
                return False

        return True

    def create(self,
               name,  # type: str
               cpu,  # type: Any
               memory,  # type: str
               disk_path,  # type: str
               cdrom,  # type: str
               nic_type,  # type: str
               nic_name,  # type: str
               hw_addr,  # type: str
               vnc_password,  # type: str
               ):
        # type: (...) -> bool

        # default values of nic
        nic = {'type': 'bridge',
               'source': nic_name,
               'mac_addr': hw_addr,
               'model': nic_type}

        vm_xml = define_vm_xml(name,
                               cpu,
                               memory,
                               disk_path,
                               cdrom,
                               nic,
                               vnc_password)

        dom = self.conn.defineXML(vm_xml)

        if dom:
            logger.error("Failed to create VM")
            return False

        if dom.create(dom) < 0:
            logger.error("Failed to create VM")
            return False

        return True

    def delete(self, name):
        # type: (str) -> bool
        try:
            vdom = self.conn.lookupByName(name)
            if vdom.isActive():
                vdom.shutdown()

            if vdom.isActive():
                vdom.destroy()
            else:
                vdom.undefine()

        except libvirt.libvirtError as e:
            logger.error("Failed to delete VM")
            return False

        return True

    def update(self, name, vcpus, memory):
        # type: (str, int, int) -> bool
        try:
            dom = self.conn.lookupByName(name)
            dom.setMemory(vcpus)
            dom.setMemory(memory)

        except libvirt.libvirtError as e:
            logger.error("Failed to change memory capacity")
            return False

        return True

    def attach_volume(self, name, volume_id):
        # type: (str, str) -> bool
        vm = self.conn.lookupByName(name)

        xml = define_volume_xml("/var/lib/n0stack/" + volume_id)
        vm.attachDevice(xml)

        return True

    def attach_nic(self, name, network_name, mac_address):
        # type: (str, str) -> bool

        # TODO: mac_address
        vm = self.conn.lookupByName(name)

        xml = define_interface_xml(network_name, mac_address)
        vm.attachDevice(xml)

        return True


class Volume(QemuOpen, Target):
    """
    Generate xml of volume
    """
    def __init__(self):
        # type: () -> None
        super().__init__()

    def apply(self, model):
        # type: (Model) -> Tuple[Model, bool, str]
        is_exist = True
        vm_name = model.name + model.id
        try:
            self.conn.storagePoolLookupByName(vm_name)
        except libvirt.libvirtError:
            is_exist = False

        if not is_exist:
            self.create(vm_name, model.size)
            return model, True, "succeeded"

        # TODO: add delete handling
        return model, False, "already exists"

    def create(self, name, size):
        # type: (str, str) -> bool
        xml = build_volume(name, size)

        if self.pool.createXML(xml) is None:
            logger.error("Failed to create the volume")
            return False

        return True

    def delete(self, name, wipe=True):
        # type: (str, bool) -> bool
        storage = self.pool.storageVolLookupByName(name+'.img')

        if storage is None:
            logger.error("Failed to delete the storage")
            return False

        if wipe:
            storage.wipe(0)
        storage.delete(0)

        return True


class Network(QemuOpen):
    """
    Generate xml of network
    """
    def __init__(self):
        # type: () -> None
        super().__init__()

    def apply(self, model):
        # type: (Model) -> Tuple[Model, bool, str]
        # TODO
        return model, True, "succeeded"

    def create(self,
               network_name,  # type: str
               bridge_name,  # type: str
               address,  # type: str
               netmask,  # type: str
               range_start,  # type: str
               range_end  # type: str
               ):
        # type: (...) -> bool
        xml = build_network(network_name,
                            bridge_name,
                            address,
                            netmask,
                            range_start,
                            range_end)

        network = self.conn.networkCreateXML(xml)

        if network is None:
            logger.error("Failed to create a virtual network")
            return False

        return True