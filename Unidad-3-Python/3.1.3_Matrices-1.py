matriz_2d_arreglo = [
    [3, 10, 4, 16],
    [1, 7, 8, -7],
    [9, -1, 3, 9]
]

print("Matriz 3x4:")
for fila in matriz_2d_arreglo:
    for elemento in fila:
        print(f"\t{elemento}", end="")
    print()  # Salto de línea entre filas