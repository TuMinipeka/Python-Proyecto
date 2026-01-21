import json

def stock_bajo():
    with open("data/herramientas.json") as f:
        d = json.load(f)
    for i, h in d.items():
        if h["cantidad"] < 3:
            print(i, h["nombre"], h["cantidad"])
