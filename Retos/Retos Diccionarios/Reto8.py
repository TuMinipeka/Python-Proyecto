# Filtro De Aprobados 
notas = {
    "Ana": 8,
    "Luis": 4,
    "Maria": 9,
    "Pedro": 5
}

aprobados = {}
# Usamos .items para ver a cada esrudiante con su nota
for nombre, nota in notas.items():
    if nota >= 6:
        aprobados [nombre] = nota
    
print (aprobados)