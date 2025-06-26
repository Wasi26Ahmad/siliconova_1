"""
gRPC client for RF control assignment.

This module provides an interactive CLI to configure RF parameters
by communicating with the gRPC server.
"""

import grpc
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'proto'))


from proto import rfcontrol_pb2_grpc
from proto import rfcontrol_pb2



def run():
    """
    Connects to the gRPC server and sends RF configuration parameters.
    """
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = rfcontrol_pb2_grpc.RFControlStub(channel)
        print("Client ready. Enter RF parameters:")

        device_id = input("Device ID: ")
        frequency = float(input("Frequency (Hz): "))
        gain = float(input("Gain (dB): "))

        request = rfcontrol_pb2.RFConfig(
            device_id=device_id,
            frequency=frequency,
            gain=gain
        )

        response = stub.SetRFSettings(request)
        print(f"Response: {response.status} | Success: {response.success}")


if __name__ == '__main__':
    run()
