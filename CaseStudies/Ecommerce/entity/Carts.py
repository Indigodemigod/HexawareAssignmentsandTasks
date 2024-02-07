from entity.Customers import Customer
from Products import Product


class Cart(Customer, Product):
    def __init__(self, customer, product, quantity):
        self.cart_id = None
        self.customer_id = customer.customerid
        self.product_id = product.product_id
        self.quantity = quantity

    @property
    def cartid(self):
        return self.cart_id

    @cartid.setter
    def cartid(self, cart_id):
        self.cart_id = cart_id