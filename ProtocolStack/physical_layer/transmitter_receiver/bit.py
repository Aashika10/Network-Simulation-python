class Bit:

    def __init__(self, value: int):
        if value not in (0, 1):
            raise ValueError("Bit value must be 0 or 1")
        
        self.value = value
        self.x = 0
        self.y = 0
        self.received = False


    def flip(self):
        """Used later by the Noise model."""
        self.value ^= 1


    def __str__(self):
        return str(self.value)


    def __repr__(self):
        return f"Bit({self.value})"