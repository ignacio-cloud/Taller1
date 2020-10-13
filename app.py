from flask import Flask, request, jsonify
import json

app = Flask(__name__)
#como personas esta esta global podemos crear varias en un metodo.
personas = []

#metodo inicio
@app.route('/',methods=['GET'])
def inicio():
    return "Bienvenido"

#metodo agregar persona. como es un POST se usa POSTMAN
@app.route('/agregar',methods=['POST'])
def agregarPersona():
    cuerpo = request.get_json()
    nombre = cuerpo['nombre']
    edad = cuerpo['edad']
    #crear persona
    persona = {'nombre':nombre,'edad':edad}
    #ingresamos al arreglo global.
    global personas
    #ingresamos la persona al arreglo.
    personas.append(persona)

    return jsonify({"mensaje": "agregado correctamente"})

#metodo obtener
@app.route('/obtener',methods=['GET'])
def obtenerPersonas():
    return jsonify(personas)

@app.route('/modificar',methods=['POST'])
def modificarPersona():
    cuerpo = request.get_json()
    nombre = cuerpo['nombre']
    new_nombre = cuerpo['new_nombre']
    new_edad = cuerpo['new_edad']
    global personas
    for i in range(len(personas)):
        if personas[i]['nombre'] == nombre:
            personas[i]['nombre'] = new_nombre
            personas[i]['edad'] = new_edad
    return jsonify({"mensaje":"Modificado correctamente"})

@app.route('/eliminar',methods=['POST'])
def eliminarPersona():
    cuerpo = request.get_json()
    nombre = cuerpo['nombre']
    global personas
    for i in range(len(personas)):
        if personas[i]['nombre'] == nombre:
            personas.pop(i)
    return jsonify({"mensaje":"Eliminado correctamente"})  
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=4000)