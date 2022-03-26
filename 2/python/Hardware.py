class Hardware:
    brand = ""
    model = ""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def setBrand(self, brand):
        self.brand = brand

    def getBrand(self):
        return self.brand

    def setModel(self, model):
        self.model = model

    def getModel(self):
        return self.model