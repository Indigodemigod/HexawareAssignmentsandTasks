from util.DBConnection import DBConnection

con = DBConnection.getConnection()
cursor = con.cursor()
cursor.execute("select products.*,order_items.quantity from order_items join products on "
               "products.product_id=order_items.product_id join orders on orders.order_id=order_items.order_id where "
               "customer_id=%s", (3,))
rows = cursor.fetchall()
for row in rows:
    print(row)