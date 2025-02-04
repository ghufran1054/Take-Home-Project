# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: edge_nodes/edge_nodes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='edge_nodes/edge_nodes.proto',
  package='edge_nodes',
  syntax='proto3',
  serialized_options=_b('\n(com.nayavpn.android_app.proto.edge_nodes'),
  serialized_pb=_b('\n\x1b\x65\x64ge_nodes/edge_nodes.proto\x12\nedge_nodes\"p\n\x08\x45\x64geNode\x12\n\n\x02id\x18\x01 \x01(\x04\x12\r\n\x05label\x18\x02 \x01(\t\x12\x10\n\x08tunnelIP\x18\x03 \x01(\x0c\x12\x10\n\x08publicIP\x18\x04 \x01(\x0c\x12\x11\n\tpublicKey\x18\x05 \x01(\x0c\x12\x12\n\nwgEndpoint\x18\x06 \x01(\t\",\n\x0f\x45\x64geNodeTrimmed\x12\n\n\x02id\x18\x01 \x01(\x04\x12\r\n\x05label\x18\x02 \x01(\t\",\n\x15GetActiveNodesRequest\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x01 \x01(\t\"D\n\x16GetActiveNodesResponse\x12*\n\x05nodes\x18\x01 \x03(\x0b\x32\x1b.edge_nodes.EdgeNodeTrimmedB*\n(com.nayavpn.android_app.proto.edge_nodesb\x06proto3')
)




_EDGENODE = _descriptor.Descriptor(
  name='EdgeNode',
  full_name='edge_nodes.EdgeNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='edge_nodes.EdgeNode.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='edge_nodes.EdgeNode.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tunnelIP', full_name='edge_nodes.EdgeNode.tunnelIP', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publicIP', full_name='edge_nodes.EdgeNode.publicIP', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publicKey', full_name='edge_nodes.EdgeNode.publicKey', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wgEndpoint', full_name='edge_nodes.EdgeNode.wgEndpoint', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=43,
  serialized_end=155,
)


_EDGENODETRIMMED = _descriptor.Descriptor(
  name='EdgeNodeTrimmed',
  full_name='edge_nodes.EdgeNodeTrimmed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='edge_nodes.EdgeNodeTrimmed.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='edge_nodes.EdgeNodeTrimmed.label', index=1,
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
  serialized_start=157,
  serialized_end=201,
)


_GETACTIVENODESREQUEST = _descriptor.Descriptor(
  name='GetActiveNodesRequest',
  full_name='edge_nodes.GetActiveNodesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accessToken', full_name='edge_nodes.GetActiveNodesRequest.accessToken', index=0,
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
  serialized_start=203,
  serialized_end=247,
)


_GETACTIVENODESRESPONSE = _descriptor.Descriptor(
  name='GetActiveNodesResponse',
  full_name='edge_nodes.GetActiveNodesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='edge_nodes.GetActiveNodesResponse.nodes', index=0,
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
  serialized_start=249,
  serialized_end=317,
)

_GETACTIVENODESRESPONSE.fields_by_name['nodes'].message_type = _EDGENODETRIMMED
DESCRIPTOR.message_types_by_name['EdgeNode'] = _EDGENODE
DESCRIPTOR.message_types_by_name['EdgeNodeTrimmed'] = _EDGENODETRIMMED
DESCRIPTOR.message_types_by_name['GetActiveNodesRequest'] = _GETACTIVENODESREQUEST
DESCRIPTOR.message_types_by_name['GetActiveNodesResponse'] = _GETACTIVENODESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EdgeNode = _reflection.GeneratedProtocolMessageType('EdgeNode', (_message.Message,), {
  'DESCRIPTOR' : _EDGENODE,
  '__module__' : 'edge_nodes.edge_nodes_pb2'
  # @@protoc_insertion_point(class_scope:edge_nodes.EdgeNode)
  })
_sym_db.RegisterMessage(EdgeNode)

EdgeNodeTrimmed = _reflection.GeneratedProtocolMessageType('EdgeNodeTrimmed', (_message.Message,), {
  'DESCRIPTOR' : _EDGENODETRIMMED,
  '__module__' : 'edge_nodes.edge_nodes_pb2'
  # @@protoc_insertion_point(class_scope:edge_nodes.EdgeNodeTrimmed)
  })
_sym_db.RegisterMessage(EdgeNodeTrimmed)

GetActiveNodesRequest = _reflection.GeneratedProtocolMessageType('GetActiveNodesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACTIVENODESREQUEST,
  '__module__' : 'edge_nodes.edge_nodes_pb2'
  # @@protoc_insertion_point(class_scope:edge_nodes.GetActiveNodesRequest)
  })
_sym_db.RegisterMessage(GetActiveNodesRequest)

GetActiveNodesResponse = _reflection.GeneratedProtocolMessageType('GetActiveNodesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACTIVENODESRESPONSE,
  '__module__' : 'edge_nodes.edge_nodes_pb2'
  # @@protoc_insertion_point(class_scope:edge_nodes.GetActiveNodesResponse)
  })
_sym_db.RegisterMessage(GetActiveNodesResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
