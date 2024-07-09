print("")
print("Bienvenido a Cesar's Pizza")
print("Menu:")
print("1.- PEPPERONI")
print("2.- QUESO")
print("3.- JAMÓN")
print("4.- 4N1")
print("5.- HULA HAWAIIAN")
print("6.- ULTIMATE SUPREME")
print("7.- VEGGIE")
print("8.- 3 MEAT TREAT")
print("9.- SUPER CHEESE 4N1")
print("10.- CHICKEN BBQ")
print("")

# Definir precios de las pizzas en una lista
precios = [6000, 7000, 8000, 10000, 9000, 11000, 12250, 13000, 14500, 6000]

opcion = input("Elija su pizza. Ingrese el número de la pizza deseada: ")
cantidad = int(input("¿Cuántas pizzas desea?: "))

# Verificar que la opción sea válida
opcion_num = int(opcion) - 1
if opcion_num >= 0 and opcion_num < len(precios):
    precio = precios[opcion_num]
    pizza_neto = precio * cantidad
    pizza_iva = pizza_neto * 0.19
    total = pizza_neto + pizza_iva

    print(f"Precio neto: {pizza_neto}")
    print(f"Precio iva: {pizza_iva}")
    print(f"Total: {total}")
else:
    print("Opción inválida. Por favor seleccione una pizza válida del menú.")
