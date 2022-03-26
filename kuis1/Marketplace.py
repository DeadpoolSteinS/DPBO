class Marketplace:
    def __init__(self, idMarketplace = "", namaMarketplace = "", tipeMarket = "", tipeBisnis = ""):
        self.idMarketplace = idMarketplace
        self.namaMarketplace = namaMarketplace
        self.tipeMarket = tipeMarket
        self.tipeBisnis = tipeBisnis
    
    def setIdMarketplace(self, idMarketplace):
        self.idMarketplace = idMarketplace

    def getIdMarketplace(self):
        return self.idMarketplace

    def setNamaMarketplace(self, namaMarketplace):
        self.namaMarketplace = namaMarketplace

    def getNamaMarketplace(self):
        return self.namaMarketplace

    def setTipeMarket(self, tipeMarket):
        self.tipeMarket = tipeMarket
    
    def getTipeMarket(self):
        return self.tipeMarket
    
    def setTipeBisnis(self, tipeBisnis):
        self.tipeBisnis = tipeBisnis
    
    def getTipeBisnis(self):
        return self.tipeBisnis

    def showMarketplace(self):
        print("ID Marketplace   : " + self.getIdMarketplace())
        print("Nama Marketplace : " + self.getNamaMarketplace())
        print("Tipe Market      : " + self.getTipeMarket())
        print("Tipe Bisnis      : " + self.getTipeBisnis())
        print("====================================")