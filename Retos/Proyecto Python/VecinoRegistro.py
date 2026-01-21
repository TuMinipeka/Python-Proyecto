import json
import os
from logger import log_evento

RUTA = "data/usuarios.json"

def cargar():
    if not os.path.exists(RUTA):
        return {}
    with open(RUTA, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar(datos):
    with open(RUTA, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def crear_usuario():
    datos = cargar()
    idu = input("ID usuario: ")
    if idu in datos:
        print("ID ya registrado")
        return

    datos[idu] = {
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "telefono": input("Teléfono: "),
        "direccion": input("Dirección: "),
        "tipo": input("Tipo (Administrador/Residente): ")
    }

    guardar(datos)
    log_evento(f"Usuario creado: {idu}")
    print("Usuario registrado")

def listar_usuarios():
    datos = cargar()
    for i, u in datos.items():
        print(i, u)

def buscar_usuario():
    datos = cargar()
    idu = input("ID a buscar: ")
    print(datos.get(idu, "No existe"))

def eliminar_usuario():
    datos = cargar()
    idu = input("ID a eliminar: ")
    if idu in datos:
        del datos[idu]
        guardar(datos)
        log_evento(f"Usuario eliminado: {idu}")
        print("Eliminado")
