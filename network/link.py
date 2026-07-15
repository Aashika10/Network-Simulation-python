from ProtocolStack.physical_layer.medium.copper import Copper
# from ProtocolStack.physical_layer.fibre import Fibre
# from ProtocolStack.physical_layer.wireless import Wireless
import math

class Link:

    def __init__(self, node1, node2):

        self.node1 = node1
        self.node2 = node2

        self.medium = Copper()
       
        self.length = math.sqrt((node2.x - node1.x) ** 2 +(node2.y - node1.y) ** 2) * 1000 * 1000 # meters


    def other(self, node):
        """Return the node on the opposite end of the link."""

        if node == self.node1:
            return self.node2

        elif node == self.node2:
            return self.node1

        raise ValueError("Node is not connected to this link")