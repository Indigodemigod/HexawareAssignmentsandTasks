from abc import ABC
from datetime import date

from myexceptions.CustomerNotFound import CustomerNotFoundException
from entity.Customers import Customer
from util.DBConnection import DBConnection
from myexceptions.OrderNotFound import OrderNotFoundException
from dao.OrderProcessorRepository import OrderProcessorRepository
from myexceptions.ProductNotFound import ProductNotFoundException
from entity.Products import Product


class OrderProcessorRepositoryImpl(OrderProcessorRepository, ABC):
    def __init__(self):
        self.con = DBConnection.getConnection()

    def createCustomer(self, customer: Customer) -> bool:
        try:
            name = customer.name
            email = customer.email
            if '@' not in email or '.' not in email:
                raise Exception("@ or . missing")
            password = customer.password
            cursor = self.con.cursor()
            cursor.execute("insert into customers(name,email,password) values(%s,%s,%s)", (name, email, password,))
            self.con.commit()
            customer.customer_id = cursor.lastrowid
            return True
        except Exception as e1:
            print("Error while registering customer. ", e1)
            return False

    def createProduct(self, product: Product) -> bool:
        name = product.name
        price = product.price
        category = product.category
        quantity = product.stockQuantity
        cursor = self.con.cursor()
        flag = 0
        try:
            query = "insert into products(name,price,category,stockquantity) values(%s,%s,%s,%s)"
            cursor.execute(query, (name, price, category, quantity,))
            self.con.commit()
            product.product_id = cursor.lastrowid
            print(f"Your product id is {product.product_id}. Remember it for future reference")
            flag = 1
            return True
        except Exception as e1:
            print("Error while adding product. ", e1)
            return False

    def deleteCustomer(self, customer_id) -> bool:
        pass

    def deleteProduct(self, product_id) -> bool:
        cursor = self.con.cursor()
        try:
            cursor.execute("delete from products where product_id=%s", (product_id,))
            self.con.commit()
            return True
        except Exception as e1:
            print(f"Sorry. We can't find product id {product_id}", e1)
            return False

    def placeOrder(self, customer: Customer, product_quantities: list, shipping_address) -> bool:
        customer_id = customer.customer_id
        cursor = self.con.cursor()
        try:
            for product, quantity in product_quantities:
                product_id = product.product_id
                date_today = date.today()
                total_price = product.price * quantity
                address = shipping_address
                cursor.execute("select stockquantity from products where product_id = %s", (product_id, ))
                quat = cursor.fetchone()
                if quat[0] >= quantity:
                    q_updateOrder = "update products set stockquantity=%s where product_id=%s"
                    cursor.execute(q_updateOrder, (quat[0]-quantity, product_id, ))
                    self.con.commit()
                    q_placeOrder = "insert into orders(customer_id,orderdate,total_price,shipping_address) values(%s,%s,%s,%s)"
                    cursor.execute(q_placeOrder, (customer_id, date_today, total_price, address))
                    self.con.commit()
                    order_id = cursor.lastrowid
                    print(f"This order product with product id {product_id} has order id {order_id}. Your total order value is worth {total_price}.")
                    q_orderItem = "insert into order_items(order_id, product_id, quantity) values(%s,%s,%s)"
                    cursor.execute(q_orderItem, (order_id, product_id, quantity,))
                    self.con.commit()
                    order_item_id = cursor.lastrowid
                    print(f"Your order item id is {order_item_id}")
                    return True
                else:
                    print("Not enough stock available.")
        except Exception as e1:
            print("Something happened while placing order try again.", e1)
            return False


    def addToCart(self, customer: Customer, product: Product, quantity) -> bool:
        customer_id = customer.customer_id
        product_id = product.product_id
        cursor = self.con.cursor()
        query = "insert into cart(customer_id, product_id, quantity) values(%s,%s,%s)"
        try:
            cursor.execute(query, (customer_id, product_id, quantity,))
            self.con.commit()
            cart_id = cursor.lastrowid
            print(f"Your item is added to cart successfully. Your cart id is {cart_id}")
            return True
        except Exception as e1:
            print("There was some issue adding item to cart.", e1)
            return False

    def getAllFromCart(self, customer: Customer) -> list:
        try:
            cursor = self.con.cursor()
            q = "select products.* from cart join products on cart.product_id=products.product_id where customer_id=%s"
            c_id = customer.customer_id
            cursor.execute(q, (c_id,))
            return cursor.fetchall()
        except Exception as e1:
            print("Problem while fetching cart details. ", e1)

    def getOrdersByCustomers(self, customer: Customer) -> list:
        customer_id = customer.customer_id
        cursor = self.con.cursor()
        query = ("select products.*,order_items.quantity from order_items join products on "
                 "products.product_id=order_items.product_id join orders on orders.order_id=order_items.order_id where "
                 "customer_id=%s")
        cursor.execute(query, (customer_id, ))
        product_details = cursor.fetchall()
        try:
            if product_details:
                return product_details
            else:
                raise OrderNotFoundException(f"No orders found for customer id {customer_id}")
        except OrderNotFoundException as o1:
            print("Error while fetching order details", o1.message)

    def removeFromCart(self, customer: Customer, product: Product) -> bool:
        pass

    def get_customer_by_id(self, customer_id):
        cursor = self.con.cursor()
        try:
            cursor.execute("select * from customers where customer_id=%s", (customer_id,))
            c_data = cursor.fetchone()
            if c_data:
                customer = Customer(c_data[1], c_data[2], c_data[3])
                customer.customer_id = c_data[0]
                return customer
            else:
                raise CustomerNotFoundException(f"Customer with customer id {customer_id} not found.")
        except CustomerNotFoundException as e1:
            print("Error while getting customer.", e1.message)

    def get_product_by_id(self, product_id):
        cursor = self.con.cursor()
        try:
            cursor.execute("select * from products where product_id=%s", (product_id,))
            p_data = cursor.fetchone()
            if p_data:
                product = Product(p_data[1], p_data[2], p_data[3], p_data[4])
                product.product_id = p_data[0]
                return product
            else:
                raise ProductNotFoundException(f"Product with product id {product_id} not found.")
        except ProductNotFoundException as e1:
            print("Error while getting product. ", e1.message)
