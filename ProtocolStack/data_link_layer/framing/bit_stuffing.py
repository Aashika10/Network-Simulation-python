from ProtocolStack.data_link_layer.framing.framing import Framing

class BitStuffing(Framing):
    def encode(self, data):
        stuffed = ""
        count = 0
        for bit in data:
            stuffed += bit
            if bit == "1":
                count += 1
                if count == 5:
                    stuffed += "0"
                    count=0
            else:
                count=0
        return "01111110" + stuffed + "01111110"
                

    def decode(self, data):
        original = ""
        count=0
        for bit in data[8:-8]:
            if bit=="1":
                count+=1
                original+=bit
            else:
                if count==5:
                    continue
                original+=bit
                count=0

        return original

