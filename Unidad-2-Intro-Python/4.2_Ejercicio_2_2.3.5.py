print("Ingrese los siguientes datos para realizar su compra. \nTodos los datos son obligatorios.")
while True:
    nom = input("Ingrese su nombre: ")
    telef = input("Ingrese su número de teléfono o celular: ")
    print("Ingrese producto y cantidad")
    product = input("Nombre del producto: ")
    cantidad = input("Cantidad: ")

    confirmacion = input("¿Está seguro que desea pagar? ('s' o 'n'): ").lower()
    
    if nom == "" or telef == "" or product == "" or cantidad == "" or confirmacion != 's':
        print("Faltan datos por ingresar o no confirmó la compra. Por favor, chequee la información ingresada.")
        print(f"Nombre: {nom}")
        print(f"Teléfono: {telef}")
        print(f"Producto: {product}")
        print(f"Cantidad: {cantidad}")
        print("")
# Permite al usuario ingresar los datos nuevamente si falta algo o no confirma la compra
        continue  
    else:
        print("")
        print("La compra se ha realizado con éxito. ¡Muchas gracias por su compra!")
        print("")
# Sale del bucle una vez que la compra se ha realizado correctamente
        break