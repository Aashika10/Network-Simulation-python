from abc import ABC, abstractmethod


class Framing(ABC):

    @abstractmethod
    def encode(self, data):
        """
        Convert payload into a framed payload.
        """
        pass

    @abstractmethod
    def decode(self, frame):
        """
        Extract payload from a framed payload.
        """
        pass