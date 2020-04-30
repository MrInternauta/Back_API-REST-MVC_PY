# -*- coding: utf-8 -*-
import sys, os
from flask import request, jsonify, Flask
from UsuarioRoute import getAllUsers, getOneUser, putUser, postUser
from CategoriaRoute import getAllCategoria,  getOneCategoria, postCategoria, putCategoria
from RoleRoute import getAllRol,  getOneRol, postRol, putRol
from VentaRoute import getAllVenta,  getOneVenta, postVenta, putVenta
from ProductoRoute import getAllProducto,  getOneProducto, postProducto, putProducto
from VentaDetalleRoute import getAllVentaDetalle,  getOneVentaDetalle, postVentaDetalle, putVentaDetalle
from ExtrasRoute import getAllExtras,  getOneExtras, postExtras, putExtras
from ExtrasProductosRoute import getAllExtrasProductos,  getOneExtrasProductos, postExtrasProductos, putExtrasProductos

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

#--------------
# USUARIO GETONE/GETALL
@app.route('/Usuario', methods=['GET'])
def getUsuario():
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(getOneUser(id))
    else:
        return jsonify(getAllUsers())

# USUARIO PUT
@app.route('/Usuario', methods=['PUT'])
def putUsuario():
    body = request.json
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(putUser(id, body))
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: Parametro Id requerido"
        }
        return jsonify(errorResponse)


# USUARIO POST
@app.route('/Usuario', methods=['POST'])
def postUsuario():
    body = request.json
    return jsonify(postUser(body))

#---------------------
# CATEGORIA GETONE/GETALL
@app.route('/Categoria', methods=['GET'])
def getCategoria():
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(getOneCategoria(id))
    else:
        return jsonify(getAllCategoria())

# CATEGORIA PUT
@app.route('/Categoria', methods=['PUT'])
def putCategori_API():
    body = request.json
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(putCategoria(id, body))
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: Parametro Id requerido"
        }
        return jsonify(errorResponse)


# CATEGORIA POST
@app.route('/Categoria', methods=['POST'])
def postCategoria_API():
    body = request.json
    return jsonify(postCategoria(body))





#---------------------
# ROL GETONE/GETALL
@app.route('/Rol', methods=['GET'])
def getRol():
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(getOneRol(id))
    else:
        return jsonify(getAllRol())

# ROL PUT
@app.route('/Rol', methods=['PUT'])
def putRol_API():
    body = request.json
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(putRol(id, body))
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: Parametro Id requerido"
        }
        return jsonify(errorResponse)
        

# ROL POST
@app.route('/Rol', methods=['POST'])
def postRol_API():
    body = request.json
    return jsonify(postRol(body))


    #---------------------
# VENTA GETONE/GETALL
@app.route('/Venta', methods=['GET'])
def getVenta():
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(getOneVenta(id))
    else:
        return jsonify(getAllVenta())

# VENTA PUT
@app.route('/Venta', methods=['PUT'])
def putVenta_API():
    body = request.json
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(putVenta(id, body))
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: Parametro Id requerido"
        }
        return jsonify(errorResponse)
        

# VENTA POST
@app.route('/Venta', methods=['POST'])
def postVenta_API():
    body = request.json
    return jsonify(postVenta(body))


    #---------------------
# PRODUCTO GETONE/GETALL
@app.route('/Producto', methods=['GET'])
def getProducto():
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(getOneProducto(id))
    else:
        return jsonify(getAllProducto())

# PRODUCTO PUT
@app.route('/Producto', methods=['PUT'])
def putProducto_API():
    body = request.json
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(putProducto(id, body))
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: Parametro Id requerido"
        }
        return jsonify(errorResponse)
        
# PRODUCTO POST
@app.route('/Producto', methods=['POST'])
def postProducto_API():
    body = request.json
    return jsonify(postProducto(body))



    #---------------------
# VentaDetalle GETONE/GETALL
@app.route('/VentaDetalle', methods=['GET'])
def getVentaDetalle():
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(getOneVentaDetalle(id))
    else:
        return jsonify(getAllVentaDetalle())

# VentaDetalle PUT
@app.route('/VentaDetalle', methods=['PUT'])
def putVentaDetalle_API():
    body = request.json
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(putVentaDetalle(id, body))
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: Parametro Id requerido"
        }
        return jsonify(errorResponse)
        
# VentaDetalle POST
@app.route('/VentaDetalle', methods=['POST'])
def postVentaDetalle_API():
    body = request.json
    return jsonify(postVentaDetalle(body))

    #---------------------
# Extras GETONE/GETALL
@app.route('/Extras', methods=['GET'])
def getExtras():
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(getOneExtras(id))
    else:
        return jsonify(getAllExtras())

# Extras PUT
@app.route('/Extras', methods=['PUT'])
def putExtras_API():
    body = request.json
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(putExtras(id, body))
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: Parametro Id requerido"
        }
        return jsonify(errorResponse)
        
# Extras POST
@app.route('/Extras', methods=['POST'])
def postExtras_API():
    body = request.json
    return jsonify(postExtras(body))



    #---------------------
# ExtrasProductos GETONE/GETALL
@app.route('/ExtrasProductos', methods=['GET'])
def getExtrasProductos():
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(getOneExtrasProductos(id))
    else:
        return jsonify(getAllExtrasProductos())

# ExtrasProductos PUT
@app.route('/ExtrasProductos', methods=['PUT'])
def putExtrasProductos_API():
    body = request.json
    query_parameters = request.args
    id = query_parameters.get('id')
    if id:
        return jsonify(putExtrasProductos(id, body))
    else:
        errorResponse = {
            "status": False,
            "Mensaje": "Error: Parametro Id requerido"
        }
        return jsonify(errorResponse)
        
# ExtrasProductos POST
@app.route('/ExtrasProductos', methods=['POST'])
def postExtrasProductosAPI():
    body = request.json
    return jsonify(postExtrasProductos(body))



