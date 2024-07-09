# ValorNetoDeUnProducto

# Solicitar información al usuario
producto = input("Ingrese el nombre del producto: ")
valorProducto = float(input("Ingrese el valor del producto: "))  # Convertir a float para manejar decimales
valorNeto = 0.81  # Descuento del 19% (0.81 es el factor multiplicativo para calcular el valor sin IVA)

# Calcular el valor del producto sin IVA
valorSinIva = valorProducto * valorNeto

# Mostrar detalle del producto
print("----- Detalle producto ----")
print(f"NOMBRE PRODUCTO: {producto}")
print(f"VALOR PRODUCTO: {valorProducto}")
print(f"VALOR PRODUCTO SIN IVA: {valorSinIva}")  # Mostrar el valor sin IVA sin redondear
print(f"VALOR PRODUCTO SIN IVA (redondeado): {round(valorSinIva, 2)}")  # Mostrar el valor sin IVA redondeado a 2 decimales
