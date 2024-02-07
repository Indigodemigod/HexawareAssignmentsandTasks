from abc import ABC,abstractmethod
from entity.Products import Product
from entity.Customers import Customer


class OrderProcessorRepository(ABC):
    @abstractmethod
    def createProduct(self, product: Product) -> bool:
        pass

    @abstractmethod
    def createCustomer(self, customer: Customer) -> bool:
        pass

    @abstractmethod
    def deleteProduct(self, product_id) -> bool:
        pass

    @abstractmethod
    def deleteCustomer(self, customer_id) -> bool:
        pass

    @abstractmethod
    def addToCart(self, customer: Customer, product: Product, quantity) -> bool:
        pass

    @abstractmethod
    def removeFromCart(self, customer: Customer, product: Product) -> bool:
        pass

    @abstractmethod
    def get_customer_by_id(self, customer_id):
        pass

    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def getAllFromCart(self, customer: Customer) -> list:
        pass

    @abstractmethod
    def placeOrder(self, customer: Customer, product_quantities: list, shipping_address) -> bool:
        pass

    @abstractmethod
    def getOrdersByCustomers(self, customer: Customer) -> list:
        pass
