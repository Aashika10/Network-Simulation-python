from ProtocolStack.data_link_layer.error_control.error_detection.crc import CRC
from ProtocolStack.data_link_layer.framing.bit_stuffing import BitStuffing
# from ProtocolStack.data_link_layer.framing.character_count import CharacterCountFraming


class DataLinkLayer:
    def __init__(self, node):
        self.node = node

        # Features (added gradually)
        self.framing = BitStuffing()
        self.error_detection = CRC()
        self.flow_control = None


    def send(self, payload):
        print(f"payload : {payload}")
        encodedmsg = self.error_detection.encoder(payload)
        print(f"Encodedmsg : {encodedmsg}")
        bits = self.framing.encode(encodedmsg)
        print(f"bits : {bits}")
        return bits
        
    
    def receive(self, bits):
        data = self.framing.decode(bits)
        print(data)
        if self.error_detection.verify(data):
            payload = data[:-self.error_detection.degree]
            print(payload)
        else:
            print("CRC Error")
        