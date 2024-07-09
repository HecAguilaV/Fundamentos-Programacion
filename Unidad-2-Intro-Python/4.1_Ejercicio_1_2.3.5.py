#Ejercicio 1: Serie de encuestas que permitan describir el nivel de desarrollo de los alumnos El test consta de 12 preguntas, cada una de las cuales posee un punto.
print(" ")
print("----Formulario----")
print("A continuación deberas responder un cuestionario con 12 preguntas de Si o No \nlas cuales estan relacionadas a tu nivel de desarrollo como alumno")
print(" ")
print("1. Estudia al menos 3 veces por semana")
respt1 = input("Ingrese su respuesta (Ej: s/n) ")

if respt1 == "s":
    respt1 = 1
else:
    respt1 = 0

print(" ")
print("2. ¿Usted tiene un buen habito de lectura (Al menos 2 veces a la semana)?")
respt2 = input("Ingrese su respuesta ")
if respt2 == "s":
    respt2 = 1
else:
    respt2 = 0

print(" ")
print("3. Tiene un buen habito de sueño")
respt3 = input("Ingrese su respuesta ")
if respt3 == "s":
    respt3 = 1
else:
    respt3 = 0

print(" ")
print("4. Llega habitualmente temprano a clases")
respt4 = input("Ingrese su respuesta ")
if respt4 == "s":
    respt4 = 1
else:
    respt4 = 0

print(" ")
print("5. Siempre esta al tanto de sus trabajos o tareas semanales")
respt5 = input("Ingrese su respuesta ")
if respt5 == "s":
    respt5 = 1
else:
    respt5 = 0

print(" ")
print("6. Siempre hace sus tareas a tiempo")
respt6 = input("Ingrese su respuesta ")
if respt6 == "s":
    respt6 = 1
else:
    respt6 = 0

print(" ")
print("7. Prefiere anteponer sus actividades extracurriculares a sus trabajos educacionales")
respt7 = input("Ingrese su respuesta ")
if respt7 == "n":
    respt7 = 1
else:
    respt7 = 0

print(" ")
print("8. Al regresar de clases usted estudia al menos media hora")
respt8 = input("Ingrese su respuesta ")
if respt8 == "s":
    respt8 = 1
else:
    respt8 = 0

print(" ")
print("9. Se junta con sus compañeros (ya sea presencial u online) a \ndiscutir sobre una materia u contenido")
respt9 = input("Ingrese su respuesta ")
if respt9 == "s":
    respt9 = 1
else:
    respt9 = 0

print(" ")
print("10. Participas activamente en las actividades de clases")
respt10 = input("Ingrese su respuesta ")
if respt10 == "s":
    respt10 = 1
else:
    respt10 = 0

print(" ")
print("11. Al tener una prueba estudias al menos con 1 semana de anticipación")
respt11 = input("Ingrese su respuesta ")
if respt11 == "s":
    respt11 = 1
else:
    respt11 = 0

print(" ")
print("12. Te estresa que en los trabajos grupales no se hagan las cosas como tu quieres")
respt12 = input("Ingrese su respuesta ")
if respt12 == "n":
    respt12 = 1
else:
    respt12 = 0

puntos = respt1+respt2+respt3+respt4+respt5+respt6+respt7+respt8+respt9+respt10+respt11+respt12

if puntos >= 0 and puntos <= 3:
    print("Su puntaje es ", puntos, " usted alumno con muchos desafíos")
elif puntos > 3 and puntos <= 6:
    print("Su puntaje es ", puntos, " usted es un alumno con algunos desafíos")
elif puntos > 6 and puntos <= 9:
    print("Su puntaje es ", puntos, " usted es un alumno que puede mejorar")
else:
    print("Su puntaje es ", puntos, " usted es un alumno de buen desempeño")