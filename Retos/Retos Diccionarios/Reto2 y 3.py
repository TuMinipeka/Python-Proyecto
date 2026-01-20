# Traductor Simple
# Acceso Seguro
print("-----BIENVENID@ A NUESTRO TRADUCTOR-----")
traductor = {
    "hola": "Hello",
    "adios": "Goodbye",
    "uno": "One",           #Diccionario
    "dos": "Two",
    "como": "How"
}


palabra = input("Ingrese Una palabra en ESPAÑOL: ").lower()

traduccion = traductor.get(palabra)
# .get es para q el codigo no se rompa
if traduccion:
    print( palabra,"En Ingles Es =",traduccion)
else:
    print("No Esta En El Diccionario")
