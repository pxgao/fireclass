import grpc
import model_serving_pb2
import model_serving_pb2_grpc


channel = grpc.insecure_channel('localhost:19999')
stub = model_serving_pb2_grpc.ModelStub(channel)

response = stub.Predict(model_serving_pb2.Input(img_id=3))
print("Greeter client received: " + response.res)
