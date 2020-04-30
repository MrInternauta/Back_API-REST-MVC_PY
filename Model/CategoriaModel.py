# -*- coding: utf-8 -*-
from BaseModel import BaseModel as BM 

class CategoriaModel(BM):
    def __init__(self):
      self.tableName = 'Categoria'
      self.idName = 'idCategoria'
      self.Base = BM(self.tableName, self.idName)
      self.rows = {}

    def setDataModel(self, idCategoria, nombreCategoria):
        self.rows['idCategoria'] = idCategoria
        self.rows['nombreCategoria'] = nombreCategoria
        self.Base.setRows(self.rows)

    def getAll(self):
        return self.Base.getAll()

    def getOneById(self, id):
        return self.Base.getOneById(id)

    def Create(self):
        return self.Base.Create()
    
    def Update(self, id):
        self.Base.Update(id)
