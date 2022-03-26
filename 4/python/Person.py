from Job import Job
from Driver import Driver

class Person(Job, Driver):

    def __init__(self, nik = "", name = "", gender = "", nip = "", companyName = "", position = "", lisenceId = 0, activeUntil = "", vehicleType = ""):
        self.nik = nik
        self.name = name
        self.gender = gender
        Job.__init__(self, nip, companyName, position)
        Driver.__init__(self, lisenceId, activeUntil, vehicleType)

    def setNik(self, nik):
        self.nik = nik

    def getNik(self):
        return self.nik

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setGender(self, gender):
        self.gender = gender

    def getGender(self):
        return self.gender

    def sleep(self):
        print(self.getName() + " is sleep.")

    def show(self):
        print("NIK            : " + self.getNik())
        print("Name           : " + self.getName())
        print("Gender         : " + self.getGender())
        print("      ---------------------------------      ")
        print("NIP            : " + self.getNip())
        print("Company Name   : " + self.getCompanyName())
        print("Position       : " + self.getPosition())
        print("      ---------------------------------      ")
        print("Lisence ID     : " + str(self.getLisenceId()))
        print("Active Until   : " + self.getActiveUntil())
        print("Vehicle Type   : " + self.getVehicleType())
        self.sleep()
        print("================================================")