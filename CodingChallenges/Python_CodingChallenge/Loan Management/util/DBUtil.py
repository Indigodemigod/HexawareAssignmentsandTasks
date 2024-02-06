from mysql import connector
import mysql


class DBUtil:
    @staticmethod
    def getDBConn():
        con = mysql.connector.connect(
            host = "localhost",
            port = "3306",
            user = "root",
            password = "root",
            database = "loanManagement"
        )
        return con