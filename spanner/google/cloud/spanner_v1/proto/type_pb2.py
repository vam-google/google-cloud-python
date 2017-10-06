# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/spanner_v1/proto/type.proto

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


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/spanner_v1/proto/type.proto',
  package='google.spanner.v1',
  syntax='proto3',
  serialized_pb=_b('\n(google/cloud/spanner_v1/proto/type.proto\x12\x11google.spanner.v1\x1a\x1cgoogle/api/annotations.proto\"\x9a\x01\n\x04Type\x12)\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x1b.google.spanner.v1.TypeCode\x12\x33\n\x12\x61rray_element_type\x18\x02 \x01(\x0b\x32\x17.google.spanner.v1.Type\x12\x32\n\x0bstruct_type\x18\x03 \x01(\x0b\x32\x1d.google.spanner.v1.StructType\"\x7f\n\nStructType\x12\x33\n\x06\x66ields\x18\x01 \x03(\x0b\x32#.google.spanner.v1.StructType.Field\x1a<\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x04type\x18\x02 \x01(\x0b\x32\x17.google.spanner.v1.Type*\x8e\x01\n\x08TypeCode\x12\x19\n\x15TYPE_CODE_UNSPECIFIED\x10\x00\x12\x08\n\x04\x42OOL\x10\x01\x12\t\n\x05INT64\x10\x02\x12\x0b\n\x07\x46LOAT64\x10\x03\x12\r\n\tTIMESTAMP\x10\x04\x12\x08\n\x04\x44\x41TE\x10\x05\x12\n\n\x06STRING\x10\x06\x12\t\n\x05\x42YTES\x10\x07\x12\t\n\x05\x41RRAY\x10\x08\x12\n\n\x06STRUCT\x10\tBx\n\x15\x63om.google.spanner.v1B\tTypeProtoP\x01Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\xaa\x02\x17Google.Cloud.Spanner.V1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_TYPECODE = _descriptor.EnumDescriptor(
  name='TypeCode',
  full_name='google.spanner.v1.TypeCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_CODE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT64', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMP', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BYTES', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARRAY', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRUCT', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=380,
  serialized_end=522,
)
_sym_db.RegisterEnumDescriptor(_TYPECODE)

TypeCode = enum_type_wrapper.EnumTypeWrapper(_TYPECODE)
TYPE_CODE_UNSPECIFIED = 0
BOOL = 1
INT64 = 2
FLOAT64 = 3
TIMESTAMP = 4
DATE = 5
STRING = 6
BYTES = 7
ARRAY = 8
STRUCT = 9



_TYPE = _descriptor.Descriptor(
  name='Type',
  full_name='google.spanner.v1.Type',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='google.spanner.v1.Type.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='array_element_type', full_name='google.spanner.v1.Type.array_element_type', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='struct_type', full_name='google.spanner.v1.Type.struct_type', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=248,
)


_STRUCTTYPE_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='google.spanner.v1.StructType.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.spanner.v1.StructType.Field.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.spanner.v1.StructType.Field.type', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=377,
)

_STRUCTTYPE = _descriptor.Descriptor(
  name='StructType',
  full_name='google.spanner.v1.StructType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='google.spanner.v1.StructType.fields', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STRUCTTYPE_FIELD, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=377,
)

_TYPE.fields_by_name['code'].enum_type = _TYPECODE
_TYPE.fields_by_name['array_element_type'].message_type = _TYPE
_TYPE.fields_by_name['struct_type'].message_type = _STRUCTTYPE
_STRUCTTYPE_FIELD.fields_by_name['type'].message_type = _TYPE
_STRUCTTYPE_FIELD.containing_type = _STRUCTTYPE
_STRUCTTYPE.fields_by_name['fields'].message_type = _STRUCTTYPE_FIELD
DESCRIPTOR.message_types_by_name['Type'] = _TYPE
DESCRIPTOR.message_types_by_name['StructType'] = _STRUCTTYPE
DESCRIPTOR.enum_types_by_name['TypeCode'] = _TYPECODE

Type = _reflection.GeneratedProtocolMessageType('Type', (_message.Message,), dict(
  DESCRIPTOR = _TYPE,
  __module__ = 'google.cloud.spanner_v1.proto.type_pb2'
  ,
  __doc__ = """``Type`` indicates the type of a Cloud Spanner value, as might be stored
  in a table cell or returned from an SQL query.
  
  
  Attributes:
      code:
          Required. The [TypeCode][google.spanner.v1.TypeCode] for this
          type.
      array_element_type:
          If [code][google.spanner.v1.Type.code] ==
          [ARRAY][google.spanner.v1.TypeCode.ARRAY], then
          ``array_element_type`` is the type of the array elements.
      struct_type:
          If [code][google.spanner.v1.Type.code] ==
          [STRUCT][google.spanner.v1.TypeCode.STRUCT], then
          ``struct_type`` provides type information for the struct's
          fields.
  """,
  # @@protoc_insertion_point(class_scope:google.spanner.v1.Type)
  ))
_sym_db.RegisterMessage(Type)

StructType = _reflection.GeneratedProtocolMessageType('StructType', (_message.Message,), dict(

  Field = _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), dict(
    DESCRIPTOR = _STRUCTTYPE_FIELD,
    __module__ = 'google.cloud.spanner_v1.proto.type_pb2'
    ,
    __doc__ = """Message representing a single field of a struct.
    """,
    # @@protoc_insertion_point(class_scope:google.spanner.v1.StructType.Field)
    ))
  ,
  DESCRIPTOR = _STRUCTTYPE,
  __module__ = 'google.cloud.spanner_v1.proto.type_pb2'
  ,
  __doc__ = """``StructType`` defines the fields of a
  [STRUCT][google.spanner.v1.TypeCode.STRUCT] type.
  
  
  Attributes:
      name:
          The name of the field. For reads, this is the column name. For
          SQL queries, it is the column alias (e.g., ``"Word"`` in the
          query ``"SELECT 'hello' AS Word"``), or the column name (e.g.,
          ``"ColName"`` in the query ``"SELECT ColName FROM Table"``).
          Some columns might have an empty name (e.g., !"SELECT
          UPPER(ColName)"\`). Note that a query result can contain
          multiple fields with the same name.
      type:
          The type of the field.
      fields:
          The list of fields that make up this struct. Order is
          significant, because values of this struct type are
          represented as lists, where the order of field values matches
          the order of fields in the
          [StructType][google.spanner.v1.StructType]. In turn, the order
          of fields matches the order of columns in a read request, or
          the order of fields in the ``SELECT`` clause of a query.
  """,
  # @@protoc_insertion_point(class_scope:google.spanner.v1.StructType)
  ))
_sym_db.RegisterMessage(StructType)
_sym_db.RegisterMessage(StructType.Field)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025com.google.spanner.v1B\tTypeProtoP\001Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\252\002\027Google.Cloud.Spanner.V1'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)