from network.channel import Channel

class Signal:

    def __init__(self, sender, receiver, link, waveform):

        self.sender = sender
        self.receiver = receiver

        self.link = link
        self.waveform = waveform

        self.x = sender.x
        self.y = sender.y

        self.power = 1.0          # 100% signal strength
        self.distance = 0.0       # Distance travelled
        self.progress = 0.0       # 0.0 -> 1.0

        self.finished = False

        self.noisy = False
        self.noise_power = 0.0
        self.channel=Channel(self.sender)

    def update(self, delta_time):

        if self.finished:
            return

        self.channel.propagate(self,delta_time)
        
        if self.progress >= 1.0:

            self.receiver.receive(self)

            self.finished = True