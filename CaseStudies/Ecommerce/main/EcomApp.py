from myexceptions.CustomerNotFound import CustomerNotFoundException
from entity.Customers import Customer
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from myexceptions.ProductNotFound import ProductNotFoundException
from entity.Products import Product


class EcomApp(OrderProcessorRepositoryImpl):
    def __init__(self):
        super().__init__()

    def main(self):
        while True:
            print("Enter your choice from the menu below : ")
            print("----- Menu -----")
            print("1. Register Customer")
            print("2. Create Product")
            print("3. Delete Product")
            print("4. Add to cart")
            print("5. View cart")
            print("6. Place order")
            print("7. View Customer Order")
            print("8. Exit")
            choice = int(input("Enter your choice here : "))
            match choice:
                case 1:
                    name = input("Enter your name here : ")
                    email = input("Enter your email here : ")
                    password = input("Enter your password here : ")
                    customer = Customer(name, email, password)
                    customer_created = self.createCustomer(customer)
                    if customer_created:
                        print("Customer registered successfully. Congratulations.")
                        print(f"Your customer id is {customer.customer_id}")
                        print()

                case 2:
                    name = input("Enter product name : ")
                    price = float(input("Enter price of the product here : "))
                    category = input("Enter category of product : ")
                    quantity = int(input("Enter number of item : "))
                    product = Product(name, price, category, quantity)
                    product_created = self.createProduct(product)
                    if product_created:
                        print("Product added successfully. Congratulations.")
                        print(f"Your product id is {product.product_id}")
                        print()

                case 3:
                    product_id = int(input("Enter your product id here : "))
                    deleted_product = self.deleteProduct(product_id)
                    if deleted_product:
                        print("Product deleted successfully.")
                        print()
                case 4:
                    customer_id = int(input("Enter customer id : "))
                    product_id = int(input("Enter product id : "))
                    quantity = int(input("Enter number of items : "))
                    customer = self.get_customer_by_id(customer_id)
                    product = self.get_product_by_id(product_id)
                    if product and customer:
                        self.addToCart(customer, product, quantity)
                        print("Product added to cart successfully.")
                    else:
                        print("Product or customer not found.")
                    print()
                case 5:
                    customer_id = int(input("Enter your customer id : "))
                    customer = self.get_customer_by_id(customer_id)
                    try:
                        if customer:
                            cart_items = self.getAllFromCart(customer)
                            for cart in cart_items:
                                print("Cart Id : ", cart[0])
                                print("Customer Id : ", cart[1])
                                print("Product Id : ", cart[2])
                                print("Quantity : ", cart[3])
                                print("-------------------")
                        else:
                            raise CustomerNotFoundException("Customer not found.")
                    except CustomerNotFoundException as e1:
                        print("Error. ", e1)
                case 6:
                    customer_id = int(input("Enter your customer id : "))
                    customer = self.get_customer_by_id(customer_id)
                    products_quantities = []
                    while True:
                        product_id = int(input("Please enter product_id(0 to stop) : "))
                        if product_id == 0:
                            break
                        quantity = int(input("Enter the quantity for this item : "))
                        product = self.get_product_by_id(product_id)
                        try:
                            if product:
                                products_quantities.append((product, quantity))
                            else:
                                raise ProductNotFoundException(f"Product not found for product id {product_id}")
                        except ProductNotFoundException as p1:
                            print("Error while getting product.", p1)
                    shipping_address = input("Enter your address where you want the orders : ")
                    orders_placed = self.placeOrder(customer, products_quantities, shipping_address)
                    if orders_placed:
                        print("Orders placed successfully! ")
                        print("We're heading you to main menu.")
                        print()
                    else:
                        print("Error while placing order.")
                        print()

                case 7:
                    customer_id = int(input("Enter your customer id : "))
                    customer = self.get_customer_by_id(customer_id)
                    try:
                        if customer:
                            products_quantities = self.getOrdersByCustomers(customer)
                            for product_quantity in products_quantities:
                                print("Product id : ", product_quantity[0])
                                print("Product Name : ", product_quantity[1])
                                print("Price : ", product_quantity[2])
                                print("Category : ", product_quantity[3])
                                print("Quantity : ", product_quantity[5])
                                print("------------------------")
                            print("Order details fetched successfully.")
                            print()
                        else:
                            raise CustomerNotFoundException("Customer not present in database.")
                    except CustomerNotFoundException as c1:
                        print("Error fetching customer. ", c1)
                        print()
                case 8:
                    print("Thanks for visiting our Ecommerce app. Please visit again.")
                    break
                case _:
                    print("Invalid input. Please try again.")


ecom = EcomApp()
ecom.main()
