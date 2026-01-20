#Diccionario Personal
name = str(input("Ingrese Su Nombre: "))
age = int(input("Ingrese Su Edad: "))
ciudad = str(input("Ingrese Su Ciudad: "))
actividad = str(input("Ingrese Su Hobby Favorito: "))

#Creacion de diccionario
mi_perfil = {
    "Nombre ": name.capitalize(), 
    "Edad ": age,
    "Ciudad ": ciudad.capitalize(),
    "Hobby ": actividad
}

#Mostrar Diccionario 
print(mi_perfil)

