class Customer:
    def __init__(self, name, email, password):
        self.customer_id = None
        self.name = name
        self.email = email
        self.password = password

    @property
    def customerid(self):
        return self.customer_id

    @customerid.setter
    def customerid(self, customer_id):
        self.customer_id = customer_id
