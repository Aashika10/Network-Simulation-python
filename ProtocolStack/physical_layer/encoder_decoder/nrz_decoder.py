from ProtocolStack.physical_layer.encoder_decoder.decoder import Decoder
from ProtocolStack.physical_layer.transmitter_receiver.bit import Bit


class NRZDecoder(Decoder):

    def decode(self, waveform):

        if waveform.voltage >= 0:
            return Bit(1)

        return Bit(0)