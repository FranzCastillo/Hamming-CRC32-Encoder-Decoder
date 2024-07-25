import argparse
from Receiver import Receiver
from Hamming import Hamming
from CRC import CRC


def main(receiver_type: str, n: int = None, m: int = None, generator: str = None):
    receiver: Receiver | None = None
    if receiver_type.upper() == "HAMMING" and n is not None and m is not None:
        receiver = Hamming(n=int(n), m=int(m))
    elif receiver_type.upper() == "CRC" and generator is not None:
        receiver = CRC(generator=generator)
    else:
        raise ValueError("Invalid receiver type or missing parameters")

    # Read the file
    with open("../data/to_decode.txt", "r") as file:
        # Get each line
        for line in file:
            # Decode the line
            print('===============================')
            print(f"Received: {line.strip()}")
            data, error, error_pos = receiver.decode(line.strip())
            if receiver_type.upper() == "HAMMING":
                if error:
                    print(f"Error found at position {error_pos}. Fixed.")
                else:
                    print("No flipped bits.")
                print(f"Final data received: {data}")
            else:  # CRC
                if error:
                    print(f"An error was found. Syndrome: {error_pos}")
                else:
                    print("No error was found.")
                print(f"Final data received: {data}")



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

    main(receiver_type=args.receiver_type, n=args.n, m=args.m, generator=args.generator)
