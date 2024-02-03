import datetime

from Products import Products


class Inventory(Products):
    def __init__(self, inventoryID: int, product, quantityInStock: int, lastStockUpdate: int):
        self.inventoryID = inventoryID
        super().__init__(product.productID, product.productName, product.description,product.price)
        self.quantityInStock = quantityInStock
        self.lastStockUpdate = lastStockUpdate

    @property
    def getQuantityInStock(self):
        return self.quantityInStock

    @getQuantityInStock.setter
    def getQuantityInStock(self,quantity):
        self.quantityInStock = quantity

    def GetProduct(self):
        print(f"Inventory Id = {self.inventoryID}")
        print(f"Product Id = {self.productID}")
        print(f"Product Name = {self.productName}")
        print(f"Product Description = {self.description}")
        print(f"Product Price = {self.price}")

    def GetQuantityInStock(self):
        return self.quantityInStock

    def AddToInventory(self, quantity):
        self.quantityInStock += quantity

    def RemoveFromInventory(self, quantity):
        try:
            if quantity <= self.quantityInStock:
                self.quantityInStock -= quantity
                self.lastStockUpdate = self.quantityInStock
            else:
                raise ValueError("Quantity is greater than available quantity.")
        except ValueError as v1:
            print("Invalid quantity. ",v1)

    def UpdateStockQuantity(self, newquantity):
        try:
            if newquantity >= 0:
                self.quantityInStock += newquantity
                self.lastStockUpdate = self.quantityInStock
            else:
                raise ValueError("Quanitity can't be negative.")
        except ValueError as v1:
            print("Please enter valid quantity.",v1)

    def IsProductAvailable(self, quantity):
        if quantity >= self.quantityInStock:
            print(f"Yes! The product {self.productName} is available.")
        else:
            print("Sorry! The product is not available right now.")

    def GetInventoryValue(self):
        pass

    def ListLowStockProducts(self, threshold):
        if self.quantityInStock < threshold:
            print(f"Low stock for {self.productName}")
        else:
            print("The stock is available")

    def ListOutOfStockProducts(self):
        pass

    def ListAllProducts(self):
        pass
