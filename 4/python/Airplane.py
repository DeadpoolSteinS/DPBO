from Vehicle import Vehicle

class Airplane(Vehicle):
    
    def __init__(self, name = "", fuelType = "", maxPassenger = 0, age = 0, type = "", wingsLength = 0):
        super().__init__(name, fuelType, maxPassenger, age, type)
        self.wingsLength = wingsLength

    def setWingsLength(self, wingsLength):
        self.wingsLength = wingsLength
        
    def getWingsLength(self):
        return self.wingsLength
    
    def show(self):
        self.showVehicle()
        print("Wings Length   : " + str(self.wingsLength))
        self.Move()
        print("================================================")