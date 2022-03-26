from Product import Product

class Memory(Product):
    frequency = ""
    memorySize = 0
    supportCuda = False

    def __init__(self, frequency, memorySize, supportCuda):
        self.frequency = frequency
        self.memorySize = memorySize
        self.supportCuda = supportCuda
    
    def setFrequency(self, frequency):
        self.frequency = frequency

    def getFrequency(self):
        return self.frequency

    def setMemorySize(self, memorySize):
        self.memorySize = memorySize

    def getMemorySize(self):
        return self.memorySize
    
    def setSupportCuda(self, supportCuda):
        self.supportCuda = supportCuda

    def getSupportCuda(self):
        return self.supportCuda