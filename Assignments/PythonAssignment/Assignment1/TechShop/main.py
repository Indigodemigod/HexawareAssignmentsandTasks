import mysql
from mysql import connector

con = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = "root",
    database = "techshop"
)

con.cursor()
