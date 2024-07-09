usuarios = {}
while True:
    print("\nMenú:\n1. Iniciar sesión\n2. Registrar usuario\n3. Eliminar usuario\n4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        usuario = input("Ingrese nombre de usuario: ")
        contrasena = input("Ingrese contraseña: ")
        if usuario in usuarios and usuarios[usuario] == contrasena:
            print("Sesión válida.\n")
        else:
            print("Error: Usuario o contraseña incorrectos.\n")

    elif opcion == "2":
        nuevo_usuario = input("Ingrese un nuevo usuario: ")
        nueva_contrasena = input("Ingrese una contraseña: ")
        usuarios[nuevo_usuario] = nueva_contrasena
        print(f"Usuario {nuevo_usuario} registrado correctamente.\n")

    elif opcion == "3":
        usuario_eliminar = input("Ingrese el nombre de usuario a eliminar: ")
        if usuario_eliminar in usuarios:
            contrasena_confirmar = input("Ingrese su contraseña para confirmar: ")
            if usuarios[usuario_eliminar] == contrasena_confirmar:
                del usuarios[usuario_eliminar]
                print(f"Usuario {usuario_eliminar} eliminado correctamente.")
            else:
                print("Error: Contraseña incorrecta.")
        else:
            print("Error: Usuario no encontrado.")

    elif opcion == "4":
        print("Bye Bye")
        break
    else:
        print("Error. Inténtelo nuevamente.\n")