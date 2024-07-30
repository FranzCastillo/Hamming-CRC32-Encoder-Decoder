from typing import Tuple


class Receiver:
    def __init__(self):
        self.type = "Receiver"

    def decode(self, data: str) -> Tuple[str, bool, int | str]:
        pass

    def extract_data(self, data: str) -> str:
        pass
