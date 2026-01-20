
texto =  str(input("Escribe la palabra:"))

opcion = int(input(
    "¿Como desea la palabra?\n"
    "1. MAYUSCULA\n"
    "2. minuscula\n"
    "3. En conjunto\n"
    "4. Primera en Mayus\n"
))

if opcion == 1:
    print(texto.upper())

elif opcion == 2:
    print(texto.lower())

elif opcion == 3:
    print(texto.split())

elif opcion == 4:
    print(texto.capitalize())