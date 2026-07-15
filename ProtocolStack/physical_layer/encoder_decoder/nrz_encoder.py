from ProtocolStack.physical_layer.encoder_decoder.waveform import Waveform
from ProtocolStack.physical_layer.encoder_decoder.encoder import Encoder


class NRZEncoder(Encoder):

    def encode(self, bit):

        if bit.value == 1:
            return Waveform(+5)      # +5V

        return Waveform(-5)    # -5V