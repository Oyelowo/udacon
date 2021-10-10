# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/location.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protobuf import person_pb2 as protobuf_dot_person__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/location.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17protobuf/location.proto\x1a\x15protobuf/person.proto\"e\n\x08Location\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\t\x12\x11\n\tlongitude\x18\x03 \x01(\t\x12\x10\n\x08latitude\x18\x04 \x01(\t\x12\x15\n\rcreation_time\x18\x05 \x01(\t\"f\n\x15\x43reateLocationRequest\x12\x11\n\tperson_id\x18\x01 \x01(\t\x12\x11\n\tlongitude\x18\x02 \x01(\t\x12\x10\n\x08latitude\x18\x03 \x01(\t\x12\x15\n\rcreation_time\x18\x04 \x01(\t\" \n\x12GetLocationRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"M\n\nConnection\x12\"\n\x06person\x18\x01 \x01(\x0b\x32\x12.api.person.Person\x12\x1b\n\x08location\x18\x02 \x01(\x0b\x32\t.Location\"_\n\x14GetConnectionRequest\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x12\n\nstart_date\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x03 \x01(\t\x12\x0e\n\x06meters\x18\x04 \x01(\x02\x32u\n\x0fLocationService\x12\x33\n\x0e\x43reateLocation\x12\x16.CreateLocationRequest\x1a\t.Location\x12-\n\x0bGetLocation\x12\x13.GetLocationRequest\x1a\t.Location2H\n\x11\x43onnectionService\x12\x33\n\rGetConnection\x12\x15.GetConnectionRequest\x1a\x0b.Connectionb\x06proto3'
  ,
  dependencies=[protobuf_dot_person__pb2.DESCRIPTOR,])




_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Location.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='Location.person_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Location.longitude', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Location.latitude', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='Location.creation_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=50,
  serialized_end=151,
)


_CREATELOCATIONREQUEST = _descriptor.Descriptor(
  name='CreateLocationRequest',
  full_name='CreateLocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='CreateLocationRequest.person_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='CreateLocationRequest.longitude', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='CreateLocationRequest.latitude', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='CreateLocationRequest.creation_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=153,
  serialized_end=255,
)


_GETLOCATIONREQUEST = _descriptor.Descriptor(
  name='GetLocationRequest',
  full_name='GetLocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GetLocationRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=257,
  serialized_end=289,
)


_CONNECTION = _descriptor.Descriptor(
  name='Connection',
  full_name='Connection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person', full_name='Connection.person', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='Connection.location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=291,
  serialized_end=368,
)


_GETCONNECTIONREQUEST = _descriptor.Descriptor(
  name='GetConnectionRequest',
  full_name='GetConnectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='GetConnectionRequest.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='GetConnectionRequest.start_date', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='GetConnectionRequest.end_date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meters', full_name='GetConnectionRequest.meters', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=370,
  serialized_end=465,
)

_CONNECTION.fields_by_name['person'].message_type = protobuf_dot_person__pb2._PERSON
_CONNECTION.fields_by_name['location'].message_type = _LOCATION
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['CreateLocationRequest'] = _CREATELOCATIONREQUEST
DESCRIPTOR.message_types_by_name['GetLocationRequest'] = _GETLOCATIONREQUEST
DESCRIPTOR.message_types_by_name['Connection'] = _CONNECTION
DESCRIPTOR.message_types_by_name['GetConnectionRequest'] = _GETCONNECTIONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'protobuf.location_pb2'
  # @@protoc_insertion_point(class_scope:Location)
  })
_sym_db.RegisterMessage(Location)

CreateLocationRequest = _reflection.GeneratedProtocolMessageType('CreateLocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATELOCATIONREQUEST,
  '__module__' : 'protobuf.location_pb2'
  # @@protoc_insertion_point(class_scope:CreateLocationRequest)
  })
_sym_db.RegisterMessage(CreateLocationRequest)

GetLocationRequest = _reflection.GeneratedProtocolMessageType('GetLocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLOCATIONREQUEST,
  '__module__' : 'protobuf.location_pb2'
  # @@protoc_insertion_point(class_scope:GetLocationRequest)
  })
_sym_db.RegisterMessage(GetLocationRequest)

Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTION,
  '__module__' : 'protobuf.location_pb2'
  # @@protoc_insertion_point(class_scope:Connection)
  })
_sym_db.RegisterMessage(Connection)

GetConnectionRequest = _reflection.GeneratedProtocolMessageType('GetConnectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONNECTIONREQUEST,
  '__module__' : 'protobuf.location_pb2'
  # @@protoc_insertion_point(class_scope:GetConnectionRequest)
  })
_sym_db.RegisterMessage(GetConnectionRequest)



_LOCATIONSERVICE = _descriptor.ServiceDescriptor(
  name='LocationService',
  full_name='LocationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=467,
  serialized_end=584,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateLocation',
    full_name='LocationService.CreateLocation',
    index=0,
    containing_service=None,
    input_type=_CREATELOCATIONREQUEST,
    output_type=_LOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLocation',
    full_name='LocationService.GetLocation',
    index=1,
    containing_service=None,
    input_type=_GETLOCATIONREQUEST,
    output_type=_LOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOCATIONSERVICE)

DESCRIPTOR.services_by_name['LocationService'] = _LOCATIONSERVICE


_CONNECTIONSERVICE = _descriptor.ServiceDescriptor(
  name='ConnectionService',
  full_name='ConnectionService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=586,
  serialized_end=658,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetConnection',
    full_name='ConnectionService.GetConnection',
    index=0,
    containing_service=None,
    input_type=_GETCONNECTIONREQUEST,
    output_type=_CONNECTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONNECTIONSERVICE)

DESCRIPTOR.services_by_name['ConnectionService'] = _CONNECTIONSERVICE

# @@protoc_insertion_point(module_scope)
