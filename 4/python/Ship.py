from Vehicle import Vehicle

class Ship(Vehicle):
    
    def __init__(self, name = "", fuelType = "", maxPassenger = 0, age = 0, type = "", countryOfManufacture = ""):
        super().__init__(name, fuelType, maxPassenger, age, type)
        self.countryOfManufacture = countryOfManufacture
        
    def setCountryOfManufacture(self, countryOfManufacture):
        self.countryOfManufacture = countryOfManufacture
    
    def getCountryOfManufacture(self):
        return self.countryOfManufacture
    
    def show(self):
        self.showVehicle()
        print("Country        : " + self.countryOfManufacture)
        self.Move()
        print("================================================")