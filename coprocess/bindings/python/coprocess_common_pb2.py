# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: coprocess_common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='coprocess_common.proto',
  package='coprocess',
  syntax='proto3',
  serialized_pb=_b('\n\x16\x63oprocess_common.proto\x12\tcoprocess\"\x1c\n\x0bStringSlice\x12\r\n\x05items\x18\x01 \x03(\t*O\n\x08HookType\x12\x0b\n\x07Unknown\x10\x00\x12\x07\n\x03Pre\x10\x01\x12\x08\n\x04Post\x10\x02\x12\x0f\n\x0bPostKeyAuth\x10\x03\x12\x12\n\x0e\x43ustomKeyCheck\x10\x04\x62\x06proto3')
)

_HOOKTYPE = _descriptor.EnumDescriptor(
  name='HookType',
  full_name='coprocess.HookType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Pre', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Post', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PostKeyAuth', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CustomKeyCheck', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=67,
  serialized_end=146,
)
_sym_db.RegisterEnumDescriptor(_HOOKTYPE)

HookType = enum_type_wrapper.EnumTypeWrapper(_HOOKTYPE)
Unknown = 0
Pre = 1
Post = 2
PostKeyAuth = 3
CustomKeyCheck = 4



_STRINGSLICE = _descriptor.Descriptor(
  name='StringSlice',
  full_name='coprocess.StringSlice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='coprocess.StringSlice.items', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=65,
)

DESCRIPTOR.message_types_by_name['StringSlice'] = _STRINGSLICE
DESCRIPTOR.enum_types_by_name['HookType'] = _HOOKTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StringSlice = _reflection.GeneratedProtocolMessageType('StringSlice', (_message.Message,), dict(
  DESCRIPTOR = _STRINGSLICE,
  __module__ = 'coprocess_common_pb2'
  # @@protoc_insertion_point(class_scope:coprocess.StringSlice)
  ))
_sym_db.RegisterMessage(StringSlice)


# @@protoc_insertion_point(module_scope)
