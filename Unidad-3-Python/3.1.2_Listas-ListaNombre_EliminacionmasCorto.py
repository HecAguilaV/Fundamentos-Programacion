lista_nombres = []
while True:
    nombre = input("Ingrese un nombre (o 'no' para terminar): ")
    if nombre.lower() == "no":
        break
    lista_nombres.append(nombre)

if lista_nombres:
    nombre_mas_corto = min(lista_nombres, key=len)
    lista_nombres.remove(nombre_mas_corto)
    print(f"Nombre más corto eliminado es: {nombre_mas_corto}")
else:
    print("No se ingresaron nombres.")
