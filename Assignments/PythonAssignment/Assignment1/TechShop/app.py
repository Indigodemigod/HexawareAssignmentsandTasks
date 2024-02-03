from DBUtil import DBUtil
from TechShopImpl import TechShopServiceImpl


class TechShop(TechShopServiceImpl):
    def __init__(self, dbUtil):
        super().__init__(dbUtil)

    def main(self):
        while True:
            print("Please select the choices from below : ")
            print("1. Customer Registration. ")
            print("2. Update Product Info.")
            print("3. Place New Order")
            print("4. Tracking Order Status")
            print("5. Inventory Management")
            print("6. Sales Reporting")
            print("7. Customer Account Updates")
            print("8. Payment Processing")
            print("9. Product Search and Recommendations")
            print("10. Exit")
            choice = int(input("Enter your choice here : "))
            match choice:
                case 1:
                    self.user_registrati1on()
                    print("Thank you for registering with us.")
                    print("We're heading you to main menu.")
                case 2:
                    self.changes_in_products()
                    print("Changes made successfully!")
                    print("We're heading you to main menu.")
                case 3:
                    self.placing_order()
                    print("Order placed successfully.")
                    print("We're heading you to main menu.")
                case 4:
                    self.get_order_status()
                    print("We're heading you to main menu.")
                case 5:
                    self.manage_inventory()
                    print("We're heading you to main menu.")
                case 6:
                    self.report_sales()
                    print("We're heading you to main menu.")
                case 7:
                    self.customer_updates()
                    print("Updates were successful.")
                    print("We're heading you to main menu.")
                case 8:
                    self.process_payments()
                    print("We're heading you to main menu.")
                case 9:
                    self.search_products()
                    print()
                case 10:
                    print("Thanks for visiting us. See you anytime soon.")


dbutil = DBUtil()
techshop = TechShop(dbutil)
techshop.main()

