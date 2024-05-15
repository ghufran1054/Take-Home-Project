# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: accounts/accounts.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='accounts/accounts.proto',
  package='accounts',
  syntax='proto3',
  serialized_options=_b('\n&com.nayavpn.android_app.proto.accounts'),
  serialized_pb=_b('\n\x17\x61\x63\x63ounts/accounts.proto\x12\x08\x61\x63\x63ounts\"(\n\x08\x41PIError\x12\x0e\n\x06\x64\x65tail\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"0\n\rLoginResponse\x12\x0e\n\x06\x61\x63\x63\x65ss\x18\x01 \x01(\t\x12\x0f\n\x07refresh\x18\x02 \x01(\t\"&\n\x13RefreshTokenRequest\x12\x0f\n\x07refresh\x18\x01 \x01(\t\"7\n\x14RefreshTokenResponse\x12\x0e\n\x06\x61\x63\x63\x65ss\x18\x01 \x01(\t\x12\x0f\n\x07refresh\x18\x02 \x01(\t\"#\n\x12VerifyTokenRequest\x12\r\n\x05token\x18\x01 \x01(\t\"$\n\x13VerifyTokenResponse\x12\r\n\x05token\x18\x01 \x01(\t\"\xe0\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x11\n\tfirstName\x18\x04 \x01(\t\x12\x10\n\x08lastName\x18\x05 \x01(\t\x12\x11\n\tlastLogin\x18\x06 \x01(\t\x12\x10\n\x08isActive\x18\x07 \x01(\x08\x12\x13\n\x0bisSuperuser\x18\x08 \x01(\x08\x12\x0f\n\x07isStaff\x18\t \x01(\x08\x12\x12\n\ndateJoined\x18\n \x01(\t\x12\x13\n\x0b\x64\x65viceLimit\x18\x0b \x01(\r\x12\x12\n\ncoverPhoto\x18\x0c \x01(\tB(\n&com.nayavpn.android_app.proto.accountsb\x06proto3')
)




_APIERROR = _descriptor.Descriptor(
  name='APIError',
  full_name='accounts.APIError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='detail', full_name='accounts.APIError.detail', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='accounts.APIError.code', index=1,
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
  serialized_start=37,
  serialized_end=77,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='accounts.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='accounts.LoginRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='accounts.LoginRequest.password', index=1,
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
  serialized_start=79,
  serialized_end=129,
)


_LOGINRESPONSE = _descriptor.Descriptor(
  name='LoginResponse',
  full_name='accounts.LoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access', full_name='accounts.LoginResponse.access', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refresh', full_name='accounts.LoginResponse.refresh', index=1,
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
  serialized_start=131,
  serialized_end=179,
)


_REFRESHTOKENREQUEST = _descriptor.Descriptor(
  name='RefreshTokenRequest',
  full_name='accounts.RefreshTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='refresh', full_name='accounts.RefreshTokenRequest.refresh', index=0,
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
  serialized_start=181,
  serialized_end=219,
)


_REFRESHTOKENRESPONSE = _descriptor.Descriptor(
  name='RefreshTokenResponse',
  full_name='accounts.RefreshTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access', full_name='accounts.RefreshTokenResponse.access', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refresh', full_name='accounts.RefreshTokenResponse.refresh', index=1,
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
  serialized_start=221,
  serialized_end=276,
)


_VERIFYTOKENREQUEST = _descriptor.Descriptor(
  name='VerifyTokenRequest',
  full_name='accounts.VerifyTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='accounts.VerifyTokenRequest.token', index=0,
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
  serialized_start=278,
  serialized_end=313,
)


_VERIFYTOKENRESPONSE = _descriptor.Descriptor(
  name='VerifyTokenResponse',
  full_name='accounts.VerifyTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='accounts.VerifyTokenResponse.token', index=0,
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
  serialized_start=315,
  serialized_end=351,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='accounts.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='accounts.User.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='accounts.User.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='accounts.User.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firstName', full_name='accounts.User.firstName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastName', full_name='accounts.User.lastName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastLogin', full_name='accounts.User.lastLogin', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isActive', full_name='accounts.User.isActive', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isSuperuser', full_name='accounts.User.isSuperuser', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isStaff', full_name='accounts.User.isStaff', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dateJoined', full_name='accounts.User.dateJoined', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceLimit', full_name='accounts.User.deviceLimit', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coverPhoto', full_name='accounts.User.coverPhoto', index=11,
      number=12, type=9, cpp_type=9, label=1,
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
  serialized_start=354,
  serialized_end=578,
)

DESCRIPTOR.message_types_by_name['APIError'] = _APIERROR
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LoginResponse'] = _LOGINRESPONSE
DESCRIPTOR.message_types_by_name['RefreshTokenRequest'] = _REFRESHTOKENREQUEST
DESCRIPTOR.message_types_by_name['RefreshTokenResponse'] = _REFRESHTOKENRESPONSE
DESCRIPTOR.message_types_by_name['VerifyTokenRequest'] = _VERIFYTOKENREQUEST
DESCRIPTOR.message_types_by_name['VerifyTokenResponse'] = _VERIFYTOKENRESPONSE
DESCRIPTOR.message_types_by_name['User'] = _USER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

APIError = _reflection.GeneratedProtocolMessageType('APIError', (_message.Message,), {
  'DESCRIPTOR' : _APIERROR,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:accounts.APIError)
  })
_sym_db.RegisterMessage(APIError)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:accounts.LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:accounts.LoginResponse)
  })
_sym_db.RegisterMessage(LoginResponse)

RefreshTokenRequest = _reflection.GeneratedProtocolMessageType('RefreshTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _REFRESHTOKENREQUEST,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:accounts.RefreshTokenRequest)
  })
_sym_db.RegisterMessage(RefreshTokenRequest)

RefreshTokenResponse = _reflection.GeneratedProtocolMessageType('RefreshTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _REFRESHTOKENRESPONSE,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:accounts.RefreshTokenResponse)
  })
_sym_db.RegisterMessage(RefreshTokenResponse)

VerifyTokenRequest = _reflection.GeneratedProtocolMessageType('VerifyTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYTOKENREQUEST,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:accounts.VerifyTokenRequest)
  })
_sym_db.RegisterMessage(VerifyTokenRequest)

VerifyTokenResponse = _reflection.GeneratedProtocolMessageType('VerifyTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYTOKENRESPONSE,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:accounts.VerifyTokenResponse)
  })
_sym_db.RegisterMessage(VerifyTokenResponse)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:accounts.User)
  })
_sym_db.RegisterMessage(User)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
