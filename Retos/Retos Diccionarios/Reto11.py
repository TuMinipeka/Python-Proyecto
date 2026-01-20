# Fusión de inventario
# Update sirve para mezclar un diccionario dentro de otro
tienda_A = {'manzana': 10,'pera': 5}
tienda_B = {'pera': 8, 'uva': 12}

tienda_A.update(tienda_B) #Meter tienda B a tienda A

# El valor de Pera cambia por el valor mas reciente
print(tienda_A)