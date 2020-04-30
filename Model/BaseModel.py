# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Config'))
import Connection as C
class BaseModel():
    def __init__(self, __tableName, __idName):
      self.__tableName = __tableName
      self.__idName = __idName
      self.__rows = {}

    def setRows(self, rows):
        self.__rows = rows

    def getAll(self):
        query = str("SELECT * FROM " +  self.__tableName)
        return C.Connection().ejecuteQuery(query)

    def getOneById(self, id):
        query = str("SELECT * FROM " +  self.__tableName + " WHERE " + self.__idName + " = " +  str(id))
        return C.Connection().ejecuteQuery(query)

    def Create(self):
        valores = []
        sql = "INSERT INTO "+ self.__tableName + "("
        for idx, key in enumerate(self.__rows.keys()):
            if idx < len(self.__rows.keys()) - 1:
                sql = sql + "`"+key+"`,"
            else:
                sql = sql + "`"+key+"`) VALUES ("
        for idx, value in enumerate(self.__rows.values()):
            valores.append(value)
            if idx < len(self.__rows.values()) - 1:
                if value == None:
                    sql = sql + str('NULL')+","
                elif(type(value) is  int or type(value) is  float ):
                     sql = sql + str(value)+","
                else:
                    sql = sql + "'" + str(value)+"',"
                    
            else:
                if value == None:
                    sql = sql + str('NULL')+");"
                elif(type(value) is  int or type(value) is  float ):
                     sql = sql + str(value) + ");"
                else:
                    sql = sql + "'" + str(value)+"');"
                    
        C.Connection().InsertRow(sql)
        return C.Connection().ejecuteQuery("Select max( +" + self.__idName + ") as id from " + str(self.__tableName))
    
    def Update(self, id):
        valores = []
        sql = "UPDATE "+ self.__tableName + " SET "
        for idx, key in enumerate(self.__rows.keys()):
            if key != self.__idName:
                sql = sql + ""+key+" = "
                value = self.__rows[key]
                print(len(self.__rows.keys()), idx)
                if idx + 1 <= len(self.__rows.keys()) - 1:
                    if value == None:
                        sql = sql + str('NULL')+","
                    elif(type(value) is int or type(value) is  float ):
                        sql = sql + str(value)+","   

                    else:
                        sql = sql + "'" + str(value)+"',"
                    
                else:
                    if value == None:
                        sql = sql + str('NULL')+""
                    elif(type(value) is  int or type(value) is  float ):
                        sql = sql + str(value)+""
                    else:
                        sql = sql + "'" + str(value)+"'"
        if sql[-1:] == ",":
            sql = sql[:-1]
        sql = sql + " WHERE " + self.__idName + " = " +  str(id) + ";"   
        print(sql) 
        C.Connection().InsertRow(sql)
