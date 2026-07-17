
from ProtocolStack.data_link_layer.data_link_layer import DataLinkLayer
from ProtocolStack.physical_layer.physical_layer import PhysicalLayer
from ProtocolStack.protocol_stack import ProtocolStack


class Node:
    '''
    Node (features):
    - Name
    - x coordinate
    - y coordinate
    - links (A node has information about how many nodes are connected to it by links)
    - network (connected to a network of nodes, links and signals)
    - stack
    '''
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.links = []
        self.ports={}
        self.network = None
        self.stack = ProtocolStack(self)



    def send(self, data):
        print(f"Node {self.name} using TCP/IP model stack for sending data")
        self.stack.send(data)


    def update(self):
        self.stack.update()


    def receive(self,signal):
        print(f"Node {self.name} using TCP/IP model stack for receiving data")
        self.stack.receive(signal)
       