productos = {}
while True:
    print("\nMenú de supermercado:\n1. Agregar productos\n2. Ver canasta\n3. Ver total\n4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        productos[nombre_producto] = precio_producto
        print(f"{nombre_producto} agregado al catálogo.\n")

    elif opcion == "2":
        print("Productos del catálogo:")
        for producto, precio in productos.items():
            print(f"{producto}: ${precio:.2f}")

    elif opcion == "3":
        carrito = []
        while True:
            producto_seleccionado = input("Ingrese un producto, o escriba 'no' para terminar: ")
            if producto_seleccionado.lower() == "no":
                break
            if producto_seleccionado in productos:
                carrito.append(producto_seleccionado)
                print(f"{producto_seleccionado} agregado al carrito.\n")
            else:
                print("Producto no válido.")
        total = sum(productos.get(producto, 0) for producto in carrito)
        print(f"Total a pagar: ${total:.2f}\n")

    elif opcion == "4":
        print("¡Gracias por su compra!")
        break
    else:
        print("Opción no válida. Inténtelo nuevamente.")