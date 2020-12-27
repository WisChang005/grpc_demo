import time
from locust import TaskSet
from locust import User
from locust import task

from grpc_client import TesterClient
from protos.proto_helloworld_python import helloworld_pb2


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def say_hello(self):
        req_data = helloworld_pb2.HelloRequest(name="wis_perf_test")
        self.locust_request_handler("say_hello", req_data)

    def locust_request_handler(self, grpc_name, req_data):
        req_func = self._get_request_function(grpc_name)
        start = time.time()
        result = None
        try:
            result = req_func(req_data)
        except Exception as e:
            total = int((time.time() - start) * 1000)
            self.user.environment.events.request_failure.fire(
                request_type="grpc", name=grpc_name, response_time=total, response_length=0, exception=e)
        else:
            total = int((time.time() - start) * 1000)
            self.user.environment.events.request_success.fire(
                request_type="grpc", name=grpc_name, response_time=total, response_length=0)
        return result

    def _get_request_function(self, grpc_name):
        req_func_map = {
            "say_hello": self.client.say_hello,
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class TesterUser(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()


