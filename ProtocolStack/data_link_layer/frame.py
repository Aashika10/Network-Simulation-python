class Frame:

    def __init__(
        self,
        destination,
        source,
        payload
    ):

        self.destination = destination
        self.source = source

        self.payload = payload

        self.header = None
        self.trailer = None