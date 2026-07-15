from ProtocolStack.physical_layer.transmitter_receiver.bit_stream import BitStream


class Transmitter:

    def __init__(self):

        self.stream = None

    def load(self, data: str):

        self.stream = BitStream(data)
