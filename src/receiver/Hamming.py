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
        for i in range(self.k):  # Check for each parity bit
            count = 0  # Count of 1s
            for j in range(len(to_check)):  # Check for each data bit
                count += int(to_check[j][i])
            error_pos += str(count % 2)  # Check parity

        # Convert binary to decimal
        error_pos = int(error_pos, 2)
        data_transmitted = ''.join([str(x) for x in data[:self.m]])

        if error_pos == 0:  # No error
            return data_transmitted, False, error_pos

        data[error_pos - 1] = 1 - data[error_pos - 1]  # Flip the bit
        data_transmitted = ''.join([str(x) for x in data[:self.m]])

        return data_transmitted, True, error_pos
