from entity.Customers import Customer


class Order(Customer):
    def __init__(self, customer, order_date, total_price, shipping_address):
        self.order_id = None
        self.customer_id = customer.customerid
        self.order_date = order_date
        self.total_price = total_price
        self.address = shipping_address

    @property
    def orderid(self):
        return self.order_id

    @orderid.setter
    def orderid(self, order_id):
        self.order_id = order_id