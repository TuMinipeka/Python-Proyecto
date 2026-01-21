from auth import login
import VecinoRegistro as VecinoRegistro
import GestionDeHerramienta as GestionDeHerramienta
import prestamos as prestamos
import consultas as consultas
 
usuario = login()
if not usuario:
    exit()

while True:
    print("\n=== MENÚ ===")
    print("1 Usuarios")
    print("2 Herramientas")
    print("3 Préstamos")
    print("4 Consultas")
    print("5 Salir")

    op = input("> ")

    if op == "1" and usuario["tipo"] == "Administrador":
        VecinoRegistro.crear_usuario()
    elif op == "2":
        GestionDeHerramienta.listar()
    elif op == "3" and usuario["tipo"] == "Administrador":
        prestamos.crear_prestamo()
    elif op == "4":
        consultas.stock_bajo()
    elif op == "5":
        break
