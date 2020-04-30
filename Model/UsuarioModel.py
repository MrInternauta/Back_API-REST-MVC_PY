# -*- coding: utf-8 -*-
from BaseModel import BaseModel as BM 

class UsuarioModel(BM):
    def __init__(self):
      self.tableName = 'Usuario'
      self.idName = 'idUsuario'
      self.Base = BM(self.tableName, self.idName)
      self.rows = {}

    def setDataModel(self, idUsuario, nombreUsuario, apellidoUsuario, emailUsuario, passwordUsuario, idRol):
        self.rows['nombreUsuario'] = nombreUsuario
        self.rows['apellidoUsuario'] = apellidoUsuario
        self.rows['emailUsuario'] = emailUsuario
        self.rows['passwordUsuario'] = passwordUsuario
        self.rows['idUsuario'] = idUsuario
        self.rows['idRol'] = idRol
        self.Base.setRows(self.rows)

    def getAll(self):
        return self.Base.getAll()

    def getOneById(self, id):
        return self.Base.getOneById(id)

    def Create(self):
        return self.Base.Create()
    
    def Update(self, id):
        self.Base.Update(id)




# usuarioModel = UsuarioModel("Usuario", "idUsuario")
# usuarioModel.setDataModel(None, "Felipe2", "Ramirez2", "feldjesus2", "1234", None)
# usuarioModel.Update(4)
# usuarioModel.Create()
# usuarioModel.getOneById(4)
#usuarioModel.getAll()
