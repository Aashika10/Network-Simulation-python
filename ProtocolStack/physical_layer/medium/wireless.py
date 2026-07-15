from ProtocolStack.physical_layer.medium.medium import Medium


class Wireless(Medium):

    def __init__(self):

        super().__init__()

        self.name = "Wireless"

        self.propagation_speed = 3e8

        # self.bandwidth = 600
        self.bit_rate = 2
        self.noise_level = 0.08
        # AWGN
        # Fading
        # Multipath
        # Interference

        self.attenuation = 0.08