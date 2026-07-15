from abc import ABC, abstractmethod


class Decoder(ABC):

    @abstractmethod
    def decode(self, signal_level):
        pass