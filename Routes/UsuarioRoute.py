# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Model'))
import UsuarioModel as UsuarioModel
usuarioM = UsuarioModel.UsuarioModel()

def getAllUsers():
    valor = usuarioM.getAll()
    response = {
        "status": True,
        "data": valor
    }
    return response

    
def getOneUser(id):
    valor = usuarioM.getOneById(id)
    response = {
        "status": True,
        "data": valor
    }
    return response

def putUser(id, body):
    usuario = usuarioM.getOneById(id)
    usuario = usuario[0]
    if usuario:
        idUsuario = body.get("idUsuario", usuario.get("idUsuario"))
        nombreUsuario = body.get("nombreUsuario", usuario.get("nombreUsuario")) 
        apellidoUsuario = body.get("apellidoUsuario", usuario.get("apellidoUsuario")) 
        emailUsuario = body.get("emailUsuario", usuario.get("emailUsuario")) 
        passwordUsuario = body.get("passwordUsuario", usuario.get("passwordUsuario"))  
        idRol = body.get("idRol", usuario.get("idRol"))
        usuarioM.setDataModel(idUsuario, nombreUsuario, apellidoUsuario, emailUsuario, passwordUsuario, idRol)
        valor = usuarioM.Update(id)
        usuario = usuarioM.getOneById(id)
        response = {
            "status": True,
            "Mensaje": "Usuario Actualizado correctamente",
            "data": usuario
        }
        return response
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: No existe el usuario"
        }
        return errorResponse

def postUser(body):
    idUsuario = body.get("idUsuario", None)
    nombreUsuario = body.get("nombreUsuario", "") 
    apellidoUsuario = body.get("apellidoUsuario", "") 
    emailUsuario = body.get("emailUsuario", "") 
    passwordUsuario = body.get("passwordUsuario", "")  
    idRol = body.get("idRol", None)
    usuarioM.setDataModel(idUsuario, nombreUsuario, apellidoUsuario, emailUsuario, passwordUsuario, idRol)
    valor = usuarioM.Create()
    if(valor[0]):
        id = valor[0].get("id")
        usuario = usuarioM.getOneById(id)
        print(usuario)
        response = {
            "status": True,
            "Mensaje": "Usuario Creado correctamente",
            "data": usuario
        }
        return response
    else:

        errorResponse = {
            "status": False,
            "Mensaje": "Error: No se pudo guardar el usuario"
        }
        return errorResponse