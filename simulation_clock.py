class SimulationClock:

    def __init__(self):

        self.time = 0.0          # Seconds since simulation started
        self.delta_time = 0.0    # Time between frames
        self.tick = 0

    def update(self, delta_time):

        self.delta_time = delta_time
        self.time += delta_time
        self.tick += 1