matriz_3d_conteo = [
    [["amarillo"], ["Verde"], ["Naranja"]],
    [["Blanco"], ["Naranja", "amarillo"], ["Blanco"]],
    [["Verde"], ["Naranja"], ["rojo"]]
]

colores = {"amarillo": 0, "rojo": 0, "Naranja": 0, "Verde": 0, "Blanco": 0}

for capa in matriz_3d_conteo:
    for fila in capa:
        for elemento in fila:
            colores[elemento] += 1

for color, cantidad in colores.items():
    print(f"Número de elementos '{color}': {cantidad}")