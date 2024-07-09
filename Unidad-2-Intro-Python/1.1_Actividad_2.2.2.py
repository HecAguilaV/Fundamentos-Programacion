#Primera Etapa
print("Bienvenidos al mundo de la programación")
nombre = input("Para comenzar, ingresa tu nombre: ")

# Segunda Etapa: Bienvenida al usuario
nom = nombre
print("Bienvenido", nom)

# Tercera Etapa: Resolver la ecuación X^2 + 3X + 1 / 4
valorX = input("Por favor, ingresa el valor de X para resolver la siguiente ecuación (X^2 + 3X + 1) / 4: ")

# Convertir el valor de entrada a entero
valX = int(valorX)

# Calcular el resultado de la ecuación
resultX = ((valX ** 2) + (3 * valX + 1)) / 4

# Mostrar el resultado
print("El resultado es: ", resultX)
