# Cuarta etapa: Ingresar información personal y mostrar en mayúsculas

# Solicitar y capturar información del usuario
noM = input("Ingrese su nombre: ")
nombre = noM.upper()

ruN = input("Ingrese su RUN: ")
run = ruN.upper()

correO = input("Ingrese su correo: ")
correo = correO.upper()

teleF = input("Ingrese su teléfono: ")
telefono = teleF.upper()

# Mostrar la información ingresada en mayúsculas
print(f"NOMBRE: {nombre} \nRUN: {run} \nCORREO: {correo} \nTELÉFONO: {telefono}")