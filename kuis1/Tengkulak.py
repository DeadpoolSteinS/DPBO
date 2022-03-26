class Tengkulak:
    def __init__(self, idPenduduk = "", idTengkulak = "", nama = "", alamat = "", idKomoditas = ""):
        self.idPenduduk = idPenduduk
        self.idTengkulak = idTengkulak
        self.nama = nama
        self.alamat = alamat
        self.idKomoditas = idKomoditas
    
    def setIdPenduduk(self, idPenduduk):
        self.idPenduduk = idPenduduk

    def getIdPenduduk(self):
        return self.idPenduduk

    def setIdTengkulak(self, idTengkulak):
        self.idTengkulak = idTengkulak

    def getIdTengkulak(self):
        return self.idTengkulak

    def setNama(self, nama):
        self.nama = nama

    def getNama(self):
        return self.nama

    def setAlamat(self, alamat):
        self.alamat = alamat
    
    def getAlamat(self):
        return self.alamat
    
    def setIdKomoditas(self, idKomoditas):
        self.idKomoditas = idKomoditas
    
    def getIdKomoditas(self):
        return self.idKomoditas

    def showTengkulak(self):
        print("ID Penduduk  : " + self.getIdPenduduk())
        print("ID Tengkulak : " + self.getIdTengkulak())
        print("Nama         : " + self.getNama())
        print("Alamat       : " + self.getAlamat())
        print("ID Komoditas : " + self.getIdKomoditas())
        print("====================================")