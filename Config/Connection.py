# -*- coding: utf-8 -*-
from mysql import connector as con
class Connection():
    __db = "McDonals"
    __user = "root"
    __password = ""
    values = []
    def __init__(self):
        pass

    def __getConnection(self):
        conex = con.connect(host="localhost", user=self.__user,
                            passwd=self.__password, db= self.__db)
        return conex

    def ejecuteQuery(self, sql):
        try:
            con = self.__getConnection()
            rs = con.cursor()
            rs.execute(sql)
            row_headers=[x[0] for x in rs.description] #this will extract row headers
            rv = rs.fetchall()
            json_data=[]
            for result in rv:
                    json_data.append(dict(zip(row_headers,result)))
            self.values = json_data

            con.close()
        except Exception as ex:
            print(ex)

        finally:
            return self.values

    def InsertRows(self,sql, valores):
        try:
            conn = self.__getConnection(self)
            rs = conn.cursor()
            rs.executemany(sql, valores)
            conn.commit()
            print(rs)
            for row in rs:
                print(row)
            conn.close()
        except Exception as ex:
            print(ex)
    
    
    def InsertRow(self,sql):
        try:
            conn = self.__getConnection()
            rs = conn.cursor()
            rs.execute(sql)
            conn.commit()
            print(rs)
            for row in rs:
                print(row)
            conn.close()
        except Exception as ex:
            print(ex)