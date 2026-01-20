def opcion(minv: int, maxv: int, defaultv:int = -1):
   
    while True:
        try:
         resultado = int(input(f"Ingrese un valor entre: {minv} y {maxv}: "))
         if resultado == defaultv and defaultv !=-1:
                return resultado 
         if resultado < minv or resultado > maxv: 

             print(f"Debe ingresar un valor valido para el rango {minv} y {maxv}")
         else:
            return resultado
        except ValueError:
            print("Solo Numeros")

def limpiar ():    
    input("Enter para continuar..")
    print("\n" * 20)

def calcularPromedio(n1: int, n2: int, n3: int):
    return (n1+n2+n3)/3

def registrarNota(materia: str, min: int, max: int):
    print(f"\tNotas Para: {materia}")
    return opcion(min, max)

nota1 = 0
nota2 = 0
nota3 = 0


while True:
    print  ("---MENU---")
    print("\t1. Registrar Notas: ")
    print("\t2. Calcular promedio: ") 
    print("\t0. salir")
    opcionSeleccionada = opcion(1, 2, 0 )
    print(f"opcion: {opcionSeleccionada}")

    if opcionSeleccionada == 0:
        print  ("Muchas gracias BYE")
        break
    elif opcionSeleccionada == 1:
        nota1 = registrarNota("Ciencias", 1, 100 )
        nota2 = registrarNota("Programacion", 1, 100 )
        nota3 = registrarNota("Ser", 1, 100 )
    elif opcionSeleccionada == 2:
        print(f"el promedio del estudiante es de: {calcularPromedio(nota1,nota2,nota3)}")
    