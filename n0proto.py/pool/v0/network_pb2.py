# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pool/v0/network.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from budget.v0 import network_interface_pb2 as budget_dot_v0_dot_network__interface__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pool/v0/network.proto',
  package='n0stack.pool',
  syntax='proto3',
  serialized_options=_b('Z3github.com/n0stack/n0stack/n0proto.go/pool/v0;ppool'),
  serialized_pb=_b('\n\x15pool/v0/network.proto\x12\x0cn0stack.pool\x1a\x1bgoogle/protobuf/empty.proto\x1a!budget/v0/network_interface.proto\"\xf9\x03\n\x07Network\x12\x0c\n\x04name\x18\x01 \x01(\t\x12;\n\x0b\x61nnotations\x18\x03 \x03(\x0b\x32&.n0stack.pool.Network.AnnotationsEntry\x12\x0f\n\x07version\x18\x05 \x01(\x04\x12\x11\n\tipv4_cidr\x18\n \x01(\t\x12\x11\n\tipv6_cidr\x18\x0b \x01(\t\x12\x0e\n\x06\x64omain\x18\x0c \x01(\t\x12\x31\n\x05state\x18\x32 \x01(\x0e\x32\".n0stack.pool.Network.NetworkState\x12Y\n\x1breserved_network_interfaces\x18\x33 \x03(\x0b\x32\x34.n0stack.pool.Network.ReservedNetworkInterfacesEntry\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x62\n\x1eReservedNetworkInterfacesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .n0stack.budget.NetworkInterface:\x02\x38\x01\"6\n\x0cNetworkState\x12\n\n\x06\x46\x41ILED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\r\n\tAVAILABLE\x10\x02\"\x15\n\x13ListNetworksRequest\"?\n\x14ListNetworksResponse\x12\'\n\x08networks\x18\x01 \x03(\x0b\x32\x15.n0stack.pool.Network\"!\n\x11GetNetworkRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xe7\x01\n\x13\x41pplyNetworkRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12G\n\x0b\x61nnotations\x18\x03 \x03(\x0b\x32\x32.n0stack.pool.ApplyNetworkRequest.AnnotationsEntry\x12\x0f\n\x07version\x18\x05 \x01(\x04\x12\x11\n\tipv4_cidr\x18\n \x01(\t\x12\x11\n\tipv6_cidr\x18\x0b \x01(\t\x12\x0e\n\x06\x64omain\x18\x0c \x01(\t\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"$\n\x14\x44\x65leteNetworkRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xa4\x02\n\x1eReserveNetworkInterfaceRequest\x12\x14\n\x0cnetwork_name\x18\x01 \x01(\t\x12\x1e\n\x16network_interface_name\x18\x02 \x01(\t\x12R\n\x0b\x61nnotations\x18\x03 \x03(\x0b\x32=.n0stack.pool.ReserveNetworkInterfaceRequest.AnnotationsEntry\x12\x18\n\x10hardware_address\x18\x04 \x01(\t\x12\x14\n\x0cipv4_address\x18\x05 \x01(\t\x12\x14\n\x0cipv6_address\x18\x06 \x01(\t\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"V\n\x1eReleaseNetworkInterfaceRequest\x12\x14\n\x0cnetwork_name\x18\x01 \x01(\t\x12\x1e\n\x16network_interface_name\x18\x02 \x01(\t2\x91\x04\n\x0eNetworkService\x12W\n\x0cListNetworks\x12!.n0stack.pool.ListNetworksRequest\x1a\".n0stack.pool.ListNetworksResponse\"\x00\x12\x46\n\nGetNetwork\x12\x1f.n0stack.pool.GetNetworkRequest\x1a\x15.n0stack.pool.Network\"\x00\x12J\n\x0c\x41pplyNetwork\x12!.n0stack.pool.ApplyNetworkRequest\x1a\x15.n0stack.pool.Network\"\x00\x12M\n\rDeleteNetwork\x12\".n0stack.pool.DeleteNetworkRequest\x1a\x16.google.protobuf.Empty\"\x00\x12`\n\x17ReserveNetworkInterface\x12,.n0stack.pool.ReserveNetworkInterfaceRequest\x1a\x15.n0stack.pool.Network\"\x00\x12\x61\n\x17ReleaseNetworkInterface\x12,.n0stack.pool.ReleaseNetworkInterfaceRequest\x1a\x16.google.protobuf.Empty\"\x00\x42\x35Z3github.com/n0stack/n0stack/n0proto.go/pool/v0;ppoolb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,budget_dot_v0_dot_network__interface__pb2.DESCRIPTOR,])



_NETWORK_NETWORKSTATE = _descriptor.EnumDescriptor(
  name='NetworkState',
  full_name='n0stack.pool.Network.NetworkState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVAILABLE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=555,
  serialized_end=609,
)
_sym_db.RegisterEnumDescriptor(_NETWORK_NETWORKSTATE)


_NETWORK_ANNOTATIONSENTRY = _descriptor.Descriptor(
  name='AnnotationsEntry',
  full_name='n0stack.pool.Network.AnnotationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='n0stack.pool.Network.AnnotationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='n0stack.pool.Network.AnnotationsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=453,
)

_NETWORK_RESERVEDNETWORKINTERFACESENTRY = _descriptor.Descriptor(
  name='ReservedNetworkInterfacesEntry',
  full_name='n0stack.pool.Network.ReservedNetworkInterfacesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='n0stack.pool.Network.ReservedNetworkInterfacesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='n0stack.pool.Network.ReservedNetworkInterfacesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=455,
  serialized_end=553,
)

_NETWORK = _descriptor.Descriptor(
  name='Network',
  full_name='n0stack.pool.Network',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='n0stack.pool.Network.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='n0stack.pool.Network.annotations', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='n0stack.pool.Network.version', index=2,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv4_cidr', full_name='n0stack.pool.Network.ipv4_cidr', index=3,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv6_cidr', full_name='n0stack.pool.Network.ipv6_cidr', index=4,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='n0stack.pool.Network.domain', index=5,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='n0stack.pool.Network.state', index=6,
      number=50, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reserved_network_interfaces', full_name='n0stack.pool.Network.reserved_network_interfaces', index=7,
      number=51, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NETWORK_ANNOTATIONSENTRY, _NETWORK_RESERVEDNETWORKINTERFACESENTRY, ],
  enum_types=[
    _NETWORK_NETWORKSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=609,
)


_LISTNETWORKSREQUEST = _descriptor.Descriptor(
  name='ListNetworksRequest',
  full_name='n0stack.pool.ListNetworksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=611,
  serialized_end=632,
)


_LISTNETWORKSRESPONSE = _descriptor.Descriptor(
  name='ListNetworksResponse',
  full_name='n0stack.pool.ListNetworksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='networks', full_name='n0stack.pool.ListNetworksResponse.networks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=634,
  serialized_end=697,
)


_GETNETWORKREQUEST = _descriptor.Descriptor(
  name='GetNetworkRequest',
  full_name='n0stack.pool.GetNetworkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='n0stack.pool.GetNetworkRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=699,
  serialized_end=732,
)


_APPLYNETWORKREQUEST_ANNOTATIONSENTRY = _descriptor.Descriptor(
  name='AnnotationsEntry',
  full_name='n0stack.pool.ApplyNetworkRequest.AnnotationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='n0stack.pool.ApplyNetworkRequest.AnnotationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='n0stack.pool.ApplyNetworkRequest.AnnotationsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=453,
)

_APPLYNETWORKREQUEST = _descriptor.Descriptor(
  name='ApplyNetworkRequest',
  full_name='n0stack.pool.ApplyNetworkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='n0stack.pool.ApplyNetworkRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='n0stack.pool.ApplyNetworkRequest.annotations', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='n0stack.pool.ApplyNetworkRequest.version', index=2,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv4_cidr', full_name='n0stack.pool.ApplyNetworkRequest.ipv4_cidr', index=3,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv6_cidr', full_name='n0stack.pool.ApplyNetworkRequest.ipv6_cidr', index=4,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='n0stack.pool.ApplyNetworkRequest.domain', index=5,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_APPLYNETWORKREQUEST_ANNOTATIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=735,
  serialized_end=966,
)


_DELETENETWORKREQUEST = _descriptor.Descriptor(
  name='DeleteNetworkRequest',
  full_name='n0stack.pool.DeleteNetworkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='n0stack.pool.DeleteNetworkRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=968,
  serialized_end=1004,
)


_RESERVENETWORKINTERFACEREQUEST_ANNOTATIONSENTRY = _descriptor.Descriptor(
  name='AnnotationsEntry',
  full_name='n0stack.pool.ReserveNetworkInterfaceRequest.AnnotationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='n0stack.pool.ReserveNetworkInterfaceRequest.AnnotationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='n0stack.pool.ReserveNetworkInterfaceRequest.AnnotationsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=453,
)

_RESERVENETWORKINTERFACEREQUEST = _descriptor.Descriptor(
  name='ReserveNetworkInterfaceRequest',
  full_name='n0stack.pool.ReserveNetworkInterfaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network_name', full_name='n0stack.pool.ReserveNetworkInterfaceRequest.network_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_interface_name', full_name='n0stack.pool.ReserveNetworkInterfaceRequest.network_interface_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='n0stack.pool.ReserveNetworkInterfaceRequest.annotations', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hardware_address', full_name='n0stack.pool.ReserveNetworkInterfaceRequest.hardware_address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv4_address', full_name='n0stack.pool.ReserveNetworkInterfaceRequest.ipv4_address', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv6_address', full_name='n0stack.pool.ReserveNetworkInterfaceRequest.ipv6_address', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RESERVENETWORKINTERFACEREQUEST_ANNOTATIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1007,
  serialized_end=1299,
)


_RELEASENETWORKINTERFACEREQUEST = _descriptor.Descriptor(
  name='ReleaseNetworkInterfaceRequest',
  full_name='n0stack.pool.ReleaseNetworkInterfaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network_name', full_name='n0stack.pool.ReleaseNetworkInterfaceRequest.network_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_interface_name', full_name='n0stack.pool.ReleaseNetworkInterfaceRequest.network_interface_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1301,
  serialized_end=1387,
)

_NETWORK_ANNOTATIONSENTRY.containing_type = _NETWORK
_NETWORK_RESERVEDNETWORKINTERFACESENTRY.fields_by_name['value'].message_type = budget_dot_v0_dot_network__interface__pb2._NETWORKINTERFACE
_NETWORK_RESERVEDNETWORKINTERFACESENTRY.containing_type = _NETWORK
_NETWORK.fields_by_name['annotations'].message_type = _NETWORK_ANNOTATIONSENTRY
_NETWORK.fields_by_name['state'].enum_type = _NETWORK_NETWORKSTATE
_NETWORK.fields_by_name['reserved_network_interfaces'].message_type = _NETWORK_RESERVEDNETWORKINTERFACESENTRY
_NETWORK_NETWORKSTATE.containing_type = _NETWORK
_LISTNETWORKSRESPONSE.fields_by_name['networks'].message_type = _NETWORK
_APPLYNETWORKREQUEST_ANNOTATIONSENTRY.containing_type = _APPLYNETWORKREQUEST
_APPLYNETWORKREQUEST.fields_by_name['annotations'].message_type = _APPLYNETWORKREQUEST_ANNOTATIONSENTRY
_RESERVENETWORKINTERFACEREQUEST_ANNOTATIONSENTRY.containing_type = _RESERVENETWORKINTERFACEREQUEST
_RESERVENETWORKINTERFACEREQUEST.fields_by_name['annotations'].message_type = _RESERVENETWORKINTERFACEREQUEST_ANNOTATIONSENTRY
DESCRIPTOR.message_types_by_name['Network'] = _NETWORK
DESCRIPTOR.message_types_by_name['ListNetworksRequest'] = _LISTNETWORKSREQUEST
DESCRIPTOR.message_types_by_name['ListNetworksResponse'] = _LISTNETWORKSRESPONSE
DESCRIPTOR.message_types_by_name['GetNetworkRequest'] = _GETNETWORKREQUEST
DESCRIPTOR.message_types_by_name['ApplyNetworkRequest'] = _APPLYNETWORKREQUEST
DESCRIPTOR.message_types_by_name['DeleteNetworkRequest'] = _DELETENETWORKREQUEST
DESCRIPTOR.message_types_by_name['ReserveNetworkInterfaceRequest'] = _RESERVENETWORKINTERFACEREQUEST
DESCRIPTOR.message_types_by_name['ReleaseNetworkInterfaceRequest'] = _RELEASENETWORKINTERFACEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Network = _reflection.GeneratedProtocolMessageType('Network', (_message.Message,), dict(

  AnnotationsEntry = _reflection.GeneratedProtocolMessageType('AnnotationsEntry', (_message.Message,), dict(
    DESCRIPTOR = _NETWORK_ANNOTATIONSENTRY,
    __module__ = 'pool.v0.network_pb2'
    # @@protoc_insertion_point(class_scope:n0stack.pool.Network.AnnotationsEntry)
    ))
  ,

  ReservedNetworkInterfacesEntry = _reflection.GeneratedProtocolMessageType('ReservedNetworkInterfacesEntry', (_message.Message,), dict(
    DESCRIPTOR = _NETWORK_RESERVEDNETWORKINTERFACESENTRY,
    __module__ = 'pool.v0.network_pb2'
    # @@protoc_insertion_point(class_scope:n0stack.pool.Network.ReservedNetworkInterfacesEntry)
    ))
  ,
  DESCRIPTOR = _NETWORK,
  __module__ = 'pool.v0.network_pb2'
  # @@protoc_insertion_point(class_scope:n0stack.pool.Network)
  ))
_sym_db.RegisterMessage(Network)
_sym_db.RegisterMessage(Network.AnnotationsEntry)
_sym_db.RegisterMessage(Network.ReservedNetworkInterfacesEntry)

ListNetworksRequest = _reflection.GeneratedProtocolMessageType('ListNetworksRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTNETWORKSREQUEST,
  __module__ = 'pool.v0.network_pb2'
  # @@protoc_insertion_point(class_scope:n0stack.pool.ListNetworksRequest)
  ))
_sym_db.RegisterMessage(ListNetworksRequest)

ListNetworksResponse = _reflection.GeneratedProtocolMessageType('ListNetworksResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTNETWORKSRESPONSE,
  __module__ = 'pool.v0.network_pb2'
  # @@protoc_insertion_point(class_scope:n0stack.pool.ListNetworksResponse)
  ))
_sym_db.RegisterMessage(ListNetworksResponse)

GetNetworkRequest = _reflection.GeneratedProtocolMessageType('GetNetworkRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETNETWORKREQUEST,
  __module__ = 'pool.v0.network_pb2'
  # @@protoc_insertion_point(class_scope:n0stack.pool.GetNetworkRequest)
  ))
_sym_db.RegisterMessage(GetNetworkRequest)

ApplyNetworkRequest = _reflection.GeneratedProtocolMessageType('ApplyNetworkRequest', (_message.Message,), dict(

  AnnotationsEntry = _reflection.GeneratedProtocolMessageType('AnnotationsEntry', (_message.Message,), dict(
    DESCRIPTOR = _APPLYNETWORKREQUEST_ANNOTATIONSENTRY,
    __module__ = 'pool.v0.network_pb2'
    # @@protoc_insertion_point(class_scope:n0stack.pool.ApplyNetworkRequest.AnnotationsEntry)
    ))
  ,
  DESCRIPTOR = _APPLYNETWORKREQUEST,
  __module__ = 'pool.v0.network_pb2'
  # @@protoc_insertion_point(class_scope:n0stack.pool.ApplyNetworkRequest)
  ))
_sym_db.RegisterMessage(ApplyNetworkRequest)
_sym_db.RegisterMessage(ApplyNetworkRequest.AnnotationsEntry)

DeleteNetworkRequest = _reflection.GeneratedProtocolMessageType('DeleteNetworkRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETENETWORKREQUEST,
  __module__ = 'pool.v0.network_pb2'
  # @@protoc_insertion_point(class_scope:n0stack.pool.DeleteNetworkRequest)
  ))
_sym_db.RegisterMessage(DeleteNetworkRequest)

ReserveNetworkInterfaceRequest = _reflection.GeneratedProtocolMessageType('ReserveNetworkInterfaceRequest', (_message.Message,), dict(

  AnnotationsEntry = _reflection.GeneratedProtocolMessageType('AnnotationsEntry', (_message.Message,), dict(
    DESCRIPTOR = _RESERVENETWORKINTERFACEREQUEST_ANNOTATIONSENTRY,
    __module__ = 'pool.v0.network_pb2'
    # @@protoc_insertion_point(class_scope:n0stack.pool.ReserveNetworkInterfaceRequest.AnnotationsEntry)
    ))
  ,
  DESCRIPTOR = _RESERVENETWORKINTERFACEREQUEST,
  __module__ = 'pool.v0.network_pb2'
  # @@protoc_insertion_point(class_scope:n0stack.pool.ReserveNetworkInterfaceRequest)
  ))
_sym_db.RegisterMessage(ReserveNetworkInterfaceRequest)
_sym_db.RegisterMessage(ReserveNetworkInterfaceRequest.AnnotationsEntry)

ReleaseNetworkInterfaceRequest = _reflection.GeneratedProtocolMessageType('ReleaseNetworkInterfaceRequest', (_message.Message,), dict(
  DESCRIPTOR = _RELEASENETWORKINTERFACEREQUEST,
  __module__ = 'pool.v0.network_pb2'
  # @@protoc_insertion_point(class_scope:n0stack.pool.ReleaseNetworkInterfaceRequest)
  ))
_sym_db.RegisterMessage(ReleaseNetworkInterfaceRequest)


DESCRIPTOR._options = None
_NETWORK_ANNOTATIONSENTRY._options = None
_NETWORK_RESERVEDNETWORKINTERFACESENTRY._options = None
_APPLYNETWORKREQUEST_ANNOTATIONSENTRY._options = None
_RESERVENETWORKINTERFACEREQUEST_ANNOTATIONSENTRY._options = None

_NETWORKSERVICE = _descriptor.ServiceDescriptor(
  name='NetworkService',
  full_name='n0stack.pool.NetworkService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1390,
  serialized_end=1919,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListNetworks',
    full_name='n0stack.pool.NetworkService.ListNetworks',
    index=0,
    containing_service=None,
    input_type=_LISTNETWORKSREQUEST,
    output_type=_LISTNETWORKSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetNetwork',
    full_name='n0stack.pool.NetworkService.GetNetwork',
    index=1,
    containing_service=None,
    input_type=_GETNETWORKREQUEST,
    output_type=_NETWORK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyNetwork',
    full_name='n0stack.pool.NetworkService.ApplyNetwork',
    index=2,
    containing_service=None,
    input_type=_APPLYNETWORKREQUEST,
    output_type=_NETWORK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteNetwork',
    full_name='n0stack.pool.NetworkService.DeleteNetwork',
    index=3,
    containing_service=None,
    input_type=_DELETENETWORKREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReserveNetworkInterface',
    full_name='n0stack.pool.NetworkService.ReserveNetworkInterface',
    index=4,
    containing_service=None,
    input_type=_RESERVENETWORKINTERFACEREQUEST,
    output_type=_NETWORK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReleaseNetworkInterface',
    full_name='n0stack.pool.NetworkService.ReleaseNetworkInterface',
    index=5,
    containing_service=None,
    input_type=_RELEASENETWORKINTERFACEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NETWORKSERVICE)

DESCRIPTOR.services_by_name['NetworkService'] = _NETWORKSERVICE

# @@protoc_insertion_point(module_scope)