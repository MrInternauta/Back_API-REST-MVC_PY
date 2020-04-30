# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Model'))
import ExtrasProductosModel as ExtrasProductosModel
model = ExtrasProductosModel.ExtrasProductosModel()

def getAllExtrasProductos():
    valor = model.getAll()
    response = {
            "status": True,
            "data": valor
        }
    return response


    
def getOneExtrasProductos(id):
    valor = model.getOneById(id)
    response = {
        "status": True,
        "data": valor
    }
    return response

def putExtrasProductos(id, body):
    ExtrasProductos = model.getOneById(id)
    ExtrasProductos = ExtrasProductos[0]
    if ExtrasProductos:
        idExtras = body.get("idExtras", None)
        idProducto = body.get("idProducto", "") 
        model.setDataModel(idExtras, idProducto)
        valor = model.Update(id)
        ExtrasProductos = model.getOneById(id)
        response = {
            "status": True,
            "Mensaje": "ExtrasProductos Actualizado correctamente",
            "data": ExtrasProductos
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No existe el ExtrasProductos"
        }
        return errorResponse

def postExtrasProductos(body):
    idExtras = body.get("idExtras", None)
    idProducto = body.get("idProducto", "") 
    model.setDataModel(idExtras, idProducto)
    if(valor[0]):
        id = valor[0].get("id")
        ExtrasProductos = model.getOneById(id)
        print(ExtrasProductos)
        response = {
            "status": True,
            "Mensaje": "ExtrasProductos Creado correctamente",
            "data": ExtrasProductos
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No se pudo guardar la ExtrasProductos"
        }
        return errorResponse