def promedio_notas(notas):
    if not notas:
        return 0.0
    return sum(notas)/len(notas)

def cargar_datos(nombre_archivo):
    estudiantes=[]
    ids_registrado = set()

    try:
        with open(nombre_archivo, "r") as f:
            for linea in f:
                #ID,nombre,nota1,nota2....
                parte=linea.strip().split(",")

                if len(parte) >= 2:
                    id_est= parte[0]
                    nombre=parte[1]
                    notas=[float(n) for n in parte [2:]]

                    estudiante= {
                        "id":id_est,
                            "nombre":nombre,
                            "notas":notas
                            }
                    estudiantes.append(estudiante)
                    ids_registrado.add(id_est)
    except FileNotFoundError:
        print("Archivo no encontrado. Se creara uno nuevo al guardar")
    except ValueError:
        print("Error de formato en el archivo")
    except Exception as e:
        print("Ocurrio un error inesperado ",e)
    return estudiantes, ids_registrado

def guardar_datos(nombre_archivo, estudiantes):
    try:
        with open(nombre_archivo,"w") as f:
            for est in estudiantes:
                notas_str=",".join([str(n)for n in est["notas"]])
                f.write(f"{est["id"]},{est["nombre"], {notas_str}}\n")
                print("Datos Guardados Exitosamente")
    except Exception as e:
        print(f"ocurrio un error al guardar: {e}")


