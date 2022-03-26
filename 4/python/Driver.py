class Driver:
    
    def __init__(self, lisenceId = "", activeUntil = "", vehicleType = ""):
        self.lisenceId = lisenceId
        self.activeUntil = activeUntil
        self.vehicleType = vehicleType

    def setLisenceId(self, lisenceId):
        self.lisenceId = lisenceId
        
    def getLisenceId(self):
        return self.lisenceId
    
    def setActiveUntil(self, activeUntil):
        self.activeUntil = activeUntil
    
    def getActiveUntil(self):
        return self.activeUntil
    
    def setVehicleType(self, vehicleType):
        self.vehicleType = vehicleType
    
    def getVehicleType(self):
        return self.vehicleType
    
    