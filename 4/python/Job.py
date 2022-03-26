class Job:
    
    def __init__(self, nip = "", companyName = "", position = ""):
        self.nip = nip
        self.companyName = companyName
        self.position = position
    
    def setNip(self, nip):
        self.nip = nip
    
    def getNip(self):
        return self.nip
    
    def setCompanyName(self, companyName):
        self.companyName = companyName
    
    def getCompanyName(self):
        return self.companyName
    
    def setPosition(self, position):
        self.position = position
    
    def getPosition(self):
        return self.position
    