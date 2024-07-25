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

        if n != 2 ** self.k - 1:
            raise ValueError("Invalid parameters. n should be 2^k - 1")

    def _validate_data(self, data: str) -> list[int]:
        """
        Validate data
        :param data: Data
        :return: List of data
        """
        if len(data) != self.n:
            raise ValueError(f"Data length should be {self.n}")

        if not all([c in ['0', '1'] for c in data]):
            raise ValueError("Data should be binary")

        return [int(x) for x in data]

    def decode(self, data: str) -> Tuple[str, bool, int|str]:
        """
        Decode Hamming code
        :param data: Hamming code
        :return: Decoded data
        """
        data = self._validate_data(data)
        reversed_data = data[::-1]  # Reverse the data due to the way binary numbers are represented
        idx_to_check = [idx for idx, value in enumerate(reversed_data, start=1) if value == 1]
        bin_to_check = [to_binary(idx, padding=self.k) for idx in idx_to_check]

        # Check parity bits
        error_pos = [0] * self.k
        for binary in bin_to_check:
            for i, bit in enumerate(binary):
                error_pos[i] += int(bit)  # Count the number of 1s

        error_pos = [str(x % 2) for x in error_pos]  # Get the error position (syndrome)
        error_pos = int(''.join(error_pos), 2)

        # Error detection
        has_error = error_pos > 0
        if has_error > 0:
            count = 0
            for x in data:
                count += x
            if count % 2 == 0:
                error_pos = "Double bit error detected. Cannot fix."
            else:
                reversed_data[error_pos - 1] = 1 - reversed_data[error_pos - 1]  # Flip the bit
                error_pos = "Single bit error detected. Bit position: " + str(error_pos)

        return ''.join([str(x) for x in reversed_data[::-1]]), has_error, error_pos
