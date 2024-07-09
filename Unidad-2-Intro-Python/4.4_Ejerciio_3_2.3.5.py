# Estado de los interruptores (0 para apagado, 1 para encendido)
interruptor1 = 1
interruptor2 = 0

# Verificación de la lógica del interruptor de escalera
if interruptor1 == 1 and interruptor2 == 1:
    print("La luz está encendida")
elif interruptor1 == 0 and interruptor2 == 0:
    print("La luz está apagada")
else:
    print("Estado no válido de los interruptores")

# Explicación del resultado según los estados de los interruptores
if interruptor1 == interruptor2:
    print("Ambos interruptores están en el mismo estado.")
else:
    print("Los interruptores están en estados diferentes.")
