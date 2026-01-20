# Gestion De Configuraciones
config = {}
resultado = config.setdefault("dificultad", "Normal")
# Busca la clave y si no existe asigna ese valor (Normal)
print(resultado)
print(config)