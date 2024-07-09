nombre1 = input("Nombre 1:")
apellido1 = input("Apellido 1:")
nombre2 = input("Nombre 2:")
apellido2 = input("Apellido 2:")
nombre3 = input("Nombre 3:")
apellido3 = input("Apellido 3:")

lista1 = [nombre1, nombre2, nombre3]
lista2 = [apellido1, apellido2, apellido3]

print("\nNombres:")
for nombre in lista1:
    print(f"- {nombre}")
print("\nApellidos:")
for apellido in lista2:
    print(f"- {apellido}")