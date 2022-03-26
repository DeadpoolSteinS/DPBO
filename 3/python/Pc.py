from Processor import Processor
from Disk import Disk
from Ram import Ram

class Pc:
    processor = None
    disk = None
    ram = None
    totalPrice = 0

    def __init__(self, processor, disk, ram):
        self.processor = processor
        self.disk = disk
        self.ram = ram
        self.totalPrice = processor.getPrice() + disk.getPrice() + ram.getPrice()

    def setProcessor(self, processor):
        self.processor = processor
    
    def getProcessor(self):
        return self.processor

    def setDisk(self, disk):
        self.disk = disk

    def getDisk(self):
        return self.disk

    def setRam(self, ram):
        self.ram = ram

    def getRam(self):
        return self.ram

    def setTotalPrice(self):
        self.totalPrice = self.processor.getPrice() + self.disk.getPrice() + self.ram.getPrice()

    def getTotalPrice(self):
        return self.totalPrice

    def showPc(self):
        self.processor.showProcessor()
        self.disk.showDisk()
        self.ram.showRam()
        
        self.setTotalPrice()
        print("Total Price     : " + str(self.getTotalPrice()))