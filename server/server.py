"""
gRPC server for RF control assignment.

This module defines a gRPC server that listens for RF configuration
commands and simulates setting those parameters using a mocked API.
"""

import grpc
from concurrent import futures
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'proto'))

from proto import rfcontrol_pb2
from proto import rfcontrol_pb2_grpc


class RFControlService(rfcontrol_pb2_grpc.RFControlServicer):
    """
    Implements the RFControl gRPC service with mocked RF parameter setting.
    """

    def SetRFSettings(self, request, context):
        """
        Receives RF configuration settings from the client and returns a response.

        Args:
            request (RFConfig): Contains device_id, frequency, and gain.
            context (grpc.ServicerContext): gRPC context.

        Returns:
            RFResponse: Response message indicating success or failure.
        """
        print(f"[Server] Received RF config: {request}")

        if request.device_id:
            print(f"Setting frequency to {request.frequency} Hz and gain to {request.gain} dB")
            return rfcontrol_pb2.RFResponse(success=True, status="RF parameters set successfully.")
        else:
            return rfcontrol_pb2.RFResponse(success=False, status="Invalid device ID.")


def serve():
    """
    Starts the gRPC server and listens for incoming requests.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    rfcontrol_pb2_grpc.add_RFControlServicer_to_server(RFControlService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
