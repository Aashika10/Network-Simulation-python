
from ProtocolStack.data_link_layer.error_control.error_detection.error_detect import ErrorDetect


class CRC(ErrorDetect):
    def __init__(self, polynomial="10011"):
        self.polynomial = polynomial
        self.degree = len(polynomial) - 1
    
    def _mod2_division(self, dividend):
        """
        Performs modulo-2 division and returns the remainder.
        """

        dividend = list(dividend)
        divisor = self.polynomial

        for i in range(len(dividend) - self.degree):
            # Only divide if current bit is 1
            if dividend[i] == "1":
                for j in range(len(divisor)):
                    dividend[i + j] = str(
                        int(dividend[i + j] != divisor[j])
                    )  # XOR

        return "".join(dividend[-self.degree:])

    def encoder(self,data):
        """
        Appends CRC bits to the data.
        """

        dividend = data + "0" * self.degree
        remainder = self._mod2_division(dividend)

        return data + remainder


    def verify(self,frame):
        remainder = self._mod2_division(frame)
        return set(remainder) == {"0"}