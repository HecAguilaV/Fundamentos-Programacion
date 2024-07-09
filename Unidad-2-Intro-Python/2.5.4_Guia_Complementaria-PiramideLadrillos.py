ladrillos = int(input("Introduzca el número de ladrillos disponibles: "))
altura = 0
utilizados = 0
por_fila = 1

while utilizados < ladrillos:
    altura += 1
    por_fila += 1
    utilizados += por_fila

print("La altura máxima de la pirámide es de: ", altura)