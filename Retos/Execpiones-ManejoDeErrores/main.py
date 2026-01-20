import Logica

CORTES = ("Corte 1","Corte 2","Corte 3")

def main():
    archivo = "notas.txt"

    estudiantes, ids = Logica.cargar_datos(archivo)

    while True:
        print("\n---GESTION DE NOTAS---")
        print("1. Agregar estudiante")
        print("2. Ver Reporte")
        print("3. Guadar y salir")

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            id_est = input("ID del estudiante: ")
            nombre = input("Nombre del estudiante: ")

            if id_est in ids:
                print(f"El id {id_est} del estudiante {nombre} ya se encuentra registrado")
                continue

            notas_temp = []

            for corte in CORTES:
                while True:
                    try:
                        nota = float(input(f"Ingrese la nota para el {corte}: "))

                        if 0.0 <= nota <= 100.0:
                            notas_temp.append(nota)
                            break
                        else:
                            print("La nota debe estar entre 0 y 100")
                    except ValueError:
                        print("Entrada invalida, Solo se reciben valores numericos.")
                    except Exception as e:
                        print(f"Ocurrio un error inesperado: {e}")
            
            nuevo_est = {
                "id":id_est,
                "nombre":nombre,
                "notas":notas_temp
            }

            estudiantes.append(nuevo_est)
            ids.add(id_est)

            print("Estudiante Registrado")
        
        elif opcion == 2:

            estudiantes.sort(key=lambda x:Logica.promedio_notas(x["notas"]), reverse=True)
             
            print(f"\n{'ID':<10} {'NOMBRE':<15} {'PROMEDIO':<10}")
            print("-"*35)

            for est in estudiantes:
                prom = Logica.promedio_notas(est["notas"])
                print(f"{est['id']:<10} {est['nombre']:<15} {prom: .2f}")
            
        elif opcion == 3:
            Logica.guardar_datos(archivo,estudiantes)
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")
            
        
if __name__ == "__main__":
    main()
