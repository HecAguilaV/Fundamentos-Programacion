Proceso Carrera_obstaculos
    Definir o1, o2, o3, r Como Entero;
    
    Escribir "�Comienza la carrera!";
    Escribir "Al continuar con tu carrera podr�as encontrar varios obst�culos";
    
    Escribir "�Encontraste una valla? (escribe el n�mero de la opci�n)";
    Escribir "1. S�";
    Escribir "2. No";
    Leer o1;
    
    Segun o1 Hacer
        1:
            Escribir "Saltas la valla haciendo una voltereta triple";
        De Otro Modo:
            Escribir "Contin�as corriendo sin mirar atr�s";
    FinSegun
    
    Escribir "Sigues con la carrera";
    Escribir "A continuaci�n, �encontraste un t�nel?";
    Escribir "1. S�";
    Escribir "2. No";
    Leer o2;
    
    Segun o2 Hacer
        1:
            Escribir "Atraviesas el t�nel lo m�s r�pido posible ya que es un t�nel embrujado y si te quedas mucho tiempo ser�s pose�do";
        De Otro Modo:
            Escribir "Contin�as corriendo sin mirar atr�s";
    FinSegun
    
    Escribir "La carrera sigue";
    Escribir "A continuaci�n, �encontraste una laguna?";
    Escribir "1. S�";
    Escribir "2. No";
    Leer o3;
    
    Segun o3 Hacer
        1:
            Escribir "Es imposible rodear esta laguna ya que es infinita";
            Escribir "�Qu� har�s?";
            Escribir "1. Nadar";
            Escribir "2. Dar la vuelta";
            Leer r;
            
            Si r = 1 Entonces
                Escribir "Te lanzas hacia la laguna y nadas lo m�s r�pido posible";
                Escribir "De repente, una manta raya aparece y te ayuda a cruzar";
                Escribir "Gracias a ella ya ves la meta en el horizonte";
                Escribir "���Has ganado la carrera!!!";
            SiNo
                Escribir "Oh no. Ya que vas de regreso, debo informarte que has perdido la carrera.";
            FinSi
        De Otro Modo:
            Escribir "Contin�as corriendo sin mirar atr�s";
            Escribir "���Has ganado la carrera!!!";
    FinSegun
	
FinProceso
