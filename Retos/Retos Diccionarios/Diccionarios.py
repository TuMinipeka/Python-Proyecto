def sistema_caja():
    inventario = {
        "salas": 0,
        "cadenas" : 12000,
        "anillos": 8000,
        "luces": 25000,
    }

    
    print("Productos in Stock: ", list(inventario.keys()))

    producto = input("Ingrese el producto que desea llevar: ").lower()
    if producto in inventario:
        cantidad = int(input("¿cuantas unidades necesita?: "))
        if cantidad > 0:
            precio_unitario = inventario[producto]
            total_pagar = cantidad * precio_unitario

            print("-----Resumen de compra-----")
            print(f"Producto: {producto.capitalize()}")
            print(f"Precio Unitario: {precio_unitario}")
            print(f"cantidad : {cantidad}")
            print(f"Total a pagar: {total_pagar}")
            
        else:
            print("Tiene q ser mayor a 0")
    else:
        print("No hay ")
    

def menu():
    print ("--------BIENVENID@ A PROXIS----------")
    
    print ("1. Comprar ")
    print ("2. Salir")

    opcion = int(input("Ingrese una opcion"))
   
    if opcion == 1:
        sistema_caja()
    elif opcion ==2:
        print ("Saliendo Del Programa")
        pass
    else:
        print("Opcion invalida")

menu()