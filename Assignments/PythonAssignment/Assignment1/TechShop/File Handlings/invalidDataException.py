class InvalidDataException(Exception):
    def __init__(self,message):
        self.message = message

def user_registration():
    try:
        customer_name = input("Enter name : ")
        customer_email = input("Enter email : ")
        if '@' not in customer_email or '.' not in customer_email:
            raise InvalidDataException("'@' or '.' is missing!")
        print("User registration done")
    except InvalidDataException as idv:
        print("Invalid input : ", idv)