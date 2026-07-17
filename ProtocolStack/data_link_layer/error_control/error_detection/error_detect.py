from abc import ABC

class ErrorDetect(ABC):
    def __init__(self, polynomial):
        self.polynomial = None
        self.degree = None

    def encoder(self,data):
        pass

    def verify(self,frame):
        pass
