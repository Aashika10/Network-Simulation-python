from abc import ABC


class Medium(ABC):

    def __init__(self):

        self.name = "Medium"

        # meters / second
        self.propagation_speed = 0

        # Mbps
        self.bit_rate  = 0
        # self.bits_per_tick = 0

        # dB per meter
        self.attenuation = 0