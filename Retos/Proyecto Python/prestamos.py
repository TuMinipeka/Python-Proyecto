import json
import os
from datetime import datetime
from logger import log_evento

RUTA = "data/prestamos.json"
HERR = "data/herramientas.json"

def cargar(r):
    if not os.path.exists(r):
        return {}
    with open(r, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar(r, d):
    with open(r, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4, ensure_ascii=False)

def crear_prestamo():
    prestamos = cargar(RUTA)
    herramientas = cargar(HERR)

    idp = input("ID préstamo: ")
    idh = input("ID herramienta: ")

    if idh not in herramientas or herramientas[idh]["cantidad"] <= 0:
        print("No disponible")
        log_evento("Intento de préstamo sin stock")
        return

    prestamos[idp] = {
        "herramienta": idh,
        "usuario": input("ID usuario: "),
        "fecha_inicio": str(datetime.now()),
        "estado": "Activo"
    }

    herramientas[idh]["cantidad"] -= 1
    guardar(RUTA, prestamos)
    guardar(HERR, herramientas)
    log_evento(f"Préstamo creado {idp}")
