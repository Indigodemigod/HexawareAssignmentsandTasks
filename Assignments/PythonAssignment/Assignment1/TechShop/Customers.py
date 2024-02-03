class InvalidDataException(Exception):
    def __init__(self, message):
        self.message = message


class Customers:
    def __init__(self, customerID: int, firstName: str, lastName: str, email: str, phone: str, address: str):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.address = address

    @property
    def getCustomerId(self):
        return self.customerID

    @getCustomerId.setter
    def setCustomerId(self, cid):
        self.customerID = cid

    @property
    def getName(self):
        return self.firstName + self.lastName

    @getName.setter
    def setName(self, fName, lName):
        self.firstName = fName
        self.lastName = lName

    @property
    def getEmail(self):
        return self.email

    @getEmail.setter
    def setEmail(self, email):
        try:
            if '@' in email:
                self.email = email
            else:
                raise InvalidDataException("Invalid email")
        except InvalidDataException as idv:
            print("@ is missing in the input provided. ", idv)

    def CalculateTotalOrders(self):
        pass

    def GetCustomerDetails(self):
        print("Customer ID = ", self.customerID)
        print("Customer Name = ", self.firstName, self.lastName)
        print("Customer Email = ", self.email)
        print("Customer Phone = ", self.phone)
        print("Customer Address = ", self.address)

    def UpdateCustomerInfo(self, email):
        self.email = email
