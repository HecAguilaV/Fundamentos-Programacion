Proceso Carrera_obstaculos
    Definir o1, o2, o3, r Como Entero;
    
    Escribir "¡Comienza la carrera!";
    Escribir "Al continuar con tu carrera podrías encontrar varios obstáculos";
    
    Escribir "¿Encontraste una valla? (escribe el número de la opción)";
    Escribir "1. Sí";
    Escribir "2. No";
    Leer o1;
    
    Segun o1 Hacer
        1:
            Escribir "Saltas la valla haciendo una voltereta triple";
        De Otro Modo:
            Escribir "Continúas corriendo sin mirar atrás";
    FinSegun
    
    Escribir "Sigues con la carrera";
    Escribir "A continuación, ¿encontraste un túnel?";
    Escribir "1. Sí";
    Escribir "2. No";
    Leer o2;
    
    Segun o2 Hacer
        1:
            Escribir "Atraviesas el túnel lo más rápido posible ya que es un túnel embrujado y si te quedas mucho tiempo serás poseído";
        De Otro Modo:
            Escribir "Continúas corriendo sin mirar atrás";
    FinSegun
    
    Escribir "La carrera sigue";
    Escribir "A continuación, ¿encontraste una laguna?";
    Escribir "1. Sí";
    Escribir "2. No";
    Leer o3;
    
    Segun o3 Hacer
        1:
            Escribir "Es imposible rodear esta laguna ya que es infinita";
            Escribir "¿Qué harás?";
            Escribir "1. Nadar";
            Escribir "2. Dar la vuelta";
            Leer r;
            
            Si r = 1 Entonces
                Escribir "Te lanzas hacia la laguna y nadas lo más rápido posible";
                Escribir "De repente, una manta raya aparece y te ayuda a cruzar";
                Escribir "Gracias a ella ya ves la meta en el horizonte";
                Escribir "¡¡¡Has ganado la carrera!!!";
            SiNo
                Escribir "Oh no. Ya que vas de regreso, debo informarte que has perdido la carrera.";
            FinSi
        De Otro Modo:
            Escribir "Continúas corriendo sin mirar atrás";
            Escribir "¡¡¡Has ganado la carrera!!!";
    FinSegun
	
FinProceso
