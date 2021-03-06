// Code generated by protoc-gen-go. DO NOT EDIT.
// source: n0stack/budget/v0/compute.proto

package pbudget

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	_ "github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger/options"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type Compute struct {
	Annotations          map[string]string `protobuf:"bytes,1,rep,name=annotations,proto3" json:"annotations,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	RequestCpuMilliCore  uint32            `protobuf:"varint,2,opt,name=request_cpu_milli_core,json=requestCpuMilliCore,proto3" json:"request_cpu_milli_core,omitempty"`
	LimitCpuMilliCore    uint32            `protobuf:"varint,3,opt,name=limit_cpu_milli_core,json=limitCpuMilliCore,proto3" json:"limit_cpu_milli_core,omitempty"`
	RequestMemoryBytes   uint64            `protobuf:"varint,4,opt,name=request_memory_bytes,json=requestMemoryBytes,proto3" json:"request_memory_bytes,omitempty"`
	LimitMemoryBytes     uint64            `protobuf:"varint,5,opt,name=limit_memory_bytes,json=limitMemoryBytes,proto3" json:"limit_memory_bytes,omitempty"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *Compute) Reset()         { *m = Compute{} }
func (m *Compute) String() string { return proto.CompactTextString(m) }
func (*Compute) ProtoMessage()    {}
func (*Compute) Descriptor() ([]byte, []int) {
	return fileDescriptor_4578c4e7d30b73f2, []int{0}
}

func (m *Compute) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Compute.Unmarshal(m, b)
}
func (m *Compute) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Compute.Marshal(b, m, deterministic)
}
func (m *Compute) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Compute.Merge(m, src)
}
func (m *Compute) XXX_Size() int {
	return xxx_messageInfo_Compute.Size(m)
}
func (m *Compute) XXX_DiscardUnknown() {
	xxx_messageInfo_Compute.DiscardUnknown(m)
}

var xxx_messageInfo_Compute proto.InternalMessageInfo

func (m *Compute) GetAnnotations() map[string]string {
	if m != nil {
		return m.Annotations
	}
	return nil
}

func (m *Compute) GetRequestCpuMilliCore() uint32 {
	if m != nil {
		return m.RequestCpuMilliCore
	}
	return 0
}

func (m *Compute) GetLimitCpuMilliCore() uint32 {
	if m != nil {
		return m.LimitCpuMilliCore
	}
	return 0
}

func (m *Compute) GetRequestMemoryBytes() uint64 {
	if m != nil {
		return m.RequestMemoryBytes
	}
	return 0
}

func (m *Compute) GetLimitMemoryBytes() uint64 {
	if m != nil {
		return m.LimitMemoryBytes
	}
	return 0
}

func init() {
	proto.RegisterType((*Compute)(nil), "n0stack.budget.v0.Compute")
	proto.RegisterMapType((map[string]string)(nil), "n0stack.budget.v0.Compute.AnnotationsEntry")
}

func init() { proto.RegisterFile("n0stack/budget/v0/compute.proto", fileDescriptor_4578c4e7d30b73f2) }

var fileDescriptor_4578c4e7d30b73f2 = []byte{
	// 365 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x74, 0x92, 0x41, 0x6f, 0xba, 0x30,
	0x18, 0xc6, 0x53, 0xd4, 0xbf, 0xb1, 0xe6, 0x9f, 0x60, 0x67, 0x16, 0xe2, 0x65, 0xc4, 0x13, 0xd9,
	0xb4, 0x25, 0x7a, 0x98, 0x71, 0xc9, 0x12, 0x35, 0x3b, 0x7a, 0xe1, 0xb8, 0x0b, 0x01, 0xd6, 0x20,
	0x13, 0xda, 0x0e, 0x8a, 0x0b, 0x5f, 0x63, 0x1f, 0x60, 0x1f, 0x6d, 0x9f, 0x65, 0xb1, 0xc5, 0xa9,
	0x33, 0x3b, 0xf1, 0xc0, 0xef, 0x79, 0xde, 0x97, 0xb7, 0x6f, 0xe1, 0x0d, 0x73, 0x0b, 0x19, 0x44,
	0x5b, 0x12, 0x96, 0x2f, 0x31, 0x95, 0x64, 0xe7, 0x92, 0x88, 0x67, 0xa2, 0x94, 0x14, 0x8b, 0x9c,
	0x4b, 0x8e, 0x7a, 0xb5, 0x01, 0x6b, 0x03, 0xde, 0xb9, 0x83, 0x91, 0x22, 0xd1, 0x38, 0xa6, 0x6c,
	0x5c, 0xbc, 0x07, 0x71, 0x4c, 0x73, 0xc2, 0x85, 0x4c, 0x38, 0x2b, 0x48, 0xc0, 0x18, 0x97, 0x81,
	0xd2, 0xba, 0xc0, 0xf0, 0xcb, 0x80, 0xed, 0x95, 0x2e, 0x89, 0xd6, 0xb0, 0x7b, 0x62, 0xb0, 0x80,
	0xdd, 0x70, 0xba, 0x93, 0x3b, 0x7c, 0xd1, 0x02, 0xd7, 0x01, 0xbc, 0x38, 0xba, 0x9f, 0x98, 0xcc,
	0x2b, 0xef, 0x34, 0x8f, 0xa6, 0xf0, 0x3a, 0xa7, 0x6f, 0x25, 0x2d, 0xa4, 0x1f, 0x89, 0xd2, 0xcf,
	0x92, 0x34, 0x4d, 0xfc, 0x88, 0xe7, 0xd4, 0x32, 0x6c, 0xe0, 0xfc, 0xf7, 0xae, 0x6a, 0xba, 0x12,
	0xe5, 0x7a, 0xcf, 0x56, 0x3c, 0xa7, 0x88, 0xc0, 0x7e, 0x9a, 0x64, 0xc9, 0x45, 0xa4, 0xa1, 0x22,
	0x3d, 0xc5, 0xce, 0x02, 0x2e, 0xec, 0x1f, 0xba, 0x64, 0x34, 0xe3, 0x79, 0xe5, 0x87, 0x95, 0xa4,
	0x85, 0xd5, 0xb4, 0x81, 0xd3, 0xf4, 0x50, 0xcd, 0xd6, 0x0a, 0x2d, 0xf7, 0x04, 0x8d, 0x20, 0xd2,
	0x2d, 0xce, 0xfc, 0x2d, 0xe5, 0x37, 0x15, 0x39, 0x71, 0x0f, 0x1e, 0xa1, 0xf9, 0x7b, 0x4c, 0x64,
	0xc2, 0xc6, 0x96, 0x56, 0x16, 0xb0, 0x81, 0xd3, 0xf1, 0xf6, 0x12, 0xf5, 0x61, 0x6b, 0x17, 0xa4,
	0xa5, 0x1e, 0xad, 0xe3, 0xe9, 0x97, 0xb9, 0x31, 0x03, 0xcb, 0x4f, 0xf0, 0xb1, 0x08, 0xd1, 0x0c,
	0xb6, 0xeb, 0x63, 0x1c, 0x8e, 0x7f, 0x24, 0x1a, 0x6e, 0xa4, 0x14, 0xc5, 0x9c, 0x90, 0x38, 0x91,
	0x9b, 0x32, 0xc4, 0x11, 0xcf, 0xc8, 0x61, 0xe3, 0xf5, 0xf3, 0xd6, 0x00, 0xc6, 0xc4, 0x0c, 0x84,
	0x48, 0x93, 0x48, 0xfd, 0x02, 0x79, 0x2d, 0x38, 0x9b, 0x5f, 0x7c, 0x79, 0xbe, 0xff, 0xbb, 0x06,
	0x61, 0xae, 0x5a, 0x36, 0x8e, 0xf9, 0xf1, 0x22, 0x3d, 0x08, 0x2d, 0xc3, 0x7f, 0x8a, 0x4d, 0xbf,
	0x03, 0x00, 0x00, 0xff, 0xff, 0xb4, 0x9e, 0x5d, 0x32, 0x6c, 0x02, 0x00, 0x00,
}
