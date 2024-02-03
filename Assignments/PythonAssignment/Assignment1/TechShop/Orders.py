import datetime

from Customers import Customers


class Orders(Customers):
    def __init__(self, orderID: int, customer, orderDate: datetime, totalAmount: float):
        self.orderID = orderID
        super().__init__(customer.customerID, customer.firstName, customer.lastName, customer.email, customer.phone, customer.address)
        self.orderDate = datetime.datetime.strptime(orderDate, "%Y-%m-%d").date()
        self.totalAmount = totalAmount
        self.status = "Processing"

    @property
    def getOrderid(self):
        return self.orderID

    @property
    def getOrderDate(self):
        return self.orderDate

    @property
    def getTotalAmount(self):
        return self.totalAmount

    @property
    def getStatus(self):
        return self.status

    @getOrderid.setter
    def setOrderid(self,oid):
        self.orderID = oid

    @getOrderDate.setter
    def setOrderDate(self,date):
        d = datetime.datetime.strptime(date,"%Y-%m-%d")
        self.orderDate = d

    @getTotalAmount.setter
    def setTotalAmount(self,am):
        try:
            if am >= 0:
                self.totalAmount = am
            else:
                raise ValueError("Amount can't be negative")
        except ValueError as v1:
            print("Please enter valid amount. ", v1)

    @getStatus.setter
    def setStatus(self, status):
        self.status = status

    def CalculateTotalAmount(self):
        return self.totalAmount

    def UpdateOrderStatus(self, status):
        self.status = status

    def CancelOrder(self):
        pass

    def getCustomerName(self):
        print(self.customer.customerName)
