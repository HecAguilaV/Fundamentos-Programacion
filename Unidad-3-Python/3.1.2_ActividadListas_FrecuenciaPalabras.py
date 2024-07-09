nombre1 = input("Nombre 1:")
nombre2 = input("Nombre 2:")
nombre3 = input("Nombre 3:")
lista = [nombre1, nombre2, nombre3]

if len(nombre1) > len(nombre2):
    lista = [nombre1]
if len(nombre2) > len(nombre3):
    lista = [nombre2]
if len(nombre3) > len(nombre1):
    lista = [nombre3]
print(f"El nombre con mayor caractéres es: {lista}")