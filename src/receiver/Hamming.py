from typing import Tuple


class Hamming:
    def __init__(self, n: int = 7, m: int = 4):
        """
        Hamming(n, m) code
        :param n:
        :param m:
        """
        self.n = n  # Total bits
        self.m = m  # Data bits
        self.k = n - m  # Parity bits

    def _validate_data(self, data: str) -> list:
        """
        Validate data
        :param data: Data
        :return: List of data
        """
        if len(data) != self.n:
            raise ValueError(f"Data length should be {self.n}")
        return [int(x) for x in data]

    def decode(self, data: str) -> str:
        """
        Decode Hamming code
        :param data: Hamming code
        :return: Decoded data
        """
        data = self._validate_data(data)
