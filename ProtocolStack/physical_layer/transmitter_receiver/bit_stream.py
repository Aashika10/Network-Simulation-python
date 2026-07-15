from ProtocolStack.physical_layer.transmitter_receiver.bit import Bit


class BitStream:

    def __init__(self, data: str):
        self.bits = []
        for ch in data:
            if ch not in ("0", "1"):
                raise ValueError("BitStream accepts only binary strings")
            self.bits.append(Bit(int(ch)))

    def __iter__(self):
        return iter(self.bits)

    def __len__(self):
        return len(self.bits)

    def __getitem__(self, index):
        return self.bits[index]

    def __str__(self):
        return "".join(str(bit) for bit in self.bits)