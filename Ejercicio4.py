# Escape Room: La Boveda:

# Variables iniciales:

energia = 100
tiempo = 12
cerraduras_abiertas= 0
alarma = False
codigo_parcial = ""

racha_forzar = 0

# Ingreso del agente:

agente = input("Ingrese el nombre del agente: ")

while not agente.isalpha():
    print("Error, el nombre debe contener solamente letras.")
    agente = input("Ingrese nuevamente el nombre del agente: ")

print(f"Bienvenido/a, agente {agente}!")
print("La mision consiste en abrir una boveda con 3 cerraduras.")


# Juego principal:

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    print("=====================")
    print(" ESTADO DE LA MISION")
    print("=====================")
    print(f"Energia: {energia}")
    print(f"Tiempo restante : {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas} /3")
    print(f"Alarma: {alarma}")
    print(f"Codigo parcial: {codigo_parcial}")

    print("======MENU======")
    print("1. Forzar Cerradura.")
    print("2. Hackear panel.")
    print("3. Descansar.")

    opcion = input("Seleccione una opcion: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese una opcion entre 1, 2, 3: ")
        opcion = input("Seleccione nuevamente una opcion: ")

    # OPCION 1 - FORZAR CERRADURAS:

    if opcion == "1":
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        print("Intentando forzar una cerradura...")
        print("Costo aplicado: .20 energia y - 2 tiempo.")

        # Regla anti-spam: tercera vez consecutiva

        if racha_forzar ==3:
            alarma = True
            print("La cerradura se trabo..")
            print("Alarma activada automaticamente.")
            print("La cerradura no se abrio.")
        else:
            if energia < 40:
                print("La energia esta por debajo de 40..")
                print("Existe riesgo de activar la alarma.")
                numero_riesgo = input ("Ingrese un numero del 1 al 3 para intentar evitarla:")

                while not numero_riesgo.isdigit() or int(numero_riesgo) < 1 or int(numero_riesgo) >3:
                    print("Error: Ingrese nuevamente un numero del 1 al 3 para intentar evitarla:")
                    numero_riesgo = int(numero_riesgo)

                if numero_riesgo == 3:
                    alarma = True
                    print("Alarma activada.")
            if not alarma:
                cerraduras_abiertas += 1
                print("Cerradura abierta correctamente.")
                print(f"Cerraduras abiertas {cerraduras_abiertas} /3")        

    # OPCION 2: HACKEAR PANEL 

    elif opcion == "2":
        racha_forzar = 0

        energia -= 10
        tiempo -= 3

        print("Iniciando hackeo del panel...")
        print("Costo aplicado: -10 energia y -3 tiempo.")

        for paso in range(1,5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4 completado.")
            print(f"Codigo parcial {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("El codigo parcial alcanzo 8 caracteres.")
            print("Se abrio automaticamente una cerradura.")
        else:
            print("EL hackeo avanzo, pero todavia no abre una cerradura.")

    # OPCION 3: DESCANSAR
    elif opcion == "3":
        racha_forzar = 0

        energia += 15

        if energia > 100:
            energia = 100

            tiempo -= 1

            print("El agente descanso!.")
            print("Recupero 15 puntos de energia.")
            print("Costo aplicado_ -1 tiempo.")

        if alarma:
            energia -= 10
            print("La alarma esta activa.")
            print("Se perdieron 10 puntos adicionales de energia.")

    # BLOQUEO POR ALARMA

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("La alarma permanece activa.")
        print("El tiempo es igual o menor que 3.")
        print("El sistema bloqueo la boveda")
        break

    # CONDIICONES FINALES

    print("======================")
    print("RESULTADO DE LA MISION")  
    print("======================")

    if cerraduras_abiertas == 3:
        print(f"VICTORIA, agente {agente}")
        print("Abriste las 3 cerraduras antes de quedarte sin recursos.")
    elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("DERROTA POR BLOQUEO.")
        print("La boveda quedo bloqueada por la alarma.")
    elif energia <= 0:
        print("DERROTA.")
        print("Te quedaste sin energia.")
    elif tiempo <= 0:
        print("DERROTA.")
        print("Te quedaste sin tiempo.")
    elif alarma:
        print("DERROTA.")
        print("La alarma quedo activada.")                       
