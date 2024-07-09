print("Calculadora")
print("1. Suma\n2. Resta\n3. Multiplica\n4. Divide\n5. Salir")
op = input("Escoge el numero de la operacion deseada: ")

def validar_numero(entrada):
    try:
        return float(entrada)
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return None

# Función para la suma
def sumar(num1, num2):
    suma = num1 + num2
    print(f"La suma es: {suma}")

# Función para la resta
def resta(num1, num2):
    resta = num1 - num2
    print(f"La resta es: {resta}")

# Función para la multiplicación
def multi(num1, num2):
    multi = num1 * num2
    print(f"La multiplicacion es: {multi}")

# Función para la división
def div(num1, num2):
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        division = num1 / num2
        print(f"La division es: {division}")

# Convertir la opción a entero
op = validar_numero(op)
if op is not None and 1 <= op <= 4:
    num1 = input("Primer número: ")
    num1 = validar_numero(num1)
    num2 = input("Segundo número: ")
    num2 = validar_numero(num2)

    if num1 is not None and num2 is not None:
        if op == 1:
            sumar(num1, num2)
        elif op == 2:
            resta(num1, num2)
        elif op == 3:
            multi(num1, num2)
        elif op == 4:
            div(num1, num2)
else:
    print("Opción inválida o fuera de rango. Saliendo de la calculadora.")