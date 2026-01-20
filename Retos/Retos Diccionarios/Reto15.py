# Backup y Modificacion
empleado = {
    "Nombre": "Daniel",
    "Edad": "17",
    "Ocupación": "Estudiante"
}
#Crea otro diccionario nuevo con los mismos datos pero separado del original
backup= empleado.copy()
#Vaciar Datos
empleado.clear()

print("Empleado:", empleado)
print("Backup:", backup)
