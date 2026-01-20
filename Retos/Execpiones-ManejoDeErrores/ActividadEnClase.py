#Dividir Las clases de JSON TXT Y CSV
import csv
import json
import os
import time
import sys

def agregar_contactos():
    print("\n---AGREGAR NUEVO CONTACTO---")
    try:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input(f"Ingrese el telefono de {nombre}: ")
        email = input(f"Ingrese el email de {nombre}: ")

        if not nombre or not telefono:
            raise ValueError("Los campos nombre y telefono son obligatorios")
    except ValueError as ve:
        print(f"Error de valores: {ve}")
    except KeyboardInterrupt:
        print("Proceso finalizado por el usuario.")
    except Exception:
        print("Ocurrio un error inesperado.")

    linea_txt = f"{nombre},{telefono},{email}"
    lista_csv = [nombre,telefono,email]
    diccionario_obj = {
        "nombre":nombre,
        "telefono":telefono,
        "emaiil":email
    }

    #Guardar en TXT
    try:
        with open("contactos.txt","a", encoding="utf-8") as archivo_txt:
            archivo_txt.write(linea_txt)
        print("Contacto guardado exitosamente en TXT !!!")
    except PermissionError:
        print("No cuenta con los permisos necesarios para agregar contactos.")
    except Exception as e:
        print(f"Error inesperado en TXT: {e}")

    #Guardar CSV
    try:
        archivo_existe = os.path.exists("contactos.csv")
        with open("contactos.csv","a",newline="",encoding="utf-8") as archivo_csv:
            writer = csv.writer(archivo_csv)
            
            if not archivo_existe:
                writer.writerow(["Nombre","Telefono","Email"])

            writer.writerow(lista_csv)

        print("Contacto guardado exitosamente en CSV !!!")
    except PermissionError:
        print("No cuenta con los permisos necesarios para agregar contactos.")
    except Exception as e:
        print(f"Error inesperado en CSV: {e}")

    #Guardar en JSON
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
                        print("El archivo JSON es corrupto. Se crearÃ¡ uno nuevo.")
                        datos_actuales = []

        datos_actuales.append(diccionario_obj)

        with open("contactos.json","w",encoding="utf-8") as archivo_writer_json:
            json.dump(datos_actuales, archivo_writer_json, indent=4)
                    
            print("Contacto guardado exitosamente en JSON !!!")
    except PermissionError:
        print("No cuenta con los permisos necesarios para agregar contactos.")
    except Exception as e:
        print(f"Error inesperado en JSON: {e}")

def leer_contactos():
    print("\n---MOSTRANDO CONTACTOS---")

    #Leer TXT
    print("\n[FORMATO TXT]")
    try:
        with open("contactos.txt","r", encoding="utf-8") as archivo_txt:
            print(archivo_txt.read())
    except FileNotFoundError:
        print("El archivo TXT aun no existe.")
    except Exception as e:
        print(f"Error inesperado en lectura de TXT: {e}")

    #Leer CSV
    print("\n[FORMATO CSV]")
    try:
        with open("contactos.csv","r", encoding="utf-8") as archivo_csv:
            reader = csv.reader(archivo_csv)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("El archivo CSV aun no existe.")
    except Exception as e:
        print(f"Error inesperado en lectura de CSV: {e}")
    except csv.Error as e:
        print(f"Error al leer el archivo CSV: {e}")

    #Leer JSON
    print("\n[FORMATO JSON]")
    try:
        with open("contactos.json","r", encoding="utf-8") as archivo_json:
            datos = json.load(archivo_json)
            for contact in datos:
                print(contact)
    except FileNotFoundError:
        print("El archivo JSON aun no existe.")
    except Exception as e:
        print(f"Error inesperado en lectura de JSON: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON: {e}")

def menu():
    while True:
        print("\n===AGENDA DE CONTACTOS===")
        try:
            print("1. Agregar contactos")
            print("2. Ver contactos")
            print("3. Salir")

            opcion = int(input("Ingrese una opcion: "))

            if opcion == 1:
                agregar_contactos()
            elif opcion == 2:
                leer_contactos()
            elif opcion == 3:
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

menu()