# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protobuf import location_pb2 as protobuf_dot_location__pb2


class LocationServiceStub(object):
    """new_location.person_id = location["person_id"]
    new_location.creation_time = location["creation_time"]
    new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateLocation = channel.unary_unary(
                '/LocationService/CreateLocation',
                request_serializer=protobuf_dot_location__pb2.CreateLocationRequest.SerializeToString,
                response_deserializer=protobuf_dot_location__pb2.Location.FromString,
                )
        self.GetLocation = channel.unary_unary(
                '/LocationService/GetLocation',
                request_serializer=protobuf_dot_location__pb2.GetLocationRequest.SerializeToString,
                response_deserializer=protobuf_dot_location__pb2.Location.FromString,
                )


class LocationServiceServicer(object):
    """new_location.person_id = location["person_id"]
    new_location.creation_time = location["creation_time"]
    new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
    """

    def CreateLocation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLocation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LocationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateLocation,
                    request_deserializer=protobuf_dot_location__pb2.CreateLocationRequest.FromString,
                    response_serializer=protobuf_dot_location__pb2.Location.SerializeToString,
            ),
            'GetLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLocation,
                    request_deserializer=protobuf_dot_location__pb2.GetLocationRequest.FromString,
                    response_serializer=protobuf_dot_location__pb2.Location.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LocationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LocationService(object):
    """new_location.person_id = location["person_id"]
    new_location.creation_time = location["creation_time"]
    new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
    """

    @staticmethod
    def CreateLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LocationService/CreateLocation',
            protobuf_dot_location__pb2.CreateLocationRequest.SerializeToString,
            protobuf_dot_location__pb2.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LocationService/GetLocation',
            protobuf_dot_location__pb2.GetLocationRequest.SerializeToString,
            protobuf_dot_location__pb2.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ConnectionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetConnection = channel.unary_unary(
                '/ConnectionService/GetConnection',
                request_serializer=protobuf_dot_location__pb2.GetConnectionRequest.SerializeToString,
                response_deserializer=protobuf_dot_location__pb2.Connection.FromString,
                )


class ConnectionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetConnection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConnectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConnection,
                    request_deserializer=protobuf_dot_location__pb2.GetConnectionRequest.FromString,
                    response_serializer=protobuf_dot_location__pb2.Connection.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ConnectionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ConnectionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ConnectionService/GetConnection',
            protobuf_dot_location__pb2.GetConnectionRequest.SerializeToString,
            protobuf_dot_location__pb2.Connection.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
