from datetime import date
from abc import ABC

from TechShopService import TechShopService


class TechShopServiceImpl(TechShopService, ABC):
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def customer_updates(self):
        customer_id = int(input("Please enter your customer id : "))
        print("Tell us what you want to do : ")
        print("1. Update email.")
        print("2. Update phone number.")
        print("3. Update address. ")
        cursor = self.dbUtil.getDBConnection()
        choice = int(input("Enter your choice here : "))
        match choice:
            case 1:
                email_id = input("Enter your new email address : ")
                cursor.execute("select email from customers where customerid=%s", (customer_id,))
                old_mails = cursor.fetchone()
                if old_mails:
                    old_email = old_mails[0]
                cursor.execute("update customers set email=%s where customerid=%s", (email_id, customer_id,))
                self.dbUtil.con.commit()
                print(f"Your email is updated from {old_email} to {email_id} successfully.")
            case 2:
                phone_number = input("Enter your new phone number : ")
                cursor.execute("select phone from customers where customerid=%s", (customer_id,))
                old_numbers = cursor.fetchone()
                if old_numbers:
                    old_number = old_numbers[0]
                cursor.execute("update customers set phone=%s where customerid=%s", (phone_number, customer_id,))
                self.dbUtil.con.commit()
                print(f"Your phone number is updated successfully from {old_number} to {phone_number}")
            case 3:
                address = input("Enter your new address : ")
                cursor.execute("select address from customers where customerid=%s", (customer_id,))
                adress = cursor.fetchone()
                if adress:
                    old_address = adress[0]
                cursor.execute("update customers set address=%s where customerid=%s", (address, customer_id,))
                self.dbUtil.con.commit()
                print(f"Your address is updated successfully from {old_address} to {address}")
            case _:
                print("Invalid input.")
        print()

    def changes_in_products(self):
        cursor = self.dbUtil.getDBConnection()
        print("What you want to do with product catalogue? ")
        print("1. Add new product.")
        print("2. Update product price. ")
        print("3. Update product description. ")
        choice = int(input("Enter your choice : "))
        match choice:
            case 1:
                product_name = input("Enter the name of product : ")
                description = input("Enter description of product : ")
                price = float(input("Enter price for the product : "))
                query = "insert into products(productname,description,price) values(%s,%s,%s)"
                cursor.execute(query, (product_name, description, price,))
                self.dbUtil.con.commit()
                cursor.execute("select productid from products where productname=%s and description=%s",
                               (product_name, description,))
                productid = cursor.fetchone()
                if productid:
                    product_id = productid[0]
                quantity = int(input("Enter the number of items : "))
                date_today = date.today()
                cursor.execute("insert into inventory(productid,quantityinstock,laststockupdate) values(%s,%s,%s)",
                               (product_id, quantity, date_today))
                self.dbUtil.con.commit()
                print(f"Product added successfully with productid {product_id}")
            case 2:
                product_id = int(input("Enter product id : "))
                new_price = float(input("Enter new price : "))
                cursor.execute("update products set price=%s where productid=%s", (new_price, product_id,))
                self.dbUtil.con.commit()
                print("Price updated successfully.")
            case 3:
                product_id = int(input("Enter product id : "))
                description = input("Enter new description of product : ")
                cursor.execute("update products set description=%s where productid=%s", (description, product_id))
                self.dbUtil.con.commit()
                print("Description updated successfully")
            case _:
                print("Invalid input.")
        print()

    def placing_order(self):
        cursor = self.dbUtil.getDBConnection()
        print("Please choose from the products below what you want to order : ")
        cursor.execute("select * from products")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        product_id = int(input("Please enter your product id here : "))
        quantity = int(input("Enter the number of items you want to order : "))
        new_customer = input("Are you a new customer? Enter yes or no : ")
        match new_customer:
            case "yes":
                first_name = input("First name : ")
                last_name = input("Last name : ")
                email = input("Email : ")
                try:
                    if '@' in email and '.' in email:
                        pass
                    else:
                        raise Exception("Incorrect input.")
                except Exception as e1:
                    print("@ or . is missing. ", e1)
                phone = input("Phone : ")
                address = input("Address : ")
                q = "insert into customers(firstname,lastname,email,phone,address) values (%s,%s,%s,%s,%s)"
                cursor.execute(q, (first_name, last_name, email, phone, address,))
                self.dbUtil.con.commit()
                cursor.execute("select customerid from customers where firstname=%s and email=%s", (first_name, email,))
                customer = cursor.fetchone()
                if customer:
                    customer_id = customer[0]
            case "no":
                customer_id = int(input("Enter your customer id : "))
            case _:
                print("Invalid input")
        cursor.execute("select price from products where productid=%s", (product_id,))
        amount = cursor.fetchone()
        if amount:
            total_amount = amount[0] * quantity
        date_today = date.today()
        placing_order = "insert into orders(customerid,orderdate,totalamount) values (%s,%s,%s)"
        cursor.execute(placing_order, (customer_id, date_today, total_amount,))
        self.dbUtil.con.commit()
        cursor.execute("select orderid from orders where customerid=%s and orderdate=%s", (customer_id, date_today,))
        orderid = cursor.fetchall()
        if orderid:
            order_id = orderid[-1][-1]
        orderdetailsupdate = "insert into orderdetails(orderid,productid,quantity) values(%s,%s,%s)"
        cursor.execute(orderdetailsupdate, (order_id, product_id, quantity,))
        self.dbUtil.con.commit()
        cursor.execute("select quantityinstock from inventory where productid=%s", (product_id,))
        quantity_in = cursor.fetchone()
        if quantity_in:
            quantity_in_stock = quantity_in[0]
        cursor.execute("update inventory set quantityinstock = %s where productid=%s",
                       (quantity_in_stock - quantity, product_id,))
        self.dbUtil.con.commit()
        print(f"Congratulations! Your order is successfully placed. Your order id is {order_id} and your total cost is {total_amount}")
        print()

    def get_order_status(self):
        order_id = int(input("Please enter your order id : "))
        cursor = self.dbUtil.getDBConnection()
        cursor.execute("select status from orders where orderid=%s", (order_id,))
        orders_result = cursor.fetchone()
        if orders_result is not None:
            status = orders_result[0]
        else:
            print("Incorrect order id please try again")
            self.get_order_status()
        print(f"Your order with order id {order_id} is {status}. Rest assured and contact us for further enquiry")
        print()

    def manage_inventory(self):
        cursor = self.dbUtil.getDBConnection()
        print("Select from below what you want to do.")
        print("1. Add new product.")
        print("2. Update any product quantity stock.")
        print("3. Remove discontinued products.")
        choice = int(input("Enter your choice here : "))
        match choice:
            case 1:
                product_name = input("Enter product name : ")
                category = input("Enter category of product : ")
                price = float(input("Enter price of the product : "))
                cursor.execute("insert into products(productname, description, price) values (%s,%s,%s)",(product_name, category, price, ))
                self.dbUtil.con.commit()
                cursor.execute("select productid from products where productname=%s limit 1", (product_name,))
                product_ids = cursor.fetchone()
                if product_ids:
                    product_id = product_ids[0]
                date_today = date.today()
                quantity = int(input("Enter the stock of product (quantity) : "))
                cursor.execute("insert into inventory(productid,quantityinstock,laststockupdate) values (%s,%s,%s)", (product_id, quantity, date_today, ))
                self.dbUtil.con.commit()
                cursor.execute("select inventoryid from inventory where productname=%s and laststockupdate=%s limit 1", (product_name, date_today, ))
                in_ids = cursor.fetchone()
                if in_ids:
                    inventory_id = in_ids[0]
                print(f"Product is added to inventory and products successfully and your product id is {product_id} where inventory id is {inventory_id} .")
                print("Heading you to main menu.")
            case 2:
                product_id = int(input("Please provide product id whose quantity you want to update : "))
                cursor.execute("select inventoryid from inventory where productid=%s limit 1", (product_id, ))
                inventory_id = cursor.fetchone()[0]
                quantity = int(input("Enter new quantity : "))
                date_today = date.today()
                cursor.execute("update inventory set quantityinstock=%s, laststockupdate=%s where productid=%s", (quantity, date_today, product_id, ))
                self.dbUtil.con.commit()
                print(f"Your updates are implemented successfully for inventory id {inventory_id}")
            case 3:
                product_id = int(input("Please enter product id of the product discontinued : "))
                cursor.execute("update inventory set quantity=0, laststockupdate=%s where productid=%s", (date.today(), product_id, ))
                self.dbUtil.con.commit()
            case _:
                print("Invalid input.")
                print("Try again.")
                self.manage_inventory()
        print("Heading you to main menu. ")
        print()

    def report_sales(self):
        cursor = self.dbUtil.getDBConnection()
        cursor.execute("select sum(totalamount),orderdate from orders group by orderdate")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("These are amount sums according to order date.")

    def user_registration(self):
        cursor = self.dbUtil.getDBConnection()
        first_name = input("Please enter your first name : ")
        last_name = input("Please enter your last name : ")
        email = input("Please enter your email : ")
        if '@' not in email or '.' not in email:
            raise Exception("Invalid email. '@' or '.' either is missing")
        phone = input("Please enter your phone number : ")
        address = input("Please enter your address : ")
        try:
            query = "insert into customers(firstname,lastname,email,phone,address) values (%s,%s,%s,%s,%s)"
            cursor.execute(query, (first_name, last_name, email, phone, address,))
            self.dbUtil.con.commit()
            cursor.execute("select * from customers")
            rows = cursor.fetchall()
            if rows:
                print(rows[-1:])
                print("Your customer id is ", rows[-1][0])
            print("Congratulations. You're registered successfully. You can view all your details above. ")
            print()
        except Exception as e1:
            print("Seems like SQL Error.", e1)

    def process_payments(self):
        print("The payment server is low at the time please come back later. Sorry for the inconvenience.")

    def search_products(self):
        cursor = self.dbUtil.getDBConnection()
        cursor.execute("select * from products")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        product_name = input("Please enter product name : ")
        cursor.execute("select * from products where productname=%s", (product_name,))
        product = cursor.fetchall()
        for p in product:
            print(p)
        cursor.execute("select description from products where productname = %s", (product_name,))
        des = cursor.fetchone()
        if des:
            description = des[0]
        cursor.execute("select * from products where description=%s", (description,))
        products = cursor.fetchall()
        print("Recommended Products .")
        for p in products:
            print(p)
        print("Go to place order section to order something.")
        print()
