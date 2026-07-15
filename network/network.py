from network.link import Link
from ProtocolStack.physical_layer.physical_port import PhysicalPort


class Network:

    def __init__(self):

        self.nodes = []
        self.links = []
        self.signals = []
        self.clock = None


    def add_node(self, node):
        self.nodes.append(node)
        node.network = self


    def connect(self, node1, node2):
        link = Link(node1, node2)
        self.links.append(link)

        node1.links.append(link)
        node2.links.append(link)
      
        node1.ports[link]=PhysicalPort(node1, link)
        node2.ports[link]=PhysicalPort(node2, link)
    

    def add_signal(self, signal):
        self.signals.append(signal)


    def update(self):
        delta_time = self.clock.delta_time

        for node in self.nodes:
            node.update()

        for signal in self.signals:
            signal.update(delta_time)

        self.signals = [
            s for s in self.signals
            if not s.finished
            ]