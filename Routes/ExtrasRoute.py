# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Model'))
import ExtrasModel as ExtrasModel
model = ExtrasModel.ExtrasModel()

def getAllExtras():
    valor = model.getAll()
    response = {
            "status": True,
            "data": valor
        }
    return response


    
def getOneExtras(id):
    valor = model.getOneById(id)
    response = {
        "status": True,
        "data": valor
    }
    return response


def putExtras(id, body):
    Extras = model.getOneById(id)
    Extras = Extras[0]
    if Extras:
        idExtras = body.get("idExtras", None)
        nombreExtra = body.get("nombreExtra", None) 
        PrecioExtra = body.get("PrecioExtra", None) 
        model.setDataModel(idExtras, nombreExtra, PrecioExtra)
        valor = model.Update(id)
        Extras = model.getOneById(id)
        response = {
            "status": True,
            "Mensaje": "Extras Actualizado correctamente",
            "data": Extras
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No existe la Extras"
        }
        return errorResponse

def postExtras(body):
    idExtras = body.get("idExtras", None)
    nombreExtra = body.get("nombreExtra", None) 
    PrecioExtra = body.get("PrecioExtra", None) 
    model.setDataModel(idExtras, nombreExtra, PrecioExtra)
    valor = model.Create()
    if(valor[0]):
        id = valor[0].get("id")
        Extras = model.getOneById(id)
        print(Extras)
        response = {
            "status": True,
            "Mensaje": "Extras Creada correctamente",
            "data": Extras
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No se pudo guardar la Extras"
        }
        return errorResponse