import datetime

print(" ")
print("-----Cantidad de ventas diarias-----")
print(" ")

while True:
    try:
        panCiab = int(input("Ingrese cantidad de Pan Ciabatta: "))
        pieLim = int(input("Ingrese cantidad de Pie de Limon: "))
        cafe = int(input("Ingrese cantidad de café: "))
        te = int(input("Ingrese cantidad de té: "))
        alfajor = int(input("Ingrese cantidad de alfajor: "))

        panCiabcosto = panCiab * 2000
        pieLimcosto = pieLim * 3500
        cafecosto = cafe * 2200
        tecosto = te * 1600
        alfajorcosto = alfajor * 1000

        total = panCiabcosto + pieLimcosto + cafecosto + tecosto + alfajorcosto
        break

    except ValueError:
        print("Por favor, ingrese un número válido.")

print(" ")
print("-----Resumen de ventas-----")
print(" ")
print(f"Total Pan Ciabatta (Vendidos {panCiab}): ${panCiabcosto}")
print(f"Total Pie de Limón (Vendidos {pieLim}): ${pieLimcosto}")
print(f"Total Café (Vendidos {cafe}): ${cafecosto}")
print(f"Total Té (Vendidos {te}): ${tecosto}")
print(f"Total Alfajores (Vendidos {alfajor}): ${alfajorcosto}")
print(f"Total ventas: ${total}\n")

if total >= 50000:
    print(f"¡Buena venta hoy! Total: ${total}")
    print(" ")
else:
    print(f"Sus ventas fueron bajas hoy. Total: ${total}")
    print(" ")

fechaHora = datetime.datetime.now()

with open('Informe_ventas.txt', 'w') as archivo:
    archivo.write("\n-----Resumen de ventas-----\n")
    archivo.write(f"Fecha y hora actual: {fechaHora}\n")
    archivo.write(f"Total Pan Ciabatta (Vendidos {panCiab}): ${panCiabcosto}\n")
    archivo.write(f"Total Pie de Limón (Vendidos {pieLim}): ${pieLimcosto}\n")
    archivo.write(f"Total Café (Vendidos {cafe}): ${cafecosto}\n")
    archivo.write(f"Total Té (Vendidos {te}): ${tecosto}\n")
    archivo.write(f"Total Alfajores (Vendidos {alfajor}): ${alfajorcosto}\n")
    archivo.write(f"Total ventas: ${total}\n")

print("Se ha creado un archivo con el resumen total del día.")