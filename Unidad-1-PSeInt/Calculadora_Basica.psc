Proceso Calculadora
	Definir n1, n2, result, op Como Real;
	
	Repetir
		Escribir "Ingrese primer n�mero";
		Leer n1;
		
		Escribir "Ingrese segundo n�mero";
		Leer n2;
		
		Escribir "Defina que operaci�n desea:";
		Escribir "1. Suma";
		Escribir "2. Resta";
		Escribir "3. Multiplicaci�n";
		Escribir "4. Divisi�n";
		Escribir "0. Salir";
		Leer op;
		
		Segun op Hacer
			1: result <- n1 + n2;
				Escribir "La suma es: ", result, ".";
			2: result <- n1 - n2;
				Escribir "La resta es: ", result, ".";
			3: result <- n1 * n2;
				Escribir "La multiplicaci�n es: ", result, ".";
			4: result <- n1 / n2;
				Escribir "La divisi�n es: ", result, ".";
			0: Escribir "Saliendo...";
			De Otro Modo:
				Escribir "Formula no v�lida";
		FinSegun
		
	Hasta Que op = 0;
	
FinProceso