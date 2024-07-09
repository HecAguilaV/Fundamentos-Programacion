Proceso Saber_si_numero_es_impar_o_par
    Definir n1 Como Entero;
	
    Escribir "Ingrese un número: ";
    Leer n1;
    
    Si n1 mod 2 == 0 Entonces
        Escribir "El número ", n1, ": es par.";
    Sino 
        Escribir "El número ", n1, ": es impar.";
    FinSi
FinProceso