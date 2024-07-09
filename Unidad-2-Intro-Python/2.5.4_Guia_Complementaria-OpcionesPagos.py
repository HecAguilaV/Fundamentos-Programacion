import random

opcion = 0
pago = 100000

while True:
    print("***************Menu*******************")
    print("1.- Pagar con tarjeta de crédito")
    print("2.- Pagar con PayPal")
    print("3.- Pagar por transferencia")
    print("4.- Cancelar")
    print("5.- Salir")

    try:
        opcion = int(input("Ingrese la opción deseada: "))
    except ValueError:
        opcion = 0

    if opcion == 1:
        numero = input("Ingrese número de tarjeta de crédito: ")
        nombre = input("Ingrese nombre titular: ")
        mes = input("Ingrese mes de vencimiento: ")
        anio = input("Ingrese año de vencimiento: ")

        print("Detalle compra")
        print(f"Costo de la compra: {pago}")
        print("Número de tarjeta: ", numero)
        print("Nombre del titular: ", nombre)
        print(f"Mes y año: {mes}/{anio}")
        break

    elif opcion == 2:
        usuario = input("Ingrese usuario: ")
        password = input("Ingrese contraseña: ")

        print("")
        print("Detalle compra")
        print(f"Costo de la compra: {pago}")        
        print("Usuario: ", usuario)
        print("Password: ********")
        break

    elif opcion == 3:
        numero_orden = random.randint(10000, 99999)

        print("Detalle compra")
        print("Código referencia: ", numero_orden)
        print(f"Costo de la compra: {pago}")        
        print("Nombre Destinatario: Dulce Capricho S.A.")
        print("Número de cuenta: 79.548.642-0")
        print("Banco: Banco Internacional")
        print("Correo: pago@capricho.com")
        break 

    elif opcion == 4:
        print("Pago cancelado")
    
    elif opcion == 5:
        print("Hasta pronto...")
        break
    
    else:
        print("Opción no válida")

print("Muchas gracias por su compra")