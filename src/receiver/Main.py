import argparse
import os
import sys
import socket

from dotenv import load_dotenv

from CRC import CRC
from Hamming import Hamming
from Receiver import Receiver


def main(receiver: Receiver):
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
                print(f"Received: {data.decode()}")
                response = receiver.decode(data.decode())
                print(f"Response: {response}")

    print("Closing socket and exiting program.")
    sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process receiver type and its parameters.')

    parser.add_argument('receiver_type', choices=['CRC', 'HAMMING'],
                        help='Type of receiver. Can be either CRC or HAMMING.')

    # CRC specific argument
    parser.add_argument('--generator', type=str,
                        help='Polynomial generator for CRC. Required if receiver type is CRC.')

    # HAMMING specific arguments
    parser.add_argument('--n', type=int,
                        help='n parameter for Hamming. Required if receiver type is HAMMING.')
    parser.add_argument('--m', type=int,
                        help='m parameter for Hamming. Required if receiver type is HAMMING.')

    args = parser.parse_args()

    receiver: Receiver | None = None
    receiver_type: str = args.receiver_type
    if receiver_type.upper() == "CRC":
        generator = args.generator
        receiver = CRC(generator=generator)
    elif receiver_type.upper() == "HAMMING":
        n = args.n
        m = args.m
        receiver = Hamming(n=n, m=m)
    else:
        raise ValueError("Invalid receiver type or missing parameters")

    main(receiver)
