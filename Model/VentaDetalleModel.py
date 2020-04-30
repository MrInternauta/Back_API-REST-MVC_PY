# -*- coding: utf-8 -*-
from BaseModel import BaseModel as BM 

class VentaDetalleModel(BM):
    def __init__(self):
      self.tableName = 'VentaDetalle'
      self.idName = 'idVentaDetalle'
      self.Base = BM(self.tableName, self.idName)
      self.rows = {}

    def setDataModel(self, idVentaDetalle, idProducto, cotidad_vendida, descuento, idVenta):
        self.rows['idVentaDetalle'] = idVentaDetalle
        self.rows['idProducto'] = idProducto
        self.rows['cotidad_vendida'] = cotidad_vendida
        self.rows['descuento'] = descuento
        self.rows['idVenta'] = idVenta
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
