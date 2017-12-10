import grpc
import model_serving_pb2
import model_serving_pb2_grpc

IMG_ID = 3 # image to predict, range [0,30)

channel = grpc.insecure_channel('ec2-34-236-255-121.compute-1.amazonaws.com:19999')
stub = model_serving_pb2_grpc.ModelStub(channel)

response = stub.Predict(model_serving_pb2.Input(img_id=IMG_ID))
print("Prediction result: " + response.res)
