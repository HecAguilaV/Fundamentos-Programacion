#Menú de opciones para pago de cupo de la tarjeta de crédito.

saldo_tarjeta = 100000

while True:
    print("\nMenú de opciones:")
    print("1. Pago de Tarjeta de Crédito")
    print("2. Simulación de Compras")
    print("3. Salir")
    op = input("Seleccione una opción (1, 2, 3): ")

    if op == "1":
        try:
            pago = float(input("Ingrese el monto a pagar: "))
            if pago >= 0 and pago <= saldo_tarjeta:
                saldo_tarjeta -= pago
                print(f"Pago realizado. Su saldo actual es de ${saldo_tarjeta:.2f}")
            else:
                print("Error: El monto ingresado no es válido.")
        except ValueError:
            print("Error: Debes ingresar un valor válido.")

    elif op == "2":
        try:
            while True:
                compra = float(input("Ingrese el monto de la compra (ingrese 0 para terminar): "))
                if compra == 0:
                    break
                elif compra > 0 and compra <= saldo_tarjeta:
                    saldo_tarjeta -= compra
                    print(f"Compra realizada. Su saldo actual es de ${saldo_tarjeta:.2f}")
                else:
                    print("Error: El monto de la compra no es válido.")
        except ValueError:
            print("Error: Ingrese un valor válido.")

    elif op == "3":
        print("Gracias por su apreciado tiempo.")
        break

    else:
        print("Error: Opción no válida. Seleccione una opción del 1 al 3.")