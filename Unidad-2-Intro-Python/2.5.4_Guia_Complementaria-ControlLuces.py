patio = False
sala = False
pasillo = False
jardin = False

while True:
    print("1.- Encender/Apagar luces Patio (Alternado)")
    print("2.- Encender/Apagar luces Sala (Alternado)")
    print("3.- Encender/Apagar luces Pasillo (Alternado)")
    print("4.- Encender/Apagar luces Jardín (Alternado)")
    print("5.- Encender todo (Alternado)")
    print("6.- Apagar todo (Alternado)")
    print("7.- Salir del sistema")
    
    try:
        opcion = int(input("Ingrese la opción deseada: "))
    except ValueError:
        opcion = 0

    if opcion == 1:
        patio = not patio
        print("El patio está ", "encendido" if patio else "apagado")
 
    elif opcion == 2:
        sala = not sala
        print("La sala está ", "encendida" if sala else "apagada")
 
    elif opcion == 3:
        pasillo = not pasillo
        print("El pasillo está ", "encendido" if pasillo else "apagado")
 
    elif opcion == 4:
        jardin = not jardin
        print("El jardín está ", "encendido" if jardin else "apagado")
 
    elif opcion == 5:
        patio = True
        sala = True
        pasillo = True
        jardin = True   
        print("Se han encendido todas las luces")
 
    elif opcion == 6:
        patio = False
        sala = False
        pasillo = False
        jardin = False      
        print("Se han apagado todas las luces")
 
    elif opcion == 7:
        print("Hasta pronto...")
        break
    else:
        print("Opción no válida")