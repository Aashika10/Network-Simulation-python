import random


class Noise:

    def __init__(self):
        self.enabled = True

    def apply(self, signal, delta_time):

        if not self.enabled:
            return

        # Noise level depends on the medium
        probability = (
            signal.link.medium.noise_level
            * delta_time
        )
        noise_voltage = random.gauss(0,signal.link.medium.noise_amplitude)

        if random.random() < probability:

            signal.waveform.voltage += noise_voltage