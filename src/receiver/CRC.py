from Receiver import Receiver


class CRC(Receiver):
    def __init__(self, generator: str):
        super().__init__()
        self.type = "CRC"
        self.generator = generator

    def decode(self, data: str):
        w_data = list(data.lstrip('0'))
        while len(w_data) >= len(self.generator):
            for i in range(len(self.generator)):
                w_data[i] = '0' if w_data[i] == self.generator[i] else '1'  # XOR

            w_data = list(
                ''.join(w_data).lstrip('0')
            )

        # If the syndrome is full of 0s, then there is no error
        has_error = len(w_data) > 0

        return data, has_error, ''.join(w_data).zfill(len(self.generator))

