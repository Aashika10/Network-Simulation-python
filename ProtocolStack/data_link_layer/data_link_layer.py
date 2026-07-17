from ProtocolStack.data_link_layer.framing.bit_stuffing import BitStuffing
from ProtocolStack.data_link_layer.framing.character_count import CharacterCountFraming


class DataLinkLayer:

    def __init__(self, node):

        self.node = node

        # Features (added gradually)
        self.framing = BitStuffing()
        self.error_detection = None
        self.flow_control = None

    def send(self, payload):
        print(f"payload : {payload}")
        bits = self.framing.encode(payload)
        print(f"bits : {bits}")
        return bits
        
    
    def receive(self, bits):
        payload = self.framing.decode(bits)
        print(payload)