# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.core import execution_pb2 as flyteidl_dot_core_dot_execution__pb2
from flyteidl.core import identifier_pb2 as flyteidl_dot_core_dot_identifier__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/admin/common.proto',
  package='flyteidl.admin',
  syntax='proto3',
  serialized_pb=_b('\n\x1b\x66lyteidl/admin/common.proto\x12\x0e\x66lyteidl.admin\x1a\x1d\x66lyteidl/core/execution.proto\x1a\x1e\x66lyteidl/core/identifier.proto\"F\n\x15NamedEntityIdentifier\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"r\n\x04Sort\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x31\n\tdirection\x18\x02 \x01(\x0e\x32\x1e.flyteidl.admin.Sort.Direction\"*\n\tDirection\x12\x0e\n\nDESCENDING\x10\x00\x12\r\n\tASCENDING\x10\x01\"\x88\x01\n NamedEntityIdentifierListRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\r\x12\r\n\x05token\x18\x04 \x01(\t\x12%\n\x07sort_by\x18\x05 \x01(\x0b\x32\x14.flyteidl.admin.Sort\"c\n\x19NamedEntityIdentifierList\x12\x37\n\x08\x65ntities\x18\x01 \x03(\x0b\x32%.flyteidl.admin.NamedEntityIdentifier\x12\r\n\x05token\x18\x02 \x01(\t\"9\n\x10ObjectGetRequest\x12%\n\x02id\x18\x01 \x01(\x0b\x32\x19.flyteidl.core.Identifier\"\x9e\x01\n\x13ResourceListRequest\x12\x31\n\x02id\x18\x01 \x01(\x0b\x32%.flyteidl.admin.NamedEntityIdentifier\x12\r\n\x05limit\x18\x02 \x01(\r\x12\r\n\x05token\x18\x03 \x01(\t\x12\x0f\n\x07\x66ilters\x18\x04 \x01(\t\x12%\n\x07sort_by\x18\x05 \x01(\x0b\x32\x14.flyteidl.admin.Sort\"-\n\x11\x45mailNotification\x12\x18\n\x10recipients_email\x18\x01 \x03(\t\"1\n\x15PagerDutyNotification\x12\x18\n\x10recipients_email\x18\x01 \x03(\t\"-\n\x11SlackNotification\x12\x18\n\x10recipients_email\x18\x01 \x03(\t\"\xf3\x01\n\x0cNotification\x12\x36\n\x06phases\x18\x01 \x03(\x0e\x32&.flyteidl.core.WorkflowExecution.Phase\x12\x32\n\x05\x65mail\x18\x02 \x01(\x0b\x32!.flyteidl.admin.EmailNotificationH\x00\x12;\n\npager_duty\x18\x03 \x01(\x0b\x32%.flyteidl.admin.PagerDutyNotificationH\x00\x12\x32\n\x05slack\x18\x04 \x01(\x0b\x32!.flyteidl.admin.SlackNotificationH\x00\x42\x06\n\x04type\"%\n\x07UrlBlob\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05\x62ytes\x18\x02 \x01(\x03\"k\n\x06Labels\x12\x32\n\x06values\x18\x01 \x03(\x0b\x32\".flyteidl.admin.Labels.ValuesEntry\x1a-\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"u\n\x0b\x41nnotations\x12\x37\n\x06values\x18\x01 \x03(\x0b\x32\'.flyteidl.admin.Annotations.ValuesEntry\x1a-\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x33Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/adminb\x06proto3')
  ,
  dependencies=[flyteidl_dot_core_dot_execution__pb2.DESCRIPTOR,flyteidl_dot_core_dot_identifier__pb2.DESCRIPTOR,])



_SORT_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='flyteidl.admin.Sort.Direction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DESCENDING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASCENDING', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=254,
  serialized_end=296,
)
_sym_db.RegisterEnumDescriptor(_SORT_DIRECTION)


_NAMEDENTITYIDENTIFIER = _descriptor.Descriptor(
  name='NamedEntityIdentifier',
  full_name='flyteidl.admin.NamedEntityIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='flyteidl.admin.NamedEntityIdentifier.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='flyteidl.admin.NamedEntityIdentifier.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flyteidl.admin.NamedEntityIdentifier.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=110,
  serialized_end=180,
)


_SORT = _descriptor.Descriptor(
  name='Sort',
  full_name='flyteidl.admin.Sort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='flyteidl.admin.Sort.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='flyteidl.admin.Sort.direction', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SORT_DIRECTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=296,
)


_NAMEDENTITYIDENTIFIERLISTREQUEST = _descriptor.Descriptor(
  name='NamedEntityIdentifierListRequest',
  full_name='flyteidl.admin.NamedEntityIdentifierListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='flyteidl.admin.NamedEntityIdentifierListRequest.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='flyteidl.admin.NamedEntityIdentifierListRequest.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='flyteidl.admin.NamedEntityIdentifierListRequest.limit', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='flyteidl.admin.NamedEntityIdentifierListRequest.token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort_by', full_name='flyteidl.admin.NamedEntityIdentifierListRequest.sort_by', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=299,
  serialized_end=435,
)


_NAMEDENTITYIDENTIFIERLIST = _descriptor.Descriptor(
  name='NamedEntityIdentifierList',
  full_name='flyteidl.admin.NamedEntityIdentifierList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='flyteidl.admin.NamedEntityIdentifierList.entities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='flyteidl.admin.NamedEntityIdentifierList.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=437,
  serialized_end=536,
)


_OBJECTGETREQUEST = _descriptor.Descriptor(
  name='ObjectGetRequest',
  full_name='flyteidl.admin.ObjectGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.ObjectGetRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=538,
  serialized_end=595,
)


_RESOURCELISTREQUEST = _descriptor.Descriptor(
  name='ResourceListRequest',
  full_name='flyteidl.admin.ResourceListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.ResourceListRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='flyteidl.admin.ResourceListRequest.limit', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='flyteidl.admin.ResourceListRequest.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filters', full_name='flyteidl.admin.ResourceListRequest.filters', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort_by', full_name='flyteidl.admin.ResourceListRequest.sort_by', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=598,
  serialized_end=756,
)


_EMAILNOTIFICATION = _descriptor.Descriptor(
  name='EmailNotification',
  full_name='flyteidl.admin.EmailNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipients_email', full_name='flyteidl.admin.EmailNotification.recipients_email', index=0,
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
  serialized_start=758,
  serialized_end=803,
)


_PAGERDUTYNOTIFICATION = _descriptor.Descriptor(
  name='PagerDutyNotification',
  full_name='flyteidl.admin.PagerDutyNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipients_email', full_name='flyteidl.admin.PagerDutyNotification.recipients_email', index=0,
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
  serialized_start=805,
  serialized_end=854,
)


_SLACKNOTIFICATION = _descriptor.Descriptor(
  name='SlackNotification',
  full_name='flyteidl.admin.SlackNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipients_email', full_name='flyteidl.admin.SlackNotification.recipients_email', index=0,
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
  serialized_start=856,
  serialized_end=901,
)


_NOTIFICATION = _descriptor.Descriptor(
  name='Notification',
  full_name='flyteidl.admin.Notification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phases', full_name='flyteidl.admin.Notification.phases', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='flyteidl.admin.Notification.email', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pager_duty', full_name='flyteidl.admin.Notification.pager_duty', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slack', full_name='flyteidl.admin.Notification.slack', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='type', full_name='flyteidl.admin.Notification.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=904,
  serialized_end=1147,
)


_URLBLOB = _descriptor.Descriptor(
  name='UrlBlob',
  full_name='flyteidl.admin.UrlBlob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='flyteidl.admin.UrlBlob.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='flyteidl.admin.UrlBlob.bytes', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1149,
  serialized_end=1186,
)


_LABELS_VALUESENTRY = _descriptor.Descriptor(
  name='ValuesEntry',
  full_name='flyteidl.admin.Labels.ValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='flyteidl.admin.Labels.ValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='flyteidl.admin.Labels.ValuesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1250,
  serialized_end=1295,
)

_LABELS = _descriptor.Descriptor(
  name='Labels',
  full_name='flyteidl.admin.Labels',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='flyteidl.admin.Labels.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LABELS_VALUESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1188,
  serialized_end=1295,
)


_ANNOTATIONS_VALUESENTRY = _descriptor.Descriptor(
  name='ValuesEntry',
  full_name='flyteidl.admin.Annotations.ValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='flyteidl.admin.Annotations.ValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='flyteidl.admin.Annotations.ValuesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1250,
  serialized_end=1295,
)

_ANNOTATIONS = _descriptor.Descriptor(
  name='Annotations',
  full_name='flyteidl.admin.Annotations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='flyteidl.admin.Annotations.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ANNOTATIONS_VALUESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1297,
  serialized_end=1414,
)

_SORT.fields_by_name['direction'].enum_type = _SORT_DIRECTION
_SORT_DIRECTION.containing_type = _SORT
_NAMEDENTITYIDENTIFIERLISTREQUEST.fields_by_name['sort_by'].message_type = _SORT
_NAMEDENTITYIDENTIFIERLIST.fields_by_name['entities'].message_type = _NAMEDENTITYIDENTIFIER
_OBJECTGETREQUEST.fields_by_name['id'].message_type = flyteidl_dot_core_dot_identifier__pb2._IDENTIFIER
_RESOURCELISTREQUEST.fields_by_name['id'].message_type = _NAMEDENTITYIDENTIFIER
_RESOURCELISTREQUEST.fields_by_name['sort_by'].message_type = _SORT
_NOTIFICATION.fields_by_name['phases'].enum_type = flyteidl_dot_core_dot_execution__pb2._WORKFLOWEXECUTION_PHASE
_NOTIFICATION.fields_by_name['email'].message_type = _EMAILNOTIFICATION
_NOTIFICATION.fields_by_name['pager_duty'].message_type = _PAGERDUTYNOTIFICATION
_NOTIFICATION.fields_by_name['slack'].message_type = _SLACKNOTIFICATION
_NOTIFICATION.oneofs_by_name['type'].fields.append(
  _NOTIFICATION.fields_by_name['email'])
_NOTIFICATION.fields_by_name['email'].containing_oneof = _NOTIFICATION.oneofs_by_name['type']
_NOTIFICATION.oneofs_by_name['type'].fields.append(
  _NOTIFICATION.fields_by_name['pager_duty'])
_NOTIFICATION.fields_by_name['pager_duty'].containing_oneof = _NOTIFICATION.oneofs_by_name['type']
_NOTIFICATION.oneofs_by_name['type'].fields.append(
  _NOTIFICATION.fields_by_name['slack'])
_NOTIFICATION.fields_by_name['slack'].containing_oneof = _NOTIFICATION.oneofs_by_name['type']
_LABELS_VALUESENTRY.containing_type = _LABELS
_LABELS.fields_by_name['values'].message_type = _LABELS_VALUESENTRY
_ANNOTATIONS_VALUESENTRY.containing_type = _ANNOTATIONS
_ANNOTATIONS.fields_by_name['values'].message_type = _ANNOTATIONS_VALUESENTRY
DESCRIPTOR.message_types_by_name['NamedEntityIdentifier'] = _NAMEDENTITYIDENTIFIER
DESCRIPTOR.message_types_by_name['Sort'] = _SORT
DESCRIPTOR.message_types_by_name['NamedEntityIdentifierListRequest'] = _NAMEDENTITYIDENTIFIERLISTREQUEST
DESCRIPTOR.message_types_by_name['NamedEntityIdentifierList'] = _NAMEDENTITYIDENTIFIERLIST
DESCRIPTOR.message_types_by_name['ObjectGetRequest'] = _OBJECTGETREQUEST
DESCRIPTOR.message_types_by_name['ResourceListRequest'] = _RESOURCELISTREQUEST
DESCRIPTOR.message_types_by_name['EmailNotification'] = _EMAILNOTIFICATION
DESCRIPTOR.message_types_by_name['PagerDutyNotification'] = _PAGERDUTYNOTIFICATION
DESCRIPTOR.message_types_by_name['SlackNotification'] = _SLACKNOTIFICATION
DESCRIPTOR.message_types_by_name['Notification'] = _NOTIFICATION
DESCRIPTOR.message_types_by_name['UrlBlob'] = _URLBLOB
DESCRIPTOR.message_types_by_name['Labels'] = _LABELS
DESCRIPTOR.message_types_by_name['Annotations'] = _ANNOTATIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NamedEntityIdentifier = _reflection.GeneratedProtocolMessageType('NamedEntityIdentifier', (_message.Message,), dict(
  DESCRIPTOR = _NAMEDENTITYIDENTIFIER,
  __module__ = 'flyteidl.admin.common_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NamedEntityIdentifier)
  ))
_sym_db.RegisterMessage(NamedEntityIdentifier)

Sort = _reflection.GeneratedProtocolMessageType('Sort', (_message.Message,), dict(
  DESCRIPTOR = _SORT,
  __module__ = 'flyteidl.admin.common_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.Sort)
  ))
_sym_db.RegisterMessage(Sort)

NamedEntityIdentifierListRequest = _reflection.GeneratedProtocolMessageType('NamedEntityIdentifierListRequest', (_message.Message,), dict(
  DESCRIPTOR = _NAMEDENTITYIDENTIFIERLISTREQUEST,
  __module__ = 'flyteidl.admin.common_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NamedEntityIdentifierListRequest)
  ))
_sym_db.RegisterMessage(NamedEntityIdentifierListRequest)

NamedEntityIdentifierList = _reflection.GeneratedProtocolMessageType('NamedEntityIdentifierList', (_message.Message,), dict(
  DESCRIPTOR = _NAMEDENTITYIDENTIFIERLIST,
  __module__ = 'flyteidl.admin.common_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NamedEntityIdentifierList)
  ))
_sym_db.RegisterMessage(NamedEntityIdentifierList)

ObjectGetRequest = _reflection.GeneratedProtocolMessageType('ObjectGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTGETREQUEST,
  __module__ = 'flyteidl.admin.common_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.ObjectGetRequest)
  ))
_sym_db.RegisterMessage(ObjectGetRequest)

ResourceListRequest = _reflection.GeneratedProtocolMessageType('ResourceListRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCELISTREQUEST,
  __module__ = 'flyteidl.admin.common_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.ResourceListRequest)
  ))
_sym_db.RegisterMessage(ResourceListRequest)

EmailNotification = _reflection.GeneratedProtocolMessageType('EmailNotification', (_message.Message,), dict(
  DESCRIPTOR = _EMAILNOTIFICATION,
  __module__ = 'flyteidl.admin.common_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.EmailNotification)
  ))
_sym_db.RegisterMessage(EmailNotification)

PagerDutyNotification = _reflection.GeneratedProtocolMessageType('PagerDutyNotification', (_message.Message,), dict(
  DESCRIPTOR = _PAGERDUTYNOTIFICATION,
  __module__ = 'flyteidl.admin.common_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.PagerDutyNotification)
  ))
_sym_db.RegisterMessage(PagerDutyNotification)

SlackNotification = _reflection.GeneratedProtocolMessageType('SlackNotification', (_message.Message,), dict(
  DESCRIPTOR = _SLACKNOTIFICATION,
  __module__ = 'flyteidl.admin.common_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.SlackNotification)
  ))
_sym_db.RegisterMessage(SlackNotification)

Notification = _reflection.GeneratedProtocolMessageType('Notification', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFICATION,
  __module__ = 'flyteidl.admin.common_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.Notification)
  ))
_sym_db.RegisterMessage(Notification)

UrlBlob = _reflection.GeneratedProtocolMessageType('UrlBlob', (_message.Message,), dict(
  DESCRIPTOR = _URLBLOB,
  __module__ = 'flyteidl.admin.common_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.UrlBlob)
  ))
_sym_db.RegisterMessage(UrlBlob)

Labels = _reflection.GeneratedProtocolMessageType('Labels', (_message.Message,), dict(

  ValuesEntry = _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), dict(
    DESCRIPTOR = _LABELS_VALUESENTRY,
    __module__ = 'flyteidl.admin.common_pb2'
    # @@protoc_insertion_point(class_scope:flyteidl.admin.Labels.ValuesEntry)
    ))
  ,
  DESCRIPTOR = _LABELS,
  __module__ = 'flyteidl.admin.common_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.Labels)
  ))
_sym_db.RegisterMessage(Labels)
_sym_db.RegisterMessage(Labels.ValuesEntry)

Annotations = _reflection.GeneratedProtocolMessageType('Annotations', (_message.Message,), dict(

  ValuesEntry = _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), dict(
    DESCRIPTOR = _ANNOTATIONS_VALUESENTRY,
    __module__ = 'flyteidl.admin.common_pb2'
    # @@protoc_insertion_point(class_scope:flyteidl.admin.Annotations.ValuesEntry)
    ))
  ,
  DESCRIPTOR = _ANNOTATIONS,
  __module__ = 'flyteidl.admin.common_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.Annotations)
  ))
_sym_db.RegisterMessage(Annotations)
_sym_db.RegisterMessage(Annotations.ValuesEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/admin'))
_LABELS_VALUESENTRY.has_options = True
_LABELS_VALUESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_ANNOTATIONS_VALUESENTRY.has_options = True
_ANNOTATIONS_VALUESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
