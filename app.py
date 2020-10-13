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

if __name__ == '__main__':
    app.run(debug=True,port=4000)