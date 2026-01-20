# Suma De Valores
gastos = {
    "Luz": 1500,
    "Agua": 500,
    "Internet": 1200
}
total = 0
for gastos in gastos.values():
    total += gastos #Sumar lo que ya tengo guardado
print("Total De Gastos Mensuales:", total,"$")