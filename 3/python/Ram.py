class Ram:
    capacity = ""
    price = 0

    def __init__(self, capacity, price):
        self.capacity = capacity
        self.price = price

    def setCapacity(self, capacity):
        self.capacity = capacity

    def getCapacity(self):
        return self.capacity

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def showRam(self):
        print("RAM Capacity    : " + self.getCapacity())
        print("RAM Price       : " + str(self.getPrice()))