# Diccionario Desde Lista
name = ["Ana", "Juan", "Daniel"]
ages = ["25", "30", "17"]
print(len(name))
print(len(ages))

diccionario = {}

for x in range (len(name)): # Cuantos nombres hay
    diccionario[name[x]] = ages[x]

print(diccionario)

