import json
import os
import socket
import sys

from dotenv import load_dotenv

from CRC import CRC
from Hamming import Hamming
from Message import Message
from Receiver import Receiver


def create_receiver(algorithm: str) -> Receiver:
    alg = algorithm.upper()
    if alg == "HAMMING":
        return Hamming()  # Hamming(7,4) by default
    elif alg == "CRC":
        return CRC(os.getenv('CRC_POLY'))
    else:
        raise ValueError(f"Invalid algorithm: {algorithm}")


def decode_message(receiver: Receiver, message: Message) -> str:
    result = ""
    if receiver.type == "HAMMING":
        for char in message.message:
            # Split each character into 2
            first_bits = char[:7]
            second_bits = char[7:]

            # Decode each half
            first_decoded, first_error, _ = receiver.decode(first_bits)
            second_decoded, second_error, _ = receiver.decode(second_bits)

            if any([first_error, second_error]):
                raise ValueError(f"Double bit error detected. Cannot fix. Message so far: '{result}'")

            # Combine the decoded halves
            result_bin = receiver.extract_data(first_decoded) + receiver.extract_data(second_decoded)

            # Parse the 8 bits into a character
            result += chr(int(result_bin, 2))

    elif receiver.type == "CRC":
        pass
    else:
        raise ValueError(f"Invalid receiver type: {receiver.type}")

    return result

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

                receiver = create_receiver(message.algorithm)
                decoded_message = decode_message(receiver, message)
                print(f"Decoded message: {decoded_message}")

    print("Closing socket and exiting program.")
    sys.exit(0)


if __name__ == '__main__':
    main()
