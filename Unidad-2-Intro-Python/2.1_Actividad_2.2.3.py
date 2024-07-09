# MatriculaColegio

# Solicitar información al usuario
nomAlum = input("Ingrese el nombre del alumno: ")
rut = input("Ingrese rut del apoderado: ")
curso = input("Ingrese curso al cual el alumno debe matricularse: ")

# Definir valores de matrícula y mensualidad
matricula = 25000
mensualidad = 30000

# Calcular valor anual (10 meses de mensualidad más matrícula)
resultadoAnual = (mensualidad * 10) + matricula

# Mostrar detalle de la anualidad
print("---- Detalle Anualidad Colegio ----")
print(f"NOMBRE ALUMNO: {nomAlum}")
print(f"RUT APODERADO: {rut}")
print(f"CURSO MATRICULADO: {curso}")
print(f"VALOR MATRÍCULA: {matricula}")
print(f"VALOR MENSUALIDAD: {mensualidad}")
print(f"VALOR TOTAL A PAGAR: {resultadoAnual}")
