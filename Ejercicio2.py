# Acceso al Campus y Menu seguro

# Credenciales fijas:

usuario_correcto= "alumno"
clave_correcta= "abc123"

intentos= 0
ingreso_exitoso= False

# Inicio de sesion: maximo 3 intentos

while intentos < 3 and not ingreso_exitoso:
    usuario= input("Ingrese su usuario: ")
    clave= input("Ingrese su clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        ingreso_exitoso = True
        print ("Ingreso exitoso!")
    else:
        intentos += 1
        restantes = 3 - intentos

        if restantes > 0:
            print (f"Usuario o clave incorrectos. Intentos restantes: {restantes}")
        else:
            print ("Cuenta bloqueada")


# Menu principal

if ingreso_exitoso:
    while True:
        print ("====== MENU PRINCIPAL ======")
        print ("1. Ver estado de inscripcion.")
        print ("2. Cambiar clave.")
        print ("3. Mostrar mensaje motivacional.")
        print ("4. Salir.")  

        opcion = input ("Seleccione una opcion: ")

        # Validacion de la opcion menu:

        if not opcion.isdigit():
            print ("Error: debe ingresar un numero.")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: la opcion debe estar entre 1 y 4.")
            continue

        if opcion == 1:
            print("Estado de inscripcion: Inscripto.")
        elif opcion == 2:
            nueva_clave = input("Ingrese la nueva clave: ")

            if len(nueva_clave) < 6:
                print("La nueva clave debe tener como minimo 6 caracteres.")
            else:
                confirmacion= input ("Confirme la nueva clave: ")

                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print ("La clave fue cambiada correctamente!")
                else:
                    print ("Las claves no coinciden. No se realizo el cambio.")
        elif opcion == 3:
            print("Cada pequeño esfuerzo te acerca mas a tus objetivos! ")
        elif opcion == 4:
            print ("Sesion finalizada. Hasta luego!")
            break           


