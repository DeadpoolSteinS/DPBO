class Vehicle:

    def __init__(self, name = "", fuelType = "", maxPassenger = 0, age = 0, type = ""):
        self.name = name
        self.fuelType = fuelType
        self.maxPassengers = maxPassenger
        self.age = age
        self.type = type
        
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setFuelType(self, fuelType):
        self.fuelType = fuelType
    
    def getFuelType(self):
        return self.fuelType

    def setMaxPassengers(self, maxPassengers):
        self.maxPassengers = maxPassengers
    
    def getMaxPassengers(self):
        return self.maxPassengers
    
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age
    
    def setType(self, type):
        self.type = type
    
    def getType(self):
        return self.type
    
    def Move(self):
        print(self.name + " is moving.")
    
    def showVehicle(self):
        print("Name           : " + self.getName())
        print("Fuel Type      : " + self.getFuelType())
        print("Max Passengers : " + str(self.getMaxPassengers()))
        print("Age            : " + str(self.getAge()))
        print("Type           : " + self.getType())