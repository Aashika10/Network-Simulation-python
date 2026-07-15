class Receiver:

    def __init__(self):

        self.bits = []

    def receive(self, bit):

        self.bits.append(bit)

    def get_data(self):

        return "".join(str(bit) for bit in self.bits)

    def clear(self):

        self.bits.clear()