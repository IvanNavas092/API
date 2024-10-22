# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:12:00 2024

@author: navas
"""

"""Creacion de APIs ahora si"""
from flask import Flask, jsonify

app = Flask(__name__)

# Lista 1
@app.route("/api/lista1", methods = ["GET"])

def obtener_lista1():
    datos = {
        "nombre": "Sebastian",
        "edad": 19,
        "Residencia": "Seseña"}
    return jsonify(datos)

# Lista 2
@app.route("/api/lista2", methods = ["GET"])

def obtener_lista2():
    lista_datos = [
        {"nombre": "Sebastian", "edad": 19, "Residencia": "Seseña"},
        {"nombre": "Javier", "edad": 12, "Residencia": "Valdemoro"},
        {"nombre": "Tymur", "edad": 9, "Residencia": "Ecuador"}]
    return jsonify(lista_datos) #Te convierte en Json

if __name__ == "__main__":
    app.run(debug = True)