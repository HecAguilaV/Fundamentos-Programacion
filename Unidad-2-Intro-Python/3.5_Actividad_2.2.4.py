# Solicitar datos de entrada
nom = input("Ingrese nombre empleado: ")
rut = input("Ingrese rut empleado: ")
horasTrabajadas = int(input("Ingrese las horas trabajadas: "))
valorHora = int(input("Ingrese el valor hora del empleado: "))

# Definir valores fijos
colacion = 5500
movilizacion = 3000

# Calcular el total a pagar
total_horas = valorHora * horasTrabajadas
resultado = total_horas + colacion + movilizacion

# Mostrar resultados
print("-----LIQUIDACIÓN EMPLEADO----")
print(f"NOMBRE EMPLEADO: {nom}")
print(f"RUT EMPLEADO: {rut}")
print(f"MOVILIZACIÓN: {movilizacion}")
print(f"ALIMENTACIÓN: {colacion}")
print(f"PAGO A EMPLEADO: {resultado}")