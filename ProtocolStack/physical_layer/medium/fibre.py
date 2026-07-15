from ProtocolStack.physical_layer.medium.medium import Medium


class Fibre(Medium):

    def __init__(self):

        super().__init__()

        self.name = "Fiber"

        self.propagation_speed = 2.1e8

        # self.bandwidth = 10000
        self.bit_rate  = 8
        self.noise_level = 0.001
#         Shot Noise
#         Dispersion Noise


        self.attenuation = 0.003