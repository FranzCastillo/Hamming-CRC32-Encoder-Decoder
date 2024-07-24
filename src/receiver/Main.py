import argparse
from Receiver import Receiver
from Hamming import Hamming
from CRC import CRC


def main(receiver_type: str, n: str = None, m: str = None, generator: str = None):
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
            if error:
                print(f"Error at position {error_pos}. Fixed.")

            print(f"Data: {data}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Specify the type of receiver to be used.")
    parser.add_argument("receiver_type", type=str, help="The type of receiver (e.g., 'Hamming' or 'CRC')")
    parser.add_argument("n", nargs='?', type=int, help="Parameter n for Hamming code", default=None)
    parser.add_argument("m", nargs='?', type=int, help="Parameter m for Hamming code", default=None)
    parser.add_argument("generator", nargs='?', type=str, help="Generator polynomial for CRC", default=None)
    args = parser.parse_args()

    main(args.receiver_type, args.n, args.m, args.generator)
