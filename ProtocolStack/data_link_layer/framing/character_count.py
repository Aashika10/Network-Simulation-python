from ProtocolStack.data_link_layer.framing.framing import Framing


class CharacterCountFraming(Framing):

    HEADER_SIZE = 16

    def encode(self, bits: str) -> str:
        """
        Add a 16-bit length field before the payload.

        Example:
        Payload : 10110011

        Length : 8

        Encoded:
        0000000000001000 10110011
        """

        length = len(bits)
        header = format(length, f"0{self.HEADER_SIZE}b")
        return header + bits

    def decode(self, bits: str) -> str:
        """
        Extract payload using the length field.

        Example:

        0000000000001000 10110011

        ↓

        10110011
        """

        if len(bits) < self.HEADER_SIZE:
            raise ValueError("Incomplete frame header.")

        length = int(bits[:self.HEADER_SIZE], 2)
        
        payload = bits[
            self.HEADER_SIZE:
            self.HEADER_SIZE + length
        ]

        if len(payload) != length:
            raise ValueError("Incomplete frame payload.")

        return payload