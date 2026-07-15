
class Channel:
    def __init__(self,sender):
        self.sender = sender

    def apply_attenuation(self,signal,delta_time):
        signal.power -= (
            signal.link.medium.attenuation
            * delta_time
        )
        if signal.power < 0.0:
            signal.power = 0.0
        

    def update_progress(self,signal, delta_time):
        signal.distance += (
            signal.link.medium.propagation_speed
            * delta_time
        )
        
        signal.progress = signal.distance / signal.link.length

        if signal.progress > 1.0:
            signal.progress = 1.0

        signal.x = (
            signal.sender.x +
            (signal.receiver.x - signal.sender.x)
            * signal.progress
        )

        signal.y = (
            signal.sender.y +
            (signal.receiver.y - signal.sender.y)
            * signal.progress
        )

        
    def propagate(self,signal,delta_time):
        self.apply_attenuation(signal,delta_time)

        self.sender.stack.model.noise.apply(
                signal,
                delta_time
            )

        self.update_progress(signal,delta_time)