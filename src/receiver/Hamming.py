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
        super().__init__()
        self.type = "HAMMING"
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

    def _has_error(self, bin_to_check: list[str]) -> Tuple[bool, int]:
        # Check parity bits
        error_pos = [0] * self.k
        for binary in bin_to_check:
            for i, bit in enumerate(binary):
                error_pos[i] += int(bit)  # Count the number of 1s

        error_pos = [str(x % 2) for x in error_pos]  # Get the error position (syndrome)
        error_pos = int(''.join(error_pos), 2)

        return error_pos > 0, error_pos

    def decode(self, data: str) -> Tuple[str, bool, int | str]:
        """
        Decode Hamming code
        :param data: Hamming code
        :return: Decoded data
        """
        data = self._validate_data(data)
        reversed_data = data[::-1]  # Reverse the data due to the way binary numbers are represented
        idx_to_check = [idx for idx, value in enumerate(reversed_data, start=1) if value == 1]
        bin_to_check = [to_binary(idx, padding=self.k) for idx in idx_to_check]
        # Error detection
        has_error, error_pos = self._has_error(bin_to_check)

        if has_error:  # Single bit error can be fixed
            has_error = False
            reversed_data[error_pos - 1] = 1 - reversed_data[error_pos - 1]  # Flip the bit
            error_pos = "Single bit error detected. Bit position: " + str(error_pos)

        if self._has_error(bin_to_check)[0]:  # Double bit error
            has_error = True
            error_pos = "Double bit error detected. Cannot fix."

        return ''.join([str(x) for x in reversed_data[::-1]]), has_error, error_pos

    def extract_data(self, data: str) -> str:
        """
        Extract data from Hamming code
        :param data: Hamming code
        :return: Extracted data
        """
        parity_idxs = [2 ** i for i in range(self.k)]
        data_reversed = self._validate_data(data)[::-1]
        result = ""
        for i in range(0, self.n):
            if i + 1 not in parity_idxs:
                result += str(data_reversed[i])

        return ''.join(list(result)[::-1])
