Proceso Calculadora
	Definir n1, n2, result, op Como Real;
	
	Repetir
		Escribir "Ingrese primer número";
		Leer n1;
		
		Escribir "Ingrese segundo número";
		Leer n2;
		
		Escribir "Defina que operación desea:";
		Escribir "1. Suma";
		Escribir "2. Resta";
		Escribir "3. Multiplicación";
		Escribir "4. División";
		Escribir "0. Salir";
		Leer op;
		
		Segun op Hacer
			1: result <- n1 + n2;
				Escribir "La suma es: ", result, ".";
			2: result <- n1 - n2;
				Escribir "La resta es: ", result, ".";
			3: result <- n1 * n2;
				Escribir "La multiplicación es: ", result, ".";
			4: result <- n1 / n2;
				Escribir "La división es: ", result, ".";
			0: Escribir "Saliendo...";
			De Otro Modo:
				Escribir "Formula no válida";
		FinSegun
		
	Hasta Que op = 0;
	
FinProceso