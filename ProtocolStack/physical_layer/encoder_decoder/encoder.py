from abc import ABC, abstractmethod


class Encoder(ABC):

    @abstractmethod
    def encode(self, bit):
        pass