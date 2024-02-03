from abc import *


class TechShopService:
    @abstractmethod
    def user_registration(self):
        pass

    @abstractmethod
    def changes_in_products(self):
        pass

    @abstractmethod
    def placing_order(self):
        pass

    @abstractmethod
    def get_order_status(self):
        pass

    @abstractmethod
    def manage_inventory(self):
        pass

    @abstractmethod
    def report_sales(self):
        pass

    @abstractmethod
    def customer_updates(self):
        pass

    @abstractmethod
    def process_payments(self):
        pass

    @abstractmethod
    def search_products(self):
        pass
