
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


    def send(self, bits):
        self.stack.model.send(bits)


    def update(self):
        self.stack.model.update()


    def receive(self,signal):
        self.stack.model.receive(signal)