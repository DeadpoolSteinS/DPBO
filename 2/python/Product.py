from Hardware import Hardware

class Product(Hardware):
    price = ""
    idProduct = 0

    def __init__(self, price, idProduct):
        self.price = price
        self.idProduct = idProduct
    
    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setIdProduct(self, idProduct):
        self.idProduct = idProduct

    def getIdProduct(self):
        return self.idProduct