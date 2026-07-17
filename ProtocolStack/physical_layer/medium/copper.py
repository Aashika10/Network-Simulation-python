from ProtocolStack.physical_layer.medium.medium import Medium


class Copper(Medium):

    def __init__(self):

        super().__init__()

        self.name = "Copper"

        self.propagation_speed = 2e8 #simulation unit

        self.noise_level = 0.5

        #   Thermal Noise
        #   Crosstalk
        self.noise_amplitude = 10

        # self.bandwidth = 100
        self.bit_rate  = 2

        self.attenuation = 0.02