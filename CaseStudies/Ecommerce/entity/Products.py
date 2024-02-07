

class Product:
    def __init__(self, name, price, category, stockQuantity):
        self.product_id = None
        self.name = name
        self.price = price
        self.category = category
        self.stockQuantity = stockQuantity

    @property
    def productid(self):
        return self.product_id

    @productid.setter
    def productid(self, product_id):
        self.product_id = product_id
