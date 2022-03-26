from Komoditas import Komoditas
from Lahan import Lahan

class Petani(Komoditas):
    def __init__(self, idPenduduk = "", idPetani = "", nama = "", alamat = "", status = "", lahan = None):
        self.idPenduduk = idPenduduk
        self.idPetani = idPetani
        self.nama = nama
        self.alamat = alamat
        self.status = status
        self.lahan = lahan
    
    def setIdPenduduk(self, idPenduduk):
        self.idPenduduk = idPenduduk

    def getIdPenduduk(self):
        return self.idPenduduk

    def setIdPetani(self, idPetani):
        self.idPetani = idPetani

    def getIdPetani(self):
        return self.idPetani

    def setNama(self, nama):
        self.nama = nama

    def getNama(self):
        return self.nama

    def setAlamat(self, alamat):
        self.alamat = alamat
    
    def getAlamat(self):
        return self.alamat
    
    def setStatus(self, status):
        self.status = status
    
    def getStatus(self):
        return self.status
    
    def setLahan(self, lahan):
        self.lahan = lahan
    
    def getLahan(self):
        return self.lahan

    def showPetani(self):
        print("ID Penduduk    : " + self.getIdPenduduk())
        print("ID Petani      : " + self.getIdPetani())
        print("Nama           : " + self.getNama())
        print("Alamat         : " + self.getAlamat())
        print("Status         : " + self.getStatus())
        print("  --------------------      ")
        self.lahan.showLahan()
        print("  --------------------      ")
        self.showKomoditas()
        print("====================================")