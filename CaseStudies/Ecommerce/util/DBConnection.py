
import mysql
from mysql import connector

from util.PropertyUtil import PropertyUtil


class DBConnection:
    con = None

    @staticmethod
    def getConnection():
        if DBConnection.con is None:
            con_string = PropertyUtil.getPropertyString()
            DBConnection.con = mysql.connector.connect(**con_string)
            return DBConnection.con
