Proceso Calcular_edad
	Definir anio, mes, dia Como Entero;
	Definir anioActual, mesActual, diaActual Como Entero;
	Definir edadAnio, edadMeses, edadDias Como Entero;
	
	Escribir "Ingrese fecha actual: ";
	Escribir "A�o: ";
	
	Leer anioActual;
	Escribir "Mes: ";
	Leer mesActual;
	
	Escribir "Dia: ";
	Leer diaActual;
	
	Escribir "Escriba su a�o de nacimiento: ";
	Leer anio;
	
	Escribir "Escriba el n�mero de su mes de nacimiento: ";
	Leer mes;
	
	Escribir "Escriba el n�mero de su d�a de nacimiento: ";
	Leer dia;
	
	edadAnio <- anioActual - anio;
	Si mesActual < mes O mesActual > m Y diaActual < d Entonces
		edadAnio <- edadAnio - 1;
	FinSi
	
	edadMeses <- mesActual - mes;
	Si edadMeses < 0 Entonces
		edadMeses <- edadMeses + 12;
	FinSi
	
	edadDias <- diaActual - dia;
	Si edadDias < 0 Entonces
		edadDias <- edadDias + 30;
		edadMeses <- edadMeses - 1;
		Si edadMeses < 0 Entonces
			edadMeses <- edadMeses + 12;
			edadAnio <- edadAnio - 1;
		FinSi
	FinSi
		
	Escribir "Usted tiene ", edadAnio, " a�os, ", edadMeses, " meses y ", edadDias, " d�as.";
FinProceso