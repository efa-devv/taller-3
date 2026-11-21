from flask import Flask, request, jsonify
import mysql.connector
import json

app = Flask(__name__)

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="soda"
    )
    return conexion


# SELECT
@app.route('/proveedores', methods=['GET'])
def ver_proveedores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM proveedores")
    datos = cursor.fetchall()
    lista = []
    for x in datos:
        p = {}
        p["id"] = x[0]
        p["nombre"] = x[1]
        p["telefono"] = x[2]
        p["correo"] = x[3]
        p["direccion"] = x[4]
        lista.append(p)
    conexion.close()
    return jsonify(lista)


@app.route('/proveedores/<id>', methods=['GET'])
def ver_uno(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM proveedores WHERE id = " + id)
    x = cursor.fetchone()
    print(x)
    if x == None:
        return jsonify({"mensaje": "no existe ese proveedor"})
    p = {}
    p["id"] = x[0]
    p["nombre"] = x[1]
    p["telefono"] = x[2]
    p["correo"] = x[3]
    p["direccion"] = x[4]
    conexion.close()
    return jsonify(p)


# INSERT
@app.route('/proveedores', methods=['POST'])
def insertar():
    datos = request.get_json()
    print(datos)
    nombre = datos["nombre"]
    telefono = datos["telefono"]
    correo = datos["correo"]
    direccion = datos["direccion"]
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO proveedores (nombre, telefono, correo, direccion) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, telefono, correo, direccion))
    conexion.commit()
    conexion.close()
    return jsonify({"mensaje": "proveedor agregado"})


# UPDATE
@app.route('/proveedores/<id>', methods=['PUT'])
def editar(id):
    datos = request.get_json()
    nombre = datos["nombre"]
    telefono = datos["telefono"]
    correo = datos["correo"]
    direccion = datos["direccion"]
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE proveedores SET nombre = %s, telefono = %s, correo = %s, direccion = %s WHERE id = %s"
    cursor.execute(sql, (nombre, telefono, correo, direccion, id))
    conexion.commit()
    #cursor.close()
    conexion.close()
    return jsonify({"mensaje": "proveedor editado"})


# DELETE
@app.route('/proveedores/<id>', methods=['DELETE'])
def eliminar(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM proveedores WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()
    return jsonify({"mensaje": "proveedor eliminado"})


if __name__ == '__main__':
    app.run(debug=True)
