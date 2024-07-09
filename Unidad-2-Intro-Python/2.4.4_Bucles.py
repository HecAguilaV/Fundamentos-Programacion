print(" ")
print("-----Calculo de costo de envio-----")
print(" ")
print("Costo base de envio es de $5.000 CLP")
print("Costo por Kg adicional es de $500 CLP")
print(" ")
print("*Si distancia es de más de 100 Km se cobra un adicional de $100 CLP por Km*")
print(" ")

costoBase = 5000
kgAdic = 500
kmAdic = 100

# Solicitar nombre del cliente
while True:
    nomC = input("Ingrese su nombre: ")
    if len(nomC) > 30:
        print("Ingrese un nombre válido con menos de 30 caracteres.")
    elif len(nomC.strip()) == 0:
        print("El nombre no debe quedar vacío.")
    else:
        break

# Solicitar peso del paquete en Kg
while True:
    try:
        paque = float(input("Ingrese el peso del paquete en Kg (Ejemplo: 1.3): "))
        if paque <= 0:
            print("El peso del paquete debe ser mayor que cero.")
        else:
            break
    except ValueError:
        print("Ingrese un valor válido.")

# Solicitar distancia del envío en Km
while True:
    try:
        kiloMe = float(input("Ingrese la distancia del envío en Km (Ejemplo: 23): "))
        if kiloMe <= 0:
            print("La distancia debe ser mayor que cero.")
        else:
            break
    except ValueError:
        print("Ingrese un valor válido.")

# Calcular costos
costoKilo = paque * kgAdic
costoTotal = costoBase + costoKilo

# Aplicar cargo adicional por distancia si es mayor a 100 Km
if kiloMe > 100:
    exceKm = (kiloMe - 100) * kmAdic
    costoTotal += exceKm
else:
    exceKm = 0

# Mostrar resumen del costo de envío
print("\n**** Desgloce del costo de envío ****")
print(f"Nombre del cliente: {nomC}")
print(f"Peso del paquete: {paque} Kg")
print(f"Distancia del envío: {kiloMe} Km")
print(f"Costo base de envío: ${costoBase}")
print(f"Costo por kilo adicional: ${kgAdic}")
print(f"Cargo adicional por distancia (>100 Km): ${exceKm}")
print(f"El costo total del envío es: ${costoTotal}")