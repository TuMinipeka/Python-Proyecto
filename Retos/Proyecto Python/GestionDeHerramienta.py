import json
import os
from logger import log_evento

RUTA = "data/herramientas.json"

def cargar():
    if not os.path.exists(RUTA):
        return {}
    with open(RUTA, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar(d):
    with open(RUTA, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4, ensure_ascii=False)

def crear():
    d = cargar()
    idh = input("ID herramienta: ")
    if idh in d:
        print("Ya existe")
        return
    d[idh] = {
        "nombre": input("Nombre: "),
        "categoria": input("Categoría: "),
        "cantidad": int(input("Cantidad: ")),
        "estado": "Activa",
        "valor": float(input("Valor: "))
    }
    guardar(d)
    log_evento(f"Herramienta creada {idh}")

def listar():
    for i, h in cargar().items():
        print(i, h)
