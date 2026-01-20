# Contador De Frecuencia
lista = ["pan", "leche", "pan", "huevos","leche","pan"]

producto = {} # Se crea el diccionario

for lista in lista: 
    if lista in producto:
        producto[lista] +=1 # Aumentar el contador
    else:
        producto[lista] = 1
print(producto)