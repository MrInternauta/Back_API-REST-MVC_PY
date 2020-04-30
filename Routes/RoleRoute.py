# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Model'))
import RolModel as RolModel
model = RolModel.RolModel()

def getAllRol():
    valor = model.getAll()
    response = {
            "status": True,
            "data": valor
        }
    return response


    
def getOneRol(id):
    valor = model.getOneById(id)
    response = {
        "status": True,
        "data": valor
    }
    return response

def putRol(id, body):
    Rol = model.getOneById(id)
    Rol = Rol[0]
    if Rol:
        idRol = body.get("idRol", None)
        nombreRol = body.get("nombreRol", "") 
        model.setDataModel(id, nombreRol)
        valor = model.Update(id)
        Rol = model.getOneById(id)
        response = {
            "status": True,
            "Mensaje": "Rol Actualizado correctamente",
            "data": Rol
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No existe el Rol"
        }
        return errorResponse

def postRol(body):
    idRol = body.get("idRol", None)
    nombreRol = body.get("nombreRol", "") 
    model.setDataModel(idRol, nombreRol)
    valor = model.Create()
    if(valor[0]):
        id = valor[0].get("id")
        Rol = model.getOneById(id)
        print(Rol)
        response = {
            "status": True,
            "Mensaje": "Rol Creado correctamente",
            "data": Rol
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No se pudo guardar la Rol"
        }
        return errorResponse