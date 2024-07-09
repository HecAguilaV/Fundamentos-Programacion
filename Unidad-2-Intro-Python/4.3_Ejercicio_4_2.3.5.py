print("¡Bienvenido a la aventura!")
print("Puedes avanzar hacia adelante ('w'), hacia la derecha ('d') o hacia la izquierda ('a').")
print(" ")

print("Estás en el bosque profundo. De repente, escuchas un rugido.")
opcion = input("¿Qué camino eliges? (w/a/d): ").lower()

if opcion == "w":
    print("Avanzas hacia adelante y encuentras un río caudaloso.")
    opcion = input("¿Intentas cruzarlo? (s/n): ").lower()
    if opcion == "s":
        print("Cruzas el río con éxito y encuentras un cofre con monedas de oro.")
    else:
        print("Decides no arriesgarte y te alejas del río.")
elif opcion == "d":
    print("Te diriges hacia la derecha y te encuentras con una cueva oscura.")
    opcion = input("¿Entrar en la cueva? (s/n): ").lower()
    if opcion == "s":
        print("Exploras la cueva y encuentras un mapa del tesoro.")
    else:
        print("Decides no entrar y continúas tu camino por el bosque.")
elif opcion == "a":
    print("Giras hacia la izquierda y te topas con un sendero rocoso.")
    opcion = input("¿Seguir el sendero? (s/n): ").lower()
    if opcion == "s":
        print("Sigues el sendero y descubres una antigua estatua misteriosa.")
    else:
        print("Prefieres explorar otro camino del bosque.")
else:
    print("No decides moverte y un águila te observa desde arriba.")

print("")
print("Fin de la aventura. ¡Gracias por jugar!")
