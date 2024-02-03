import Customers
from Orders import Orders
from Products import Products


class OrderDetails(Orders, Products):
    def __init__(self, orderDetailId: int, orders, products, quantity: int):
        self.orderDetailId = orderDetailId
        self.order = orders
        self.product = products
        self.quantity = quantity

    @property
    def getOrderDetailsId(self):
        return self.orderDetailId

    @getOrderDetailsId.setter
    def setOrderDetailsId(self,id):
        self.orderDetailId = id

    @property
    def getQuantity(self):
        return self.quantity

    @getQuantity.setter
    def setQuantity(self,q):
        try:
            if q >= 0:
                self.quantity = q
            else:
                raise ValueError("Quantity must be negative")
        except ValueError as v1:
            print("Invalid Quantity. ", v1)


    def CalculateSubTotal(self):
        totalAmount = self.order.totalAmount
        return totalAmount

    def GetOrderDetailInfo(self):
        print(f"OrderDetail ID = {self.orderDetailId} ")
        print(f"Product Name = {self.product.productName}")
        print(f"Quantity = {self.quantity}")

    def UpdateQuantity(self, newQuantity):
        try:
            if newQuantity >= 0:
                self.quantity = newQuantity
            else:
                raise ValueError("Quantity must be positive")
        except ValueError as e1:
            print("Sorry! You must enter a valid quantity.",e1)

    def AddDiscount(self):
        pass
