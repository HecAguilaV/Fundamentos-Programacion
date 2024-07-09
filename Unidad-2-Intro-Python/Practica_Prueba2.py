import datetime

print(" ")
print("-----Calculo de costo de envio-----")
print(" ")
print("Costo base de envio es de $5.000 CLP")
print("Costo por Kg adicional es de $500 CLP")
print(" ")
print("*Si distancia es de más de 100 Km se cobra un adicional de $100 CLP*")
print(" ")

costoBase = 5000
kgAdic = 500
kmAdic = 100

while True:
    nomCliente = input("Ingrese su nombre: ")
    if len(nomCliente) > 30:
        print("Introduzca un nombre válido con menos de 30 caracteres")
    elif len(nomCliente) == 0:
        print("El nombre no debe quedar vacío")
    else:
        break

while True:
    try:
        paque = float(input("Ingrese el peso del paquete en Kg (Ejemplo: 1.3): "))
        break
    except ValueError:
        print("Ingrese un valor válido")   

while True:
    try:
        kiloMe = float(input("Ingrese la distancia del envío en Km (Ejemplo: 23): "))
        break
    except ValueError:
        print("Ingrese un valor válido") 

costoKilo = paque * kgAdic
costoTotal = costoBase + costoKilo

if kiloMe > 100:
    exceKm = (kiloMe - 100) * kmAdic
    costoTotal += exceKm
else:
    exceKm = 0

total = costoTotal

print("\n")
print("**** Desgloce del costo de envío ****")
print(f"Nombre del cliente: {nomCliente} ")
print(f"Peso del paquete: {paque} Kg")
print(f"Distancia a la que se enviará el paquete: {kiloMe} Km")
print(f"Costo base de envío: ${costoBase} ")
print(f"Costo por Kg de peso: ${kgAdic}")
print(f"Costo de envío por el excedente de kilómetros: ${exceKm}")
print(f"El costo total del envío es: ${total}")

fechaHora = datetime.datetime.now()

# Limpiar el nombre del cliente para el archivo (reemplazar espacios por guiones bajos)
nombre_archivo = f'Envio_{nomCliente.replace(" ", "_")}.txt'

with open(nombre_archivo, 'w') as archivo:
    archivo.write("\n-----Resumen de envío-----\n")
    archivo.write(f"\nFecha y hora actual: {fechaHora}\n")
    archivo.write(f"Nombre del cliente: {nomCliente}\n")
    archivo.write(f"Peso del paquete: {paque} Kg\n")
    archivo.write(f"Distancia a la que se enviará el paquete: {kiloMe} Km\n")
    archivo.write(f"Costo base de envío: ${costoBase}\n")
    archivo.write(f"Costo por Kg de peso: ${kgAdic}\n")
    archivo.write(f"Costo de envío por el excedente de kilómetros: ${exceKm}\n")
    archivo.write(f"El costo total del envío es: ${total}\n")

print("Se ha creado un archivo con el resumen de envío del paquete.")
