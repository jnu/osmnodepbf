# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osmformat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='osmformat.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0fosmformat.proto\"\x80\x02\n\x0bHeaderBlock\x12\x19\n\x04\x62\x62ox\x18\x01 \x01(\x0b\x32\x0b.HeaderBBox\x12\x19\n\x11required_features\x18\x04 \x03(\t\x12\x19\n\x11optional_features\x18\x05 \x03(\t\x12\x16\n\x0ewritingprogram\x18\x10 \x01(\t\x12\x0e\n\x06source\x18\x11 \x01(\t\x12%\n\x1dosmosis_replication_timestamp\x18  \x01(\x03\x12+\n#osmosis_replication_sequence_number\x18! \x01(\x03\x12$\n\x1cosmosis_replication_base_url\x18\" \x01(\t\"F\n\nHeaderBBox\x12\x0c\n\x04left\x18\x01 \x02(\x12\x12\r\n\x05right\x18\x02 \x02(\x12\x12\x0b\n\x03top\x18\x03 \x02(\x12\x12\x0e\n\x06\x62ottom\x18\x04 \x02(\x12\"\xc4\x01\n\x0ePrimitiveBlock\x12!\n\x0bstringtable\x18\x01 \x02(\x0b\x32\x0c.StringTable\x12\'\n\x0eprimitivegroup\x18\x02 \x03(\x0b\x32\x0f.PrimitiveGroup\x12\x18\n\x0bgranularity\x18\x11 \x01(\x05:\x03\x31\x30\x30\x12\x15\n\nlat_offset\x18\x13 \x01(\x03:\x01\x30\x12\x15\n\nlon_offset\x18\x14 \x01(\x03:\x01\x30\x12\x1e\n\x10\x64\x61te_granularity\x18\x12 \x01(\x05:\x04\x31\x30\x30\x30\"\x94\x01\n\x0ePrimitiveGroup\x12\x14\n\x05nodes\x18\x01 \x03(\x0b\x32\x05.Node\x12\x1a\n\x05\x64\x65nse\x18\x02 \x01(\x0b\x32\x0b.DenseNodes\x12\x12\n\x04ways\x18\x03 \x03(\x0b\x32\x04.Way\x12\x1c\n\trelations\x18\x04 \x03(\x0b\x32\t.Relation\x12\x1e\n\nchangesets\x18\x05 \x03(\x0b\x32\n.ChangeSet\"\x18\n\x0bStringTable\x12\t\n\x01s\x18\x01 \x03(\x0c\"q\n\x04Info\x12\x13\n\x07version\x18\x01 \x01(\x05:\x02-1\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x11\n\tchangeset\x18\x03 \x01(\x03\x12\x0b\n\x03uid\x18\x04 \x01(\x05\x12\x10\n\x08user_sid\x18\x05 \x01(\r\x12\x0f\n\x07visible\x18\x06 \x01(\x08\"\x8a\x01\n\tDenseInfo\x12\x13\n\x07version\x18\x01 \x03(\x05\x42\x02\x10\x01\x12\x15\n\ttimestamp\x18\x02 \x03(\x12\x42\x02\x10\x01\x12\x15\n\tchangeset\x18\x03 \x03(\x12\x42\x02\x10\x01\x12\x0f\n\x03uid\x18\x04 \x03(\x11\x42\x02\x10\x01\x12\x14\n\x08user_sid\x18\x05 \x03(\x11\x42\x02\x10\x01\x12\x13\n\x07visible\x18\x06 \x03(\x08\x42\x02\x10\x01\"\x17\n\tChangeSet\x12\n\n\x02id\x18\x01 \x02(\x03\"e\n\x04Node\x12\n\n\x02id\x18\x01 \x02(\x12\x12\x10\n\x04keys\x18\x02 \x03(\rB\x02\x10\x01\x12\x10\n\x04vals\x18\x03 \x03(\rB\x02\x10\x01\x12\x13\n\x04info\x18\x04 \x01(\x0b\x32\x05.Info\x12\x0b\n\x03lat\x18\x08 \x02(\x12\x12\x0b\n\x03lon\x18\t \x02(\x12\"t\n\nDenseNodes\x12\x0e\n\x02id\x18\x01 \x03(\x12\x42\x02\x10\x01\x12\x1d\n\tdenseinfo\x18\x05 \x01(\x0b\x32\n.DenseInfo\x12\x0f\n\x03lat\x18\x08 \x03(\x12\x42\x02\x10\x01\x12\x0f\n\x03lon\x18\t \x03(\x12\x42\x02\x10\x01\x12\x15\n\tkeys_vals\x18\n \x03(\x05\x42\x02\x10\x01\"\\\n\x03Way\x12\n\n\x02id\x18\x01 \x02(\x03\x12\x10\n\x04keys\x18\x02 \x03(\rB\x02\x10\x01\x12\x10\n\x04vals\x18\x03 \x03(\rB\x02\x10\x01\x12\x13\n\x04info\x18\x04 \x01(\x0b\x32\x05.Info\x12\x10\n\x04refs\x18\x08 \x03(\x12\x42\x02\x10\x01\"\xd2\x01\n\x08Relation\x12\n\n\x02id\x18\x01 \x02(\x03\x12\x10\n\x04keys\x18\x02 \x03(\rB\x02\x10\x01\x12\x10\n\x04vals\x18\x03 \x03(\rB\x02\x10\x01\x12\x13\n\x04info\x18\x04 \x01(\x0b\x32\x05.Info\x12\x15\n\troles_sid\x18\x08 \x03(\x05\x42\x02\x10\x01\x12\x12\n\x06memids\x18\t \x03(\x12\x42\x02\x10\x01\x12\'\n\x05types\x18\n \x03(\x0e\x32\x14.Relation.MemberTypeB\x02\x10\x01\"-\n\nMemberType\x12\x08\n\x04NODE\x10\x00\x12\x07\n\x03WAY\x10\x01\x12\x0c\n\x08RELATION\x10\x02')
)



_RELATION_MEMBERTYPE = _descriptor.EnumDescriptor(
  name='MemberType',
  full_name='Relation.MemberType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NODE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELATION', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1488,
  serialized_end=1533,
)
_sym_db.RegisterEnumDescriptor(_RELATION_MEMBERTYPE)


_HEADERBLOCK = _descriptor.Descriptor(
  name='HeaderBlock',
  full_name='HeaderBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bbox', full_name='HeaderBlock.bbox', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required_features', full_name='HeaderBlock.required_features', index=1,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optional_features', full_name='HeaderBlock.optional_features', index=2,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writingprogram', full_name='HeaderBlock.writingprogram', index=3,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='HeaderBlock.source', index=4,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osmosis_replication_timestamp', full_name='HeaderBlock.osmosis_replication_timestamp', index=5,
      number=32, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osmosis_replication_sequence_number', full_name='HeaderBlock.osmosis_replication_sequence_number', index=6,
      number=33, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osmosis_replication_base_url', full_name='HeaderBlock.osmosis_replication_base_url', index=7,
      number=34, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=276,
)


_HEADERBBOX = _descriptor.Descriptor(
  name='HeaderBBox',
  full_name='HeaderBBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left', full_name='HeaderBBox.left', index=0,
      number=1, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right', full_name='HeaderBBox.right', index=1,
      number=2, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top', full_name='HeaderBBox.top', index=2,
      number=3, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='HeaderBBox.bottom', index=3,
      number=4, type=18, cpp_type=2, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=348,
)


_PRIMITIVEBLOCK = _descriptor.Descriptor(
  name='PrimitiveBlock',
  full_name='PrimitiveBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stringtable', full_name='PrimitiveBlock.stringtable', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primitivegroup', full_name='PrimitiveBlock.primitivegroup', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='granularity', full_name='PrimitiveBlock.granularity', index=2,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lat_offset', full_name='PrimitiveBlock.lat_offset', index=3,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon_offset', full_name='PrimitiveBlock.lon_offset', index=4,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_granularity', full_name='PrimitiveBlock.date_granularity', index=5,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1000,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=547,
)


_PRIMITIVEGROUP = _descriptor.Descriptor(
  name='PrimitiveGroup',
  full_name='PrimitiveGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='PrimitiveGroup.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dense', full_name='PrimitiveGroup.dense', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ways', full_name='PrimitiveGroup.ways', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relations', full_name='PrimitiveGroup.relations', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changesets', full_name='PrimitiveGroup.changesets', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=550,
  serialized_end=698,
)


_STRINGTABLE = _descriptor.Descriptor(
  name='StringTable',
  full_name='StringTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='StringTable.s', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=700,
  serialized_end=724,
)


_INFO = _descriptor.Descriptor(
  name='Info',
  full_name='Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='Info.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Info.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changeset', full_name='Info.changeset', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='Info.uid', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_sid', full_name='Info.user_sid', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visible', full_name='Info.visible', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=726,
  serialized_end=839,
)


_DENSEINFO = _descriptor.Descriptor(
  name='DenseInfo',
  full_name='DenseInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='DenseInfo.version', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='DenseInfo.timestamp', index=1,
      number=2, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changeset', full_name='DenseInfo.changeset', index=2,
      number=3, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='DenseInfo.uid', index=3,
      number=4, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_sid', full_name='DenseInfo.user_sid', index=4,
      number=5, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visible', full_name='DenseInfo.visible', index=5,
      number=6, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=842,
  serialized_end=980,
)


_CHANGESET = _descriptor.Descriptor(
  name='ChangeSet',
  full_name='ChangeSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ChangeSet.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=982,
  serialized_end=1005,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Node.id', index=0,
      number=1, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keys', full_name='Node.keys', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vals', full_name='Node.vals', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='Node.info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lat', full_name='Node.lat', index=4,
      number=8, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='Node.lon', index=5,
      number=9, type=18, cpp_type=2, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1007,
  serialized_end=1108,
)


_DENSENODES = _descriptor.Descriptor(
  name='DenseNodes',
  full_name='DenseNodes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='DenseNodes.id', index=0,
      number=1, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='denseinfo', full_name='DenseNodes.denseinfo', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lat', full_name='DenseNodes.lat', index=2,
      number=8, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='DenseNodes.lon', index=3,
      number=9, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keys_vals', full_name='DenseNodes.keys_vals', index=4,
      number=10, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1110,
  serialized_end=1226,
)


_WAY = _descriptor.Descriptor(
  name='Way',
  full_name='Way',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Way.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keys', full_name='Way.keys', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vals', full_name='Way.vals', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='Way.info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refs', full_name='Way.refs', index=4,
      number=8, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1228,
  serialized_end=1320,
)


_RELATION = _descriptor.Descriptor(
  name='Relation',
  full_name='Relation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Relation.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keys', full_name='Relation.keys', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vals', full_name='Relation.vals', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='Relation.info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roles_sid', full_name='Relation.roles_sid', index=4,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memids', full_name='Relation.memids', index=5,
      number=9, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='types', full_name='Relation.types', index=6,
      number=10, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RELATION_MEMBERTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1323,
  serialized_end=1533,
)

_HEADERBLOCK.fields_by_name['bbox'].message_type = _HEADERBBOX
_PRIMITIVEBLOCK.fields_by_name['stringtable'].message_type = _STRINGTABLE
_PRIMITIVEBLOCK.fields_by_name['primitivegroup'].message_type = _PRIMITIVEGROUP
_PRIMITIVEGROUP.fields_by_name['nodes'].message_type = _NODE
_PRIMITIVEGROUP.fields_by_name['dense'].message_type = _DENSENODES
_PRIMITIVEGROUP.fields_by_name['ways'].message_type = _WAY
_PRIMITIVEGROUP.fields_by_name['relations'].message_type = _RELATION
_PRIMITIVEGROUP.fields_by_name['changesets'].message_type = _CHANGESET
_NODE.fields_by_name['info'].message_type = _INFO
_DENSENODES.fields_by_name['denseinfo'].message_type = _DENSEINFO
_WAY.fields_by_name['info'].message_type = _INFO
_RELATION.fields_by_name['info'].message_type = _INFO
_RELATION.fields_by_name['types'].enum_type = _RELATION_MEMBERTYPE
_RELATION_MEMBERTYPE.containing_type = _RELATION
DESCRIPTOR.message_types_by_name['HeaderBlock'] = _HEADERBLOCK
DESCRIPTOR.message_types_by_name['HeaderBBox'] = _HEADERBBOX
DESCRIPTOR.message_types_by_name['PrimitiveBlock'] = _PRIMITIVEBLOCK
DESCRIPTOR.message_types_by_name['PrimitiveGroup'] = _PRIMITIVEGROUP
DESCRIPTOR.message_types_by_name['StringTable'] = _STRINGTABLE
DESCRIPTOR.message_types_by_name['Info'] = _INFO
DESCRIPTOR.message_types_by_name['DenseInfo'] = _DENSEINFO
DESCRIPTOR.message_types_by_name['ChangeSet'] = _CHANGESET
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['DenseNodes'] = _DENSENODES
DESCRIPTOR.message_types_by_name['Way'] = _WAY
DESCRIPTOR.message_types_by_name['Relation'] = _RELATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HeaderBlock = _reflection.GeneratedProtocolMessageType('HeaderBlock', (_message.Message,), dict(
  DESCRIPTOR = _HEADERBLOCK,
  __module__ = 'osmformat_pb2'
  # @@protoc_insertion_point(class_scope:HeaderBlock)
  ))
_sym_db.RegisterMessage(HeaderBlock)

HeaderBBox = _reflection.GeneratedProtocolMessageType('HeaderBBox', (_message.Message,), dict(
  DESCRIPTOR = _HEADERBBOX,
  __module__ = 'osmformat_pb2'
  # @@protoc_insertion_point(class_scope:HeaderBBox)
  ))
_sym_db.RegisterMessage(HeaderBBox)

PrimitiveBlock = _reflection.GeneratedProtocolMessageType('PrimitiveBlock', (_message.Message,), dict(
  DESCRIPTOR = _PRIMITIVEBLOCK,
  __module__ = 'osmformat_pb2'
  # @@protoc_insertion_point(class_scope:PrimitiveBlock)
  ))
_sym_db.RegisterMessage(PrimitiveBlock)

PrimitiveGroup = _reflection.GeneratedProtocolMessageType('PrimitiveGroup', (_message.Message,), dict(
  DESCRIPTOR = _PRIMITIVEGROUP,
  __module__ = 'osmformat_pb2'
  # @@protoc_insertion_point(class_scope:PrimitiveGroup)
  ))
_sym_db.RegisterMessage(PrimitiveGroup)

StringTable = _reflection.GeneratedProtocolMessageType('StringTable', (_message.Message,), dict(
  DESCRIPTOR = _STRINGTABLE,
  __module__ = 'osmformat_pb2'
  # @@protoc_insertion_point(class_scope:StringTable)
  ))
_sym_db.RegisterMessage(StringTable)

Info = _reflection.GeneratedProtocolMessageType('Info', (_message.Message,), dict(
  DESCRIPTOR = _INFO,
  __module__ = 'osmformat_pb2'
  # @@protoc_insertion_point(class_scope:Info)
  ))
_sym_db.RegisterMessage(Info)

DenseInfo = _reflection.GeneratedProtocolMessageType('DenseInfo', (_message.Message,), dict(
  DESCRIPTOR = _DENSEINFO,
  __module__ = 'osmformat_pb2'
  # @@protoc_insertion_point(class_scope:DenseInfo)
  ))
_sym_db.RegisterMessage(DenseInfo)

ChangeSet = _reflection.GeneratedProtocolMessageType('ChangeSet', (_message.Message,), dict(
  DESCRIPTOR = _CHANGESET,
  __module__ = 'osmformat_pb2'
  # @@protoc_insertion_point(class_scope:ChangeSet)
  ))
_sym_db.RegisterMessage(ChangeSet)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
  DESCRIPTOR = _NODE,
  __module__ = 'osmformat_pb2'
  # @@protoc_insertion_point(class_scope:Node)
  ))
_sym_db.RegisterMessage(Node)

DenseNodes = _reflection.GeneratedProtocolMessageType('DenseNodes', (_message.Message,), dict(
  DESCRIPTOR = _DENSENODES,
  __module__ = 'osmformat_pb2'
  # @@protoc_insertion_point(class_scope:DenseNodes)
  ))
_sym_db.RegisterMessage(DenseNodes)

Way = _reflection.GeneratedProtocolMessageType('Way', (_message.Message,), dict(
  DESCRIPTOR = _WAY,
  __module__ = 'osmformat_pb2'
  # @@protoc_insertion_point(class_scope:Way)
  ))
_sym_db.RegisterMessage(Way)

Relation = _reflection.GeneratedProtocolMessageType('Relation', (_message.Message,), dict(
  DESCRIPTOR = _RELATION,
  __module__ = 'osmformat_pb2'
  # @@protoc_insertion_point(class_scope:Relation)
  ))
_sym_db.RegisterMessage(Relation)


_DENSEINFO.fields_by_name['version'].has_options = True
_DENSEINFO.fields_by_name['version']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_DENSEINFO.fields_by_name['timestamp'].has_options = True
_DENSEINFO.fields_by_name['timestamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_DENSEINFO.fields_by_name['changeset'].has_options = True
_DENSEINFO.fields_by_name['changeset']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_DENSEINFO.fields_by_name['uid'].has_options = True
_DENSEINFO.fields_by_name['uid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_DENSEINFO.fields_by_name['user_sid'].has_options = True
_DENSEINFO.fields_by_name['user_sid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_DENSEINFO.fields_by_name['visible'].has_options = True
_DENSEINFO.fields_by_name['visible']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_NODE.fields_by_name['keys'].has_options = True
_NODE.fields_by_name['keys']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_NODE.fields_by_name['vals'].has_options = True
_NODE.fields_by_name['vals']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_DENSENODES.fields_by_name['id'].has_options = True
_DENSENODES.fields_by_name['id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_DENSENODES.fields_by_name['lat'].has_options = True
_DENSENODES.fields_by_name['lat']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_DENSENODES.fields_by_name['lon'].has_options = True
_DENSENODES.fields_by_name['lon']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_DENSENODES.fields_by_name['keys_vals'].has_options = True
_DENSENODES.fields_by_name['keys_vals']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_WAY.fields_by_name['keys'].has_options = True
_WAY.fields_by_name['keys']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_WAY.fields_by_name['vals'].has_options = True
_WAY.fields_by_name['vals']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_WAY.fields_by_name['refs'].has_options = True
_WAY.fields_by_name['refs']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_RELATION.fields_by_name['keys'].has_options = True
_RELATION.fields_by_name['keys']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_RELATION.fields_by_name['vals'].has_options = True
_RELATION.fields_by_name['vals']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_RELATION.fields_by_name['roles_sid'].has_options = True
_RELATION.fields_by_name['roles_sid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_RELATION.fields_by_name['memids'].has_options = True
_RELATION.fields_by_name['memids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_RELATION.fields_by_name['types'].has_options = True
_RELATION.fields_by_name['types']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
