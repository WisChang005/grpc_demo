import grpc
import uuid

from protos.proto_helloworld_python import helloworld_pb2
from protos.proto_helloworld_python.helloworld_pb2_grpc import TesterStub


class TesterClient:
    HelloRequest = helloworld_pb2.HelloRequest

    def __init__(self):
        self.host = "localhost:8787"
        self.channel = grpc.insecure_channel(self.host)

    def say_hello(self, request: helloworld_pb2.HelloRequest) -> helloworld_pb2.HelloResponse:
        stub = TesterStub(self.channel).SayHello
        resp, call = stub.with_call(request=request, metadata=self.get_grpc_metadata())
        print(call)
        print(resp)

    @staticmethod
    def get_grpc_metadata():
        # request headers
        md = [
            ("authorization", "Bearer xxxxxxxxxxxxxxxx"),
            ("id", str(uuid.uuid4()))
        ]
        return md

if __name__ == "__main__":
    client = TesterClient()
    req = client.HelloRequest(name="wis_test")
    client.say_hello(req)
