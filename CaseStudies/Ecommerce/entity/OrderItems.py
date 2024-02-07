from Orders import Order
from Products import Product


class OrderItem(Order, Product):
    def __init__(self, order, product, quantity):
        self.order_item_id = None
        self.order_id = order.order_id
        self.product_id = product.product_id
        self.quantity = quantity

    @property
    def orderItemId(self):
        return self.order_item_id

    @orderItemId.setter
    def orderItemId(self, order_item_id):
        self.order_item_id = order_item_id