Proceso Adivina_Numero
    Definir intentos, numSecreto, numIngresado Como Entero;
    
    intentos <- 10;
    numSecreto <- azar(100) + 1;
    
    Escribir "Adivine el n�mero (de 1 a 100): ";
    Leer numIngresado;
    
    Mientras numSecreto <> numIngresado Y intentos > 1 Hacer
        Si numSecreto > numIngresado Entonces
            Escribir "Muy bajoo.";
        Sino 
            Escribir "Muy alto.";
        FinSi
        intentos <- intentos - 1;
        Escribir "Le quedan ", intentos, " intentos: ";
        Leer numIngresado;
    FinMientras
    
    Si numSecreto = numIngresado Entonces
        Escribir "�Exacto! Usted adivin� en ", 11 - intentos, " intentos.";
    Sino
        Escribir "El n�mero era: ", numSecreto, ".";
    FinSi
FinProceso