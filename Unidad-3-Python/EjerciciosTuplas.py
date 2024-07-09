#Ejercicio 1: Información Personal

informacion = ("Héctor", 39, "Puerto Montt")

print(informacion[0])
print(informacion[1])
print(informacion[2])

nombre, edad, ciudad = informacion

print("Nombre: ", nombre)
print("Edad: ", edad)
print("Ciudad: ", ciudad)


#Ejercicio 2: Operaciones con Tuplas Numéricas

numeros = (1,2,3,4,5,6,7,8,9,10)

print(sum(numeros))
print(max(numeros))
print(min(numeros))
print(numeros.count(5))


#Ejercicio 3: Rebanado de Tuplas

letras = ("a","b","c","d","e","f","g","h","i","j")

subtupla = letras[:5]
subtupla2 = letras[7:]
subtupla3 = letras[::2]

print(subtupla)
print(subtupla2)
print(subtupla3)