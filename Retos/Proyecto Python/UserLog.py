import sys
import json
import os
import time
def gestion_usuarios ():
    print("\n<<<<<<-SISTEMA COMUNITARIO->>>>>>")
    print("        Bienvenido Vecino")
    try:

        name  = input("Ingrese Su Nombre Vecino: ").capitalize()
        id_veci = input(f"Ingrese Su ID {name} : ")
        apellido = input(f"Ingrese su apellido {name } : ").capitalize()
        telefono = input(f"Ingrese Su Numero de Telefono {name} {apellido} : ")
        direccion = input(f"Ingrese Su Direccion {name} : ")
        print("Que Tipo De Usuario Es Usted")
        print ("1. Administrador")
        print ("2. Residente")
        
        tipo_usuario = int(input("Ingresa Una Opcion: "))
        

        if not name or not telefono or not apellido or not direccion or not id_veci or not tipo_usuario:
            raise ValueError("Te falto llenar Datos")
    except KeyboardInterrupt:
            print("Proceso finalizado por el usuario.")
    except Exception:
            print("Ocurrio un error inesperado.") 
            
    diccionario = {
        "nombre": name,
        "id": id_veci,
        "apellido": apellido,
        "telefono": telefono,
        "direccion": direccion,
        "Tipo De Usuario": tipo_usuario
    }


    # Guardar en JSON
    try:
            datos_actuales = []
            archivo_existe = os.path.exists("contactos.json")

            if archivo_existe:
                with open("contactos.json","r",encoding="utf-8") as archivo_json:
                    contenido = archivo_json.read()

                    if contenido:
                        try:
                            datos_actuales = json.load(contenido)
                        except json.JSONDecodeError:
                            print("El archivo JSON es corrupto. Se creara uno nuevo.")
                            datos_actuales = []

            datos_actuales.append(diccionario)

            with open("contactos.json","w",encoding="utf-8") as archivo_writer_json:
                json.dump(datos_actuales, archivo_writer_json, indent=4)
                        
                print("Contacto guardado exitosamente en JSON !!!")
    except PermissionError:
            print("No cuenta con los permisos necesarios para agregar contactos.")
    except Exception as e:
            print(f"Error inesperado en JSON: {e}")

   # Leer en JSON
def leer_json ():
    print("\n[Guardado]")
    try:
        with open("contactos.json","r", encoding="utf-8") as archivo_json:
            datos = json.load(archivo_json)
            for contact in datos:
                print(f"Nombre: {contact["nombre"]}")
                print(f"Id: {contact["id"]}")
                print(f"Apellido: {contact["apellido"]}")
                print(f"Telefono: {contact["telefono"]}")
                print(f"Dirección: {contact["direccion"]}")
                print(f"Tipo De Usuario: {contact["tipo_usuario"]}")
    except FileNotFoundError:
        print("El archivo JSON aun no existe.")
    except Exception as e:
        print(f"Error inesperado en lectura de JSON: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON: {e}")

def menu():
    while True:
        print("\n=====MENU PRINCIPAL=====")
        try:
            print("1. Registrar Vecino")
            print("2. Registrados")
            print("3. Proximamente")
            print("4. Proximamente")
            print("5. Salir")

            opcion= int(input("Ingrese Una Opcion: "))
            if opcion == 1:
                gestion_usuarios()
            elif opcion == 2:
                leer_json()
                time.sleep(2)
            elif opcion == 3:
                print("Proximamente")
                time.sleep(2)
            elif opcion == 4:
                print("Proximamente")
                time.sleep(2)
            elif opcion == 5:
                print("Saliendo del programa...")
                time.sleep(2)
                break
            else:
                    print("Opcion no valida. Intente nuevamente")
        except ValueError:
            print("La opcion debe ser un valor numerico.")
            continue
        except KeyboardInterrupt:
            print("\nSaliendo forzosamente...")
            time.sleep(2)
            sys.exit() #Cierre del programa limpiamente
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")
            break
menu()