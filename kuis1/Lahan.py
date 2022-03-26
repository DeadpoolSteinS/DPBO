class Lahan:
    def __init__(self, idLahan = "", jenisTanah = "", desa = "", kecamatan = "", kota = "", provinsi = "", luas = ""):
        self.idLahan = idLahan
        self.jenisTanah = jenisTanah
        self.desa = desa
        self.kecamatan = kecamatan
        self.kota = kota
        self.provinsi = provinsi
        self.luas = luas
    
    def setIdLahan(self, idLahan):
        self.idLahan = idLahan

    def getIdLahan(self):
        return self.idLahan

    def setJenisTanah(self, jenisTanah):
        self.jenisTanah = jenisTanah

    def getJenisTanah(self):
        return self.jenisTanah
    
    def setDesa(self, desa):
        self.desa = desa
    
    def getDesa(self):
        return self.desa
    
    def setKecamatan(self, kecamatan):
        self.kecamatan = kecamatan
    
    def getKecamatan(self):
        return self.kecamatan

    def setKota(self, kota):
        self.kota = kota
    
    def getKota(self):
        return self.kota

    def setProvinsi(self, provinsi):
        self.provinsi = provinsi
    
    def getProvinsi(self):
        return self.provinsi

    def setLuas(self, luas):
        self.luas = luas
    
    def getLuas(self):
        return self.luas

    def showLahan(self):
        print("ID Lahan       : " + self.getIdLahan())
        print("Jenis Tanah    : " + self.getJenisTanah())
        print("Desa           : " + self.getDesa())
        print("Kecamatan      : " + self.getKecamatan())
        print("Kota           : " + self.getKota())
        print("Provinsi       : " + self.getProvinsi())
        print("Luas           : " + self.getLuas())