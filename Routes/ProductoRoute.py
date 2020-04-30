# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Model'))
import ProductoModel as ProductoModel
model = ProductoModel.ProductoModel()

def getAllProducto():
    valor = model.getAll()
    response = {
            "status": True,
            "data": valor
        }
    return response


    
def getOneProducto(id):
    valor = model.getOneById(id)
    response = {
        "status": True,
        "data": valor
    }
    return response

def putProducto(id, body):
    Producto = model.getOneById(id)
    Producto = Producto[0]
    if Producto:
        idProducto = body.get("idProducto", None)
        nombre = body.get("nombre", "") 
        stock = body.get("stock", 0) 
        idCategoria = body.get("idCategoria", None) 
        model.setDataModel(idProducto, nombre, stock, idCategoria)
        valor = model.Update(id)
        Producto = model.getOneById(id)
        response = {
            "status": True,
            "Mensaje": "Producto Actualizado correctamente",
            "data": Producto
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No existe la Producto"
        }
        return errorResponse

def postProducto(body):
    idProducto = body.get("idProducto", None)
    nombre = body.get("nombre", "") 
    stock = body.get("stock", 0) 
    idCategoria = body.get("idCategoria", None) 
    model.setDataModel(idProducto, nombre, stock, idCategoria)
    valor = model.Create()
    if(valor[0]):
        id = valor[0].get("id")
        Producto = model.getOneById(id)
        print(Producto)
        response = {
            "status": True,
            "Mensaje": "Producto Creado correctamente",
            "data": Producto
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No se pudo guardar el Producto"
        }
        return errorResponse