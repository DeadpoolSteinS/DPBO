class Disk:
    type = ""
    capacity = ""
    price = 0

    def __init__(self, type, capacity, price):
        self.type = type
        self.capacity = capacity
        self.price = price

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def setCapacity(self, capacity):
        self.capacity = capacity

    def getCapacity(self):
        return self.capacity

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def showDisk(self):
        print("Disk Type       : " + self.getType())
        print("Disk Capacity   : " + self.getCapacity())
        print("Disk Price      : " + str(self.getPrice()))