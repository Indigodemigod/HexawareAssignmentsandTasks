class Products:
    def __init__(self, productID: int, productName, description, price: float):
        self.productID = productID
        self.productName = productName
        self.description = description
        self.price = price

    @property
    def getProductID(self):
        return self.productID

    @property
    def getProductName(self):
        return self.productName

    @property
    def getProductDescription(self):
        return self.description

    @property
    def getPrice(self):
        return self.price

    @getProductID.setter
    def setProductId(self,pid):
        self.productID = pid

    @getProductName.setter
    def setProductName(self,name):
        self.productName = name

    @getProductDescription.setter
    def setProductDescription(self,desc):
        self.description = desc

    @getPrice.setter
    def setPrice(self, price):
        try:
            if price >= 0:
                self.price = price
            else:
                raise Exception("Price Can't be negative")
        except Exception as e1:
            print("Prices can't be negative please enter a positive value", e1)

    def GetProductDetails(self):
        print("Product ID = ", self.productID)
        print("Product Name = ", self.productName)
        print("Description = ", self.description)
        print("Price = ", self.price)

    def UpdateProductInfo(self, price):
        try:
            if price >= 0:
                self.price = price
            else:
                raise ValueError("Price can't be nagative")
        except ValueError as v1:
            print("Please enter a valid price", v1)

    def IsProductInStock(self):
        pass
