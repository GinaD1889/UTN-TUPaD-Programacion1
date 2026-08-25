# Agenda de turnos con Nombres.

# Datos inciales del sistema:

operador = input("Ingrese el nombre del operador: ")

while not operador.isalpha():
    print("Error: el nombre debe contener solamente letras.")
    operador= input("Ingrese nuevamente el nombre del operador: ")

print(f"Bienvenido/a {operador}.")

# Turnos del lunes:

lunes1 = ""
lunes2 = ""
lunes3 = ""

# Turnos del martes:

martes1 = ""
martes2 = ""
martes3 = ""

# Menu principal:

while True:
    print("====== MENU ======")
    print("1. Reservar turno.")
    print("2. Cancelar turno.")
    print("3. Ver agenda del dia.")
    print("4. Ver resumen general.")
    print("5. Cerrar sistema.")

    opcion = input("Seleccione una opcion: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: ingrese un numero del 1 al 5.")
        opcion = input("Seleccione una opcion: ")

    opcion = int(opcion)

    # Reservar turno: 

    if opcion == 1:
        print("Usted eligio reservar un turno.")
        print("Dias disponibles: ")
        print("1. Lunes")
        print("2. Martes")

        dia = input("Seleccione el dia: ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: Seleccione 1 para el lunes o 2 para el martes: ")
            dia = input("Seleccione nuevamente el dia: ")

            dia = int(dia)

        paciente= input("Ingrese el nombre del paciente: ")
            
        while not paciente.isalpha():
            print("Error: el nombre debe contener solamente letras.")
            paciente = input("Ingrese nuevamente el nombre del paciente: ")

             # Reserva para el dia lunes:

        if dia == "1":
            print("Turnos disponibles para el lunes: ")

            if lunes1 == "":
                print("Turno N1: LIBRE.")
            else:
                print("Turno N1: OCUPADO.")

            if lunes2 == "":
                print("Turno N2: LIBRE.")
            else:
                print("Turno N2: OCUPADO.")

            if lunes3 == "":
                print ("Turno N3: LIBRE.")
            else:
                print("Turno N3: OCUPADO.")

            turno = input("Seleccione el turno del deseado del dia lunes: ")

            while not turno.isdigit() or int(turno) < 1 or int(turno) > 3:
                print("Error, seleccione un turno del 1 al 3.")
                turno = input("Seleccione nuevamente el turno deseado del dia lunes: ")

            turno = int(turno)    

            # Verificamos si el paciente ya esta registrado el dia lunes:

            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3:
                print("El paciente ya tiene un turno reservado ese dia.")
            elif turno == 1:
                if lunes1 == "":
                     lunes1 = paciente                           
                     print("Turno reservado correctamente! Lunes - Turno N1.")
                else:
                    print("El turno N1 ya esta ocupado.")
            elif turno == 2:
                if lunes2 == "":
                     lunes2 = paciente
                     print("Turno reservado correctamente! Lunes - Turno N2.")
                else:
                    print("El turno N2 ya esta ocupado.")
            elif turno == 3:
                if lunes3 == "":
                     lunes3 = paciente
                     print("Turno reservado correctamente! Lunes - Turno N3.")
                else: 
                    print("El turno N3 ya esta ocupado.")
            else:
                print("No hay turnos disponibles para el dia lunes.")

                     
                # Reserva para el dia martes:

        elif dia == "2":
            print("Turnos disponibles para el dia martes.")

            if martes1 == "":
                print("Turno N1: LIBRE.")
            else:
                print("Turno N1: OCUPADO.")
            
            if martes2 == "":
                print("Turno N2: LIBRE.")
            else:
                 print("Turno N2: OCUPADO.")
            
            if martes3 == "":
                print ("Turno N3: LIBRE.")
            else:
                print("Turno N3: OCUPADO.")
            
            turno = input("Seleccione el turno del deseado del dia martes: ")
            
            while not turno.isdigit() or int(turno) < 1 or int(turno) > 3:
                print("Error, seleccione un turno del 1 al 3.")
                turno = input("Seleccione nuevamente el turno deseado del dia lunes: ")
            
            turno = int(turno)    
            
            # Verificamos si el paciente ya esta registrado el dia martes:

            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("El paciente ya tiene un turno reservado ese dia.") 
            elif turno == 1:
                 if martes1 == "":                          
                     martes1 = paciente
                     print("Turno reservado correctamente! Martes - Turno N1.")
                 else:
                     print("El turno N1 ya esta ocupado.")
            elif turno == 2:
                 if martes2 == "":
                     martes2 = paciente
                     print("Turno reservado correctamente! Martes - Turno N2.")
                 else:
                     print("El turno N2 ya esta ocupado.")
            elif turno == 3:
                 if martes3 == "":            
                    martes3 = paciente
                    print("Turno reservado correctamente! Martes - Turno N3.")
                 else:
                     print("El turno N3 ya esta ocupado.")
            else:
               print("No hay turnos disponibles para el dia martes.")


    # Cancelar turnos:

    elif opcion == 2:
        print("Dias disponibles: ")
        print("1. Lunes")
        print("2. Martes")
        
        dia = input("Seleccione el dia: ")
        
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: Seleccione 1 para el lunes o 2 para el martes: ")
            dia = input("Seleccione el dia: ")
        
            dia= int(dia)
        
        paciente= input("Ingrese el nombre del paciente a cancelar: ")
        
        while not paciente.isalpha():
            print("Error: el nombre debe contener solamente letras.")
            paciente = input("Ingrese nuevamente el nombre del paciente: ")

        cancelado = False

        if dia == "1":
            if paciente == lunes1:
                lunes1 = ""
                cancelado = True
            elif paciente == lunes2:
                lunes2 = ""
                cancelado = True
            elif paciente == lunes3:
                lunes3 = ""
                cancelado = True
        else:
            if paciente == martes1:
                lunes1 = ""
                cancelado = True
            elif paciente == martes2:
                martes2 = ""
                cancelado = True
            elif paciente == martes3:
                martes3 = ""
                cancelado = True 

        if cancelado:
            print("Turno cancelado correctamente.")
        else:
            print("No se encontro un turno para ese paciente en el dia indicado.")

        
    # Ver agenda del dia:

    elif opcion == 3:
        print("Dias disponibles: ")
        print("1. Lunes")
        print("2. Martes")
                
        dia = input("Seleccione el dia: ")
                
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: Seleccione 1 para el lunes o 2 para el martes: ")
            dia = input("Seleccione el dia: ")
                
            dia= int(dia)

        if dia == "1":
            print("Agenda del lunes: ")
            if lunes1 == "":
                print("Turno N1: LIBRE.")
            else:
                print(f"Turno N1 : {lunes1}")
            if lunes2 == "":
                print("Turno N2: LIBRE.")
            else:
                print(f"Turno N2: {lunes2}")
            if lunes3 == "":
                print("Turno N3: LIBRE.")
            else:
                print(f"Turno N3: {lunes3}")
        else:
            print("Agenda del martes: ")
            if martes1 == "":
                    print("Turno N1: LIBRE.")
            else:
                print(f"Turno N1 : {martes1}")
            if martes2 == "":
                print("Turno N2: LIBRE.")
            else:
                print(f"Turno N2: {martes2}")
            if martes3 == "":
                print("Turno N3: LIBRE.")
            else:
                print(f"Turno N3: {martes3}")

    # Resumen general:

    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        disponibles_lunes = 3 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print("====== RESUMEN GENERAL ======")
        print("Lunes: ")
        print(f"Turnos ocupados: {ocupados_lunes}")
        print(f"Turnos disponibles: {disponibles_lunes}")
        print("Martes: ")
        print(f"Turnos ocupados: {ocupados_martes}")
        print(f"Turnos disponibles: {disponibles_martes}")


        if ocupados_lunes > ocupados_martes:
            print("El dia con mas turnos es el lunes.")
        elif ocupados_martes > ocupados_lunes:
            print("El dia con mas turnos es el martes.")
        else:
            print("Hay empate: lunes y martes tienen la misma cantidad de turnos.")

    # Cerrar sistema:  
                                               
    elif opcion == 5:
        print(f"Sistema cerrado por el operador: {operador}.")
        break




