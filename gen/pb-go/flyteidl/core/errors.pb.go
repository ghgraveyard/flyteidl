// Code generated by protoc-gen-go. DO NOT EDIT.
// source: flyteidl/core/errors.proto

package core // import "github.com/lyft/flyteidl/gen/pb-go/flyteidl/core"

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

// Defines a generic error type that dictates the behavior of the retry strategy.
type ContainerError_Kind int32

const (
	ContainerError_NON_RECOVERABLE ContainerError_Kind = 0
	ContainerError_RECOVERABLE     ContainerError_Kind = 1
)

var ContainerError_Kind_name = map[int32]string{
	0: "NON_RECOVERABLE",
	1: "RECOVERABLE",
}
var ContainerError_Kind_value = map[string]int32{
	"NON_RECOVERABLE": 0,
	"RECOVERABLE":     1,
}

func (x ContainerError_Kind) String() string {
	return proto.EnumName(ContainerError_Kind_name, int32(x))
}
func (ContainerError_Kind) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_errors_33f047924d6d3f90, []int{0, 0}
}

// Error message to propagate detailed errors from container executions to the execution
// engine.
type ContainerError struct {
	// A simplified code for errors, so that we can provide a glossary of all possible errors.
	Code string `protobuf:"bytes,1,opt,name=code,proto3" json:"code,omitempty"`
	// A detailed error message.
	Message string `protobuf:"bytes,2,opt,name=message,proto3" json:"message,omitempty"`
	// An abstract error kind for this error. Defaults to Non_Recoverable if not specified.
	Kind                 ContainerError_Kind `protobuf:"varint,3,opt,name=kind,proto3,enum=flyteidl.core.ContainerError_Kind" json:"kind,omitempty"`
	XXX_NoUnkeyedLiteral struct{}            `json:"-"`
	XXX_unrecognized     []byte              `json:"-"`
	XXX_sizecache        int32               `json:"-"`
}

func (m *ContainerError) Reset()         { *m = ContainerError{} }
func (m *ContainerError) String() string { return proto.CompactTextString(m) }
func (*ContainerError) ProtoMessage()    {}
func (*ContainerError) Descriptor() ([]byte, []int) {
	return fileDescriptor_errors_33f047924d6d3f90, []int{0}
}
func (m *ContainerError) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ContainerError.Unmarshal(m, b)
}
func (m *ContainerError) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ContainerError.Marshal(b, m, deterministic)
}
func (dst *ContainerError) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ContainerError.Merge(dst, src)
}
func (m *ContainerError) XXX_Size() int {
	return xxx_messageInfo_ContainerError.Size(m)
}
func (m *ContainerError) XXX_DiscardUnknown() {
	xxx_messageInfo_ContainerError.DiscardUnknown(m)
}

var xxx_messageInfo_ContainerError proto.InternalMessageInfo

func (m *ContainerError) GetCode() string {
	if m != nil {
		return m.Code
	}
	return ""
}

func (m *ContainerError) GetMessage() string {
	if m != nil {
		return m.Message
	}
	return ""
}

func (m *ContainerError) GetKind() ContainerError_Kind {
	if m != nil {
		return m.Kind
	}
	return ContainerError_NON_RECOVERABLE
}

// Defines the errors.pb file format the container can produce to communicate
// failure reasons to the execution engine.
type ErrorDocument struct {
	// The error raised during execution.
	Error                *ContainerError `protobuf:"bytes,1,opt,name=error,proto3" json:"error,omitempty"`
	XXX_NoUnkeyedLiteral struct{}        `json:"-"`
	XXX_unrecognized     []byte          `json:"-"`
	XXX_sizecache        int32           `json:"-"`
}

func (m *ErrorDocument) Reset()         { *m = ErrorDocument{} }
func (m *ErrorDocument) String() string { return proto.CompactTextString(m) }
func (*ErrorDocument) ProtoMessage()    {}
func (*ErrorDocument) Descriptor() ([]byte, []int) {
	return fileDescriptor_errors_33f047924d6d3f90, []int{1}
}
func (m *ErrorDocument) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ErrorDocument.Unmarshal(m, b)
}
func (m *ErrorDocument) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ErrorDocument.Marshal(b, m, deterministic)
}
func (dst *ErrorDocument) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ErrorDocument.Merge(dst, src)
}
func (m *ErrorDocument) XXX_Size() int {
	return xxx_messageInfo_ErrorDocument.Size(m)
}
func (m *ErrorDocument) XXX_DiscardUnknown() {
	xxx_messageInfo_ErrorDocument.DiscardUnknown(m)
}

var xxx_messageInfo_ErrorDocument proto.InternalMessageInfo

func (m *ErrorDocument) GetError() *ContainerError {
	if m != nil {
		return m.Error
	}
	return nil
}

func init() {
	proto.RegisterType((*ContainerError)(nil), "flyteidl.core.ContainerError")
	proto.RegisterType((*ErrorDocument)(nil), "flyteidl.core.ErrorDocument")
	proto.RegisterEnum("flyteidl.core.ContainerError_Kind", ContainerError_Kind_name, ContainerError_Kind_value)
}

func init() { proto.RegisterFile("flyteidl/core/errors.proto", fileDescriptor_errors_33f047924d6d3f90) }

var fileDescriptor_errors_33f047924d6d3f90 = []byte{
	// 245 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0x92, 0x4a, 0xcb, 0xa9, 0x2c,
	0x49, 0xcd, 0x4c, 0xc9, 0xd1, 0x4f, 0xce, 0x2f, 0x4a, 0xd5, 0x4f, 0x2d, 0x2a, 0xca, 0x2f, 0x2a,
	0xd6, 0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x17, 0xe2, 0x85, 0xc9, 0xe9, 0x81, 0xe4, 0x94, 0x96, 0x30,
	0x72, 0xf1, 0x39, 0xe7, 0xe7, 0x95, 0x24, 0x66, 0xe6, 0xa5, 0x16, 0xb9, 0x82, 0x14, 0x0a, 0x09,
	0x71, 0xb1, 0x24, 0xe7, 0xa7, 0xa4, 0x4a, 0x30, 0x2a, 0x30, 0x6a, 0x70, 0x06, 0x81, 0xd9, 0x42,
	0x12, 0x5c, 0xec, 0xb9, 0xa9, 0xc5, 0xc5, 0x89, 0xe9, 0xa9, 0x12, 0x4c, 0x60, 0x61, 0x18, 0x57,
	0xc8, 0x8c, 0x8b, 0x25, 0x3b, 0x33, 0x2f, 0x45, 0x82, 0x59, 0x81, 0x51, 0x83, 0xcf, 0x48, 0x49,
	0x0f, 0xc5, 0x78, 0x3d, 0x54, 0xa3, 0xf5, 0xbc, 0x33, 0xf3, 0x52, 0x82, 0xc0, 0xea, 0x95, 0x74,
	0xb8, 0x58, 0x40, 0x3c, 0x21, 0x61, 0x2e, 0x7e, 0x3f, 0x7f, 0xbf, 0xf8, 0x20, 0x57, 0x67, 0xff,
	0x30, 0xd7, 0x20, 0x47, 0x27, 0x1f, 0x57, 0x01, 0x06, 0x21, 0x7e, 0x2e, 0x6e, 0x64, 0x01, 0x46,
	0x25, 0x17, 0x2e, 0x5e, 0xb0, 0x09, 0x2e, 0xf9, 0xc9, 0xa5, 0xb9, 0xa9, 0x79, 0x25, 0x42, 0xc6,
	0x5c, 0xac, 0x60, 0x6f, 0x81, 0x5d, 0xc9, 0x6d, 0x24, 0x8b, 0xd7, 0xde, 0x20, 0x88, 0x5a, 0x27,
	0xa3, 0x28, 0x83, 0xf4, 0xcc, 0x92, 0x8c, 0xd2, 0x24, 0xbd, 0xe4, 0xfc, 0x5c, 0xfd, 0x9c, 0xca,
	0xb4, 0x12, 0x7d, 0x78, 0x48, 0xa5, 0xa7, 0xe6, 0xe9, 0x17, 0x24, 0xe9, 0xa6, 0xe7, 0xeb, 0xa3,
	0x04, 0x5e, 0x12, 0x1b, 0x38, 0xd8, 0x8c, 0x01, 0x01, 0x00, 0x00, 0xff, 0xff, 0xf6, 0xbe, 0xb8,
	0x64, 0x54, 0x01, 0x00, 0x00,
}
