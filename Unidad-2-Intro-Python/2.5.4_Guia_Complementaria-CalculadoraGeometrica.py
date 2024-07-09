print("Calculadora Geométrica")  

while True:  
    print("***********Menu************")  
    print("1. Calcular Perímetro")  
    print("2. Calcular Área")  
    print("3. Salir")  
    
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        while True:  
            print("Calcular Perímetro")  
            print("1. Para Círculo")  
            print("2. Para Rectángulo")  
            print("3. Para Cuadrado")  
            print("4. Volver menu principal")  
            
            opcion2 = int(input("Elija una opción: "))  

            if opcion2 == 1:  
                radio = int(input("Ingrese radio del círculo: "))              
                perimetro = 2 * 3.14 * radio  
                print("Perímetro del Círculo: ", perimetro)  

            elif opcion2 == 2:  
                altura = int(input("Ingrese altura del Rectángulo: "))  
                ancho = int(input("Ingrese ancho del Rectángulo: "))  
                perimetro = 2 * (altura + ancho)  
                print("Perímetro del Rectángulo: ", perimetro)  

            elif opcion2 == 3:  
                lado = int(input("Ingrese lado del Cuadrado: "))  
                perimetro = 4 * lado  
                print("Perímetro del Cuadrado: ", perimetro)              

            elif opcion2 == 4:  
                break         

            else:  
                print("Elección inválida.")  
    
    elif opcion == 2:  
        while True:  
            print("Calcular Área")  
            print("1. Para Círculo")  
            print("2. Para Rectángulo")  
            print("3. Para Cuadrado")  
            print("4. Volver menu principal")  

            opcion3 = int(input("Elija una opción: "))  

            if opcion3 == 1:  
                radio = int(input("Ingrese radio del círculo: "))  
                area = 3.14 * radio * radio  
                print("Área del Círculo: ", area)  

            elif opcion3 == 2:  
                altura = int(input("Ingrese altura del Rectángulo: "))  
                ancho = int(input("Ingrese ancho del Rectángulo: "))  
                area = altura * ancho  
                print("Área del Rectángulo: ", area)   

            elif opcion3 == 3:  
                lado = int(input("Ingrese lado del Cuadrado: "))  
                area = lado * lado  
                print("Área del Cuadrado: ", area)  

            elif opcion3 == 4:  
                break              

            else:  
                print("Elección inválida.")  
    
    elif opcion == 3:  
        break     

    else:  
        print("Elección inválida.")  