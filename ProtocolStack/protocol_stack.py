from ProtocolStack.physical_layer.physical_layer import PhysicalLayer


class ProtocolStack:

    def __init__(self, node):

        self.node = node

        self.model = PhysicalLayer(node)