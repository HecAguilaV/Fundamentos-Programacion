print("Ingresar los datos de la venta")
cliente = input("Ingrese el nombre del cliente: ")
precio1 = int(input("Ingrese el precio del producto1: "))
cantidad1 = int(input("Ingrese la cantidad del producto1: "))

precio2 = int(input("Ingrese el precio del producto2: "))
cantidad2 = int(input("Ingrese la cantidad del producto2: "))

precio3 = int(input("Ingrese el precio del producto3: "))
cantidad3 = int(input("Ingrese la cantidad del producto3: "))

descuento = int(input("Ingrese el descuento (%): "))

total_bruto = (precio1 * cantidad1) + (precio2 * cantidad2) + (precio3 * cantidad3)
precio_con_descuento = round(total_bruto - (total_bruto * descuento / 100))
# Calcula el IVA sobre el precio con descuento
iva = round(precio_con_descuento * 0.19)  
total = precio_con_descuento + iva

print("")
print(f"Cliente:\t{cliente}")
print(f"Total bruto:\t${total_bruto}")
print(f"Total desc.:\t${precio_con_descuento}")
print(f"Iva:\t\t${iva}")
print(f"Total:\t\t${total}")