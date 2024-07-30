import json
import os
import socket
import sys

from dotenv import load_dotenv

from Message import Message


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Read dotenv
        load_dotenv()
        host = os.getenv('SOCKET_IP')
        port = int(os.getenv('SOCKET_PORT'))

        s.bind((host, port))
        print(f"Socket bound to {host}:{port}")

        s.listen()
        print("Socket is listening")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")

            while True:
                data = conn.recv(1024)
                if not data:
                    break
                decoded_data = data.decode()
                message = Message(**json.loads(decoded_data))
                print(f"Received message: {message}")

    print("Closing socket and exiting program.")
    sys.exit(0)


if __name__ == '__main__':
    main()
