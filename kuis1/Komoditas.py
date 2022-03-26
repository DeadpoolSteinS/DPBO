class Komoditas:
    def __init__(self, idKomoditas = "", namaKomoditas = "", jenisLahan = "", sistemTanam = ""):
        self.idKomoditas = idKomoditas
        self.namaKomoditas = namaKomoditas
        self.jenisLahan = jenisLahan
        self.sistemTanam = sistemTanam
    
    def setIdKomoditas(self, idKomoditas):
        self.idKomoditas = idKomoditas

    def getIdKomoditas(self):
        return self.idKomoditas

    def setNamaKomoditas(self, namaKomoditas):
        self.namaKomoditas = namaKomoditas

    def getNamaKomoditas(self):
        return self.namaKomoditas

    def setJenisLahan(self, jenisLahan):
        self.jenisLahan = jenisLahan
    
    def getJenisLahan(self):
        return self.jenisLahan
    
    def setSistemTanam(self, sistemTanam):
        self.sistemTanam = sistemTanam
    
    def getSistemTanam(self):
        return self.sistemTanam

    def showKomoditas(self):
        print("ID Komoditas   : " + self.getIdKomoditas())
        print("Nama Komoditas : " + self.getNamaKomoditas())
        print("Jenis Lahan    : " + self.getJenisLahan())
        print("Sistem Tanah   : " + self.getSistemTanam())