# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Model'))
import CategoriaModel as CategoriaModel
CategoriaM = CategoriaModel.CategoriaModel()

def getAllCategoria():
    valor = CategoriaM.getAll()
    response = {
            "status": True,
            "data": valor
        }
    return response


    
def getOneCategoria(id):
    valor = CategoriaM.getOneById(id)
    response = {
        "status": True,
        "data": valor
    }
    return response

def putCategoria(id, body):
    categoria = CategoriaM.getOneById(id)
    categoria = categoria[0]
    if categoria:
        idCategoria = body.get("idCategoria", None)
        nombreCategoria = body.get("nombreCategoria", "") 
        CategoriaM.setDataModel(idCategoria, nombreCategoria)
        valor = CategoriaM.Update(id)
        categoria = CategoriaM.getOneById(id)
        response = {
            "status": True,
            "Mensaje": "Categoria Actualizada correctamente",
            "data": categoria
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No existe la categoria"
        }
        return errorResponse

def postCategoria(body):
    idCategoria = body.get("idCategoria", None)
    nombreCategoria = body.get("nombreCategoria", "") 
    CategoriaM.setDataModel(idCategoria, nombreCategoria)
    valor = CategoriaM.Create()
    if(valor[0]):
        id = valor[0].get("id")
        categoria = CategoriaM.getOneById(id)
        print(categoria)
        response = {
            "status": True,
            "Mensaje": "Categoria Creada correctamente",
            "data": categoria
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No se pudo guardar la Categoria"
        }
        return errorResponse