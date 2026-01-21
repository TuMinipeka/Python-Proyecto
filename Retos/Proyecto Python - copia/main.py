from GestionDeHerramienta import menu_herramienta
from VecinoRegistro import menu_usuario

ADMIN_PASSWORD = "0000"
usuario_actual = {
    "tipo": None  # Administrador | Residente
}
def login():
    print("/// INICIO DE SESIÓN ///")
    print("1. Administrador")
    print("2. Residente")

    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            if verificar_admin():
                usuario_actual["tipo"] = "Administrador"
                print(" Sesión iniciada como Administrador")
            else:
                return False
        elif opcion == 2:
            usuario_actual["tipo"] = "Residente"
            print(" Sesión iniciada como Residente")
        else:
            print("Opción inválida")
            return False
        return True

    except ValueError:
        print("Debe ingresar un número.")
        return False

def verificar_admin():
    intentos = 3
    while intentos > 0:
        password = input("Ingrese la contraseña de administrador: ")
        if password == ADMIN_PASSWORD:
            return True
        intentos -= 1
        print(f"Contraseña incorrecta. Intentos restantes: {intentos}")
    print(" Acceso bloqueado.")
    return False


def menu_principal():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print(f"Rol actual: {usuario_actual['tipo']}")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Herramientas")
        print("3. Gestión de Préstamos")
        print("4. Consultas")
        print("5. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                    menu_usuario(usuario_actual)
            elif opcion == 2:
                menu_herramienta(usuario_actual)
            elif opcion == 3:
                print("Módulo préstamos (pendiente)")
            elif opcion == 4:
                print("Módulo consultas (pendiente)")
            elif opcion == 5:
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Debe ingresar un número.")
if login():
    menu_principal()