# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='uclite.proto',
  package='uclite',
  serialized_pb='\n\x0cuclite.proto\x12\x06uclite\" \n\x02Kv\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"\x84\x01\n\tComponent\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.uclite.ComponentType\x12\x19\n\x05\x61ttrs\x18\x02 \x03(\x0b\x32\n.uclite.Kv\x12#\n\x08\x63hildren\x18\x03 \x03(\x0b\x32\x11.uclite.Component\x12\x12\n\ninner_text\x18\x04 \x01(\t\"S\n\x06\x41\x63tion\x12\x0b\n\x03\x63md\x18\x01 \x02(\t\x12\x0e\n\x06target\x18\x02 \x02(\t\x12\x1f\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\x11.uclite.Component\x12\x0b\n\x03msg\x18\x04 \x01(\t\")\n\x06Result\x12\x1f\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32\x0e.uclite.Action*\x88\x03\n\rComponentType\x12\x0f\n\x0b\x43omPageType\x10\x00\x12\x12\n\x0e\x43omToolbarType\x10\x01\x12\x11\n\rComTabbarType\x10\x02\x12\x0f\n\x0b\x43omCardType\x10\x03\x12\x0f\n\x0b\x43omNewsType\x10\x04\x12\x12\n\x0e\x43omFlexboxType\x10\x05\x12\x0f\n\x0b\x43omListType\x10\x06\x12\x11\n\rComButtonType\x10\x07\x12\x0f\n\x0b\x43omTextType\x10\x08\x12\x10\n\x0c\x43omImageType\x10\t\x12\x0f\n\x0b\x43omInfoType\x10\n\x12\x0e\n\nComNavType\x10\x0b\x12\x0c\n\x08\x43omHType\x10\x0c\x12\x0e\n\nComWebType\x10\r\x12\x11\n\rComFooterType\x10\x0e\x12\x10\n\x0c\x43omInputType\x10\x0f\x12\x13\n\x0f\x43omCheckboxType\x10\x10\x12\x10\n\x0c\x43omStyleType\x10\x11\x12\x13\n\x0f\x43omReadmoreType\x10\x12\x12\x0f\n\x0b\x43omItemType\x10\x13\x12\x11\n\rComFBCardType\x10\x14\x42\x30\n\"com.uc.application.uclite.protobufB\nComponents')

_COMPONENTTYPE = descriptor.EnumDescriptor(
  name='ComponentType',
  full_name='uclite.ComponentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='ComPageType', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComToolbarType', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComTabbarType', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComCardType', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComNewsType', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComFlexboxType', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComListType', index=6, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComButtonType', index=7, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComTextType', index=8, number=8,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComImageType', index=9, number=9,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComInfoType', index=10, number=10,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComNavType', index=11, number=11,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComHType', index=12, number=12,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComWebType', index=13, number=13,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComFooterType', index=14, number=14,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComInputType', index=15, number=15,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComCheckboxType', index=16, number=16,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComStyleType', index=17, number=17,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComReadmoreType', index=18, number=18,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComItemType', index=19, number=19,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ComFBCardType', index=20, number=20,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=322,
  serialized_end=714,
)


ComPageType = 0
ComToolbarType = 1
ComTabbarType = 2
ComCardType = 3
ComNewsType = 4
ComFlexboxType = 5
ComListType = 6
ComButtonType = 7
ComTextType = 8
ComImageType = 9
ComInfoType = 10
ComNavType = 11
ComHType = 12
ComWebType = 13
ComFooterType = 14
ComInputType = 15
ComCheckboxType = 16
ComStyleType = 17
ComReadmoreType = 18
ComItemType = 19
ComFBCardType = 20



_KV = descriptor.Descriptor(
  name='Kv',
  full_name='uclite.Kv',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='uclite.Kv.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='uclite.Kv.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=24,
  serialized_end=56,
)


_COMPONENT = descriptor.Descriptor(
  name='Component',
  full_name='uclite.Component',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='uclite.Component.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attrs', full_name='uclite.Component.attrs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='children', full_name='uclite.Component.children', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='inner_text', full_name='uclite.Component.inner_text', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=59,
  serialized_end=191,
)


_ACTION = descriptor.Descriptor(
  name='Action',
  full_name='uclite.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cmd', full_name='uclite.Action.cmd', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target', full_name='uclite.Action.target', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='uclite.Action.data', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='msg', full_name='uclite.Action.msg', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=193,
  serialized_end=276,
)


_RESULT = descriptor.Descriptor(
  name='Result',
  full_name='uclite.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='actions', full_name='uclite.Result.actions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=278,
  serialized_end=319,
)


_COMPONENT.fields_by_name['type'].enum_type = _COMPONENTTYPE
_COMPONENT.fields_by_name['attrs'].message_type = _KV
_COMPONENT.fields_by_name['children'].message_type = _COMPONENT
_ACTION.fields_by_name['data'].message_type = _COMPONENT
_RESULT.fields_by_name['actions'].message_type = _ACTION

class Kv(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KV
  
  # @@protoc_insertion_point(class_scope:uclite.Kv)

class Component(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMPONENT
  
  # @@protoc_insertion_point(class_scope:uclite.Component)

class Action(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACTION
  
  # @@protoc_insertion_point(class_scope:uclite.Action)

class Result(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESULT
  
  # @@protoc_insertion_point(class_scope:uclite.Result)

# @@protoc_insertion_point(module_scope)
