from ProtocolStack.data_link_layer.data_link_layer import DataLinkLayer
from ProtocolStack.physical_layer.physical_layer import PhysicalLayer


class ProtocolStack:

    def __init__(self, node):
        self.node = node
        self.layers = {}
        self.add_layer("physical", PhysicalLayer(node))
        self.add_layer("datalink", DataLinkLayer(node))


    def add_layer(self, name, layer):
        self.layers[name] = layer
    
    
    def update(self):
        self.layers["physical"].update()


    def get_layer(self, name):
        return self.layers[name]
    

    def send(self, data):

        print(f"Node {self.node.name} is sending {data} to the DataLinkLayer")
        bits = self.layers["datalink"].send(data) #000000000000100000001111

        print(f"DatalinkLayer is sending {bits} to the physical layer")
        self.layers["physical"].send(bits)



    def receive(self, signal):
        print(f"Node {self.node.name} is receiving a signal")
        bit_stream = self.layers["physical"].receive(signal)

        if signal.bit_index == signal.total_bits - 1:
            print(f"PhysicalLayer is forwarding received payload:{bit_stream} to the DataLinkLayer")
            frame = self.layers["datalink"].receive(bit_stream)

