def validar_lista_numeros():
    while True:
        entrada = input("Ingrese una lista de números enteros separados por espacios: ")
        # Utilizamos split() sin argumentos para manejar múltiples espacios en blanco
        try:
            lista = [int(numero) for numero in entrada.split()]
            return lista
        except ValueError:
            print("Lista no válida, asegúrese de ingresar solo números enteros separados por espacios.")

# Función para validar y obtener la lista de números
lista_valida = validar_lista_numeros()

# Inicializamos listas para números pares e impares
pares = []
impares = []

# Separar números pares e impares
for numero in lista_valida:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Mostrar resultados
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")