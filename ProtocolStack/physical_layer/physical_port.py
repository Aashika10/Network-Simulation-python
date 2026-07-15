class PhysicalPort:

    def __init__(self, node, link):

        self.node = node
        self.link = link

        # Time since the last transmitted bit
        self.timer = 0.0

        self.current_bit = 0

    @property
    def medium(self):
        return self.link.medium

    @property
    def receiver(self):
        return self.link.other(self.node)
    
    def can_transmit(self, delta_time):

        self.timer += delta_time

        interval = 1 / self.medium.bit_rate

        if self.timer >= interval:

            self.timer -= interval

            return True

        return False
    
    @property
    def transmission_delay(self, bits: int):

        return bits / self.medium.bit_rate
    
    @property
    def propagation_delay(self):

        return (
            self.link.length /
            self.medium.propagation_speed
        )
    
    @property
    def total_delay(self):

        return self.transmission_delay + self.propagation_delay