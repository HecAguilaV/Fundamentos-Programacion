Proceso Saber_si_numero_es_impar_o_par
    Definir n1 Como Entero;
	
    Escribir "Ingrese un n�mero: ";
    Leer n1;
    
    Si n1 mod 2 == 0 Entonces
        Escribir "El n�mero ", n1, ": es par.";
    Sino 
        Escribir "El n�mero ", n1, ": es impar.";
    FinSi
FinProceso