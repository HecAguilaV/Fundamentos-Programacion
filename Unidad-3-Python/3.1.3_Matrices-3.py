filas = 10
columnas = 4
bus = [[0] * columnas for _ in range(filas)]

# Asignar números de asiento automáticamente
numero_asiento = 1
for fila in range(filas):
    for columna in range(columnas):
        bus[fila][columna] = numero_asiento
        numero_asiento += 1

print("Asientos del bus:")
for fila in bus:
    print(*fila, sep="\t")