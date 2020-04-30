# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Model'))
import VentaDetalleModel as VentaDetalleModel
model = VentaDetalleModel.VentaDetalleModel()

def getAllVentaDetalle():
    valor = model.getAll()
    response = {
            "status": True,
            "data": valor
        }
    return response


    
def getOneVentaDetalle(id):
    valor = model.getOneById(id)
    response = {
        "status": True,
        "data": valor
    }
    return response

def putVentaDetalle(id, body):
    VentaDetalle = model.getOneById(id)
    VentaDetalle = VentaDetalle[0]
    if VentaDetalle:
        idVentaDetalle = body.get("idVentaDetalle", None)
        idProducto = body.get("idProducto", None) 
        contidad_vendida = body.get("contidad_vendida", 0) 
        descuento = body.get("descuento", 0) 
        idVenta = body.get("idVenta", None) 

        model.setDataModel(idVentaDetalle, idProducto, contidad_vendida, descuento, idVenta)
        valor = model.Update(id)
        VentaDetalle = model.getOneById(id)
        response = {
            "status": True,
            "Mensaje": "VentaDetalle Actualizada correctamente",
            "data": VentaDetalle
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No existe la VentaDetalle"
        }
        return errorResponse

def postVentaDetalle(body):
     idVentaDetalle = body.get("idVentaDetalle", None)
    idProducto = body.get("idProducto", None) 
    contidad_vendida = body.get("contidad_vendida", 0) 
    descuento = body.get("descuento", 0) 
    idVenta = body.get("idVenta", None) 
    model.setDataModel(idVentaDetalle, idProducto, contidad_vendida, descuento, idVenta)
    valor = model.Create()
    if(valor[0]):
        id = valor[0].get("id")
        VentaDetalle = model.getOneById(id)
        print(VentaDetalle)
        response = {
            "status": True,
            "Mensaje": "VentaDetalle Creada correctamente",
            "data": VentaDetalle
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No se pudo guardar la VentaDetalle"
        }
        return errorResponse