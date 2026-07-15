from ProtocolStack.physical_layer.receiver import Receiver
from ProtocolStack.physical_layer.bit import Bit

rx = Receiver()

rx.receive(Bit(1))
rx.receive(Bit(0))
rx.receive(Bit(1))

print(rx.get_data())