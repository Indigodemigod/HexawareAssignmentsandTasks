
class Customer:
    def __init__(self, name, email, phone, address, creditScore):
        self.customer_id = None
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.creditScore = creditScore

    @property
    def customerId(self):
        return self.customer_id

    @customerId.setter
    def customerId(self, customer_id):
        self.customer_id = customer_id
        