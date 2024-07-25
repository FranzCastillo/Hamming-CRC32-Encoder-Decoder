from Receiver import Receiver


def parse_generator(generator: str) -> list[int]:
    parsed = [bool(x) for x in generator]

    if len(parsed) != 4:
        raise ValueError("The polynomial should have 4 bits (x^3, x^2, x^1, x^0)")

    return parsed


class CRC(Receiver):
    def __init__(self, generator: str):
        self.generator = parse_generator(generator)

    def decode(self, data: str):
        print(self.generator)
