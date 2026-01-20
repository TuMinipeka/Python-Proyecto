# Pila De Tareas
tareas = {"Tarea1": "Limpiar", "Tarea2": "Estudiar", "Tarea3": "Entrenar"}

#.popitem() extrae un elemento completo del diccionario (Devuelve clave y valor)
while tareas:
    clave, tarea = tareas.popitem() #Saca una tarea, la elimina, la guarda
    print("Ejecutando", clave, ":", tarea)
print ("No quedan tareas pendientes")