class Processor:
    name = ""
    price = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def showProcessor(self):
        print("Processor name  : " + self.getName())
        print("Processor Price : " + str(self.getPrice()))