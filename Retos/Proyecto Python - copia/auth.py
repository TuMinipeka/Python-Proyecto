ADMIN_PASSWORD = "0000"

def login():
    print("\n=== INICIO DE SESIÓN ===")
    print("1. Administrador")
    print("2. Residente")

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            if verificar_admin():
                return {"tipo": "Administrador"}
            else:
                return None
        elif opcion == 2:
            return {"tipo": "Residente"}
        else:
            print("Opción inválida")
            return None
    except ValueError:
        print("Debe ingresar un número.")
        return None

def verificar_admin():
    intentos = 3
    while intentos > 0:
        password = input("Contraseña administrador: ")
        if password == ADMIN_PASSWORD:
            print("Acceso concedido")
            return True
        intentos -= 1
        print(f"Intentos restantes: {intentos}")
    print("Acceso bloqueado")
    return False
