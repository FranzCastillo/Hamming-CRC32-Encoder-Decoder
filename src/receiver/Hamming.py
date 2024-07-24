from typing import Tuple
from Receiver import Receiver


def to_binary(num: int, padding: int = 0) -> str:
    """
    Convert number to binary
    :param padding:
    :param num: Number
    :return: Binary representation
    """
    return (bin(num)[2:]).zfill(padding)  # Remove the prefix '0b'


class Hamming(Receiver):
    def __init__(self, n: int = 7, m: int = 4):
        """
        Hamming(n, m) code
        :param n:
        :param m:
        """
        self.n = n  # Total bits
        self.m = m  # Data bits
        self.k = n - m  # Parity bits

    def _validate_data(self, data: str) -> list[int]:
        """
        Validate data
        :param data: Data
        :return: List of data
        """
        if len(data) != self.n:
            raise ValueError(f"Data length should be {self.n}")
        return [int(x) for x in data]

    def _extract_data(self, data: list[int]) -> str:
        """
        Extract data bits
        :param data: Data
        :return: Data bits
        """
        parity_bits = [self.n + 1 - 2 ** i for i in range(self.k)]
        return ''.join([str(data[i]) for i in range(self.n) if i + 1 not in parity_bits])

    def decode(self, data: str) -> Tuple[str, bool, int]:
        """
        Decode Hamming code
        :param data: Hamming code
        :return: Decoded data
        """
        data = self._validate_data(data)

        to_check: list[list[str]] = []
        idx = self.n  # Start from the last bit
        pos: int = 0  # Position
        while pos < self.n:
            if data[pos] == 1:
                to_check.append(
                    list(to_binary(idx, padding=self.k))
                )
            idx -= 1
            pos += 1

        # Check for error
        error_pos = ''  # Keeps track of the error position in binary representation

        for i in range(self.k):
            count = 0
            for position in to_check:
                count += int(position[i])
            error_pos += str(count % 2)

        # Convert binary to decimal and invert it
        error_pos_normal = int(error_pos, 2)
        error_pos_inverted = (self.n + 1) - int(error_pos, 2)

        if error_pos_normal == 0:  # No error
            return ''.join([str(c) for c in data]), False, error_pos_normal

        data[error_pos_inverted - 1] = 1 - data[error_pos_inverted - 1]  # Flip the bit

        return ''.join([str(c) for c in data]), True, error_pos_normal
