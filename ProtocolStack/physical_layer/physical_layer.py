from ProtocolStack.physical_layer.transmitter_receiver.transmitter import Transmitter
from ProtocolStack.physical_layer.transmitter_receiver.receiver import Receiver
from ProtocolStack.physical_layer.irregularities.noice import Noise
from ProtocolStack.physical_layer.encoder_decoder.nrz_encoder import NRZEncoder
from ProtocolStack.physical_layer.encoder_decoder.nrz_decoder import NRZDecoder
from network.signal import Signal



class PhysicalLayer:

    def __init__(self, node):

        self.node = node

        self.transmitter = Transmitter()
        self.receiver = Receiver()
        self.encoder = NRZEncoder()
        self.decoder = NRZDecoder()
        self.noise = Noise()


    def send(self, data):
        self.transmitter.load(data)
        for port in self.node.ports.values():
            port.current_bit = 0
            port.timer = 0.0

    def update(self):
        clock = self.node.network.clock
        stream = self.transmitter.stream

        if stream is None:
            return

        for port in self.node.ports.values():

            if not port.can_transmit(clock.delta_time):
                continue

            if port.current_bit >= len(stream):
                continue

            bit = stream[port.current_bit]

            waveform = self.encoder.encode(bit)

            signal = Signal(sender=self.node, receiver=port.receiver,link=port.link ,waveform=waveform)

            self.node.network.add_signal(signal)

            port.current_bit += 1

    def receive(self, signal):
        bit = self.decoder.decode(signal.waveform)
        self.receiver.receive(bit)
        print("Power:",signal.power)
        print(f"{self.node.name}: {self.receiver.get_data()}")