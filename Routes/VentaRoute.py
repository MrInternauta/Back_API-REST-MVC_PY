# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Model'))
import VentaModel as VentaModel
model = VentaModel.VentaModel()

def getAllVenta():
    valor = model.getAll()
    response = {
            "status": True,
            "data": valor
        }
    return response


    
def getOneVenta(id):
    valor = model.getOneById(id)
    response = {
        "status": True,
        "data": valor
    }
    return response

def putVenta(id, body):
    Venta = model.getOneById(id)
    Venta = Venta[0]
    if Venta:
        idVenta = body.get("idVenta", None)
        idCliente = body.get("idCliente", None) 
        idVendedor = body.get("idVendedor", None) 
        fecha = body.get("fecha", "2020/04/14") 

        model.setDataModel(idVenta, idCliente, idVendedor, fecha)
        valor = model.Update(id)
        Venta = model.getOneById(id)
        response = {
            "status": True,
            "Mensaje": "Venta Actualizada correctamente",
            "data": Venta
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No existe la Venta"
        }
        return errorResponse

def postVenta(body):
    idVenta = body.get("idVenta", None)
    idCliente = body.get("idCliente", None) 
    idVendedor = body.get("idVendedor", None) 
    fecha = body.get("fecha", "2020/04/14") 
    model.setDataModel(idVenta, idCliente, idVendedor, fecha)
    valor = model.Create()
    if(valor[0]):
        id = valor[0].get("id")
        Venta = model.getOneById(id)
        print(Venta)
        response = {
            "status": True,
            "Mensaje": "Venta Creada correctamente",
            "data": Venta
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No se pudo guardar la Venta"
        }
        return errorResponse