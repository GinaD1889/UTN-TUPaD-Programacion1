# Escape Room: "La arena del gladiador"

# Configuracion del personaje:

nombre_gladiador = input("Ingrese el nombre del gladiador: ")

while not nombre_gladiador.isalpha():
    print("Error: solo se permiten letras.")
    nombre_gladiador = input("Ingrese nuevamente el nombre: ")

# Estadisticas iniciales:

hp_jugador = 100
hp_enemigo = 100
pociones = 3

daño_base_jugador = 15
daño_base_enemigo = 12

turno_jugador = True
juego_activo = True

print(f"Bienvenido/a {nombre_gladiador}.")
print("Comienza la batalla contra el enemigo.")

# Ciclo principal del combate:

while hp_jugador > 0 and hp_enemigo > 0 and juego_activo:

    if turno_jugador:
        print("==========ESTADO DE LA BATALLA==========")
        print(f"Vida de {nombre_gladiador}: {hp_jugador}")
        print(f"Vida del enemigo: {hp_enemigo}")
        print(f"Pociones disponibles: {pociones}")

        print("Que accion desea realizar?")
        print("1. Ataque pesado.")
        print("2. Rafaga veloz.")
        print("3. Curar.")

        opcion = input("Seleccione una opcion: ")

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            print("Error: seleccione una opcion del 1 al 3.")
            opcion = input("Seleccione nuevamente una opcion: ")

            opcion= int(opcion)


        # Accion 1: Ataque pesado

        if opcion == "1":
            if hp_enemigo < 20:
                daño_final = float(daño_base_jugador * 1.5)
                print("Golpe critico!")
            else:
                daño_final = float(daño_base_jugador)
                hp_enemigo -= int(daño_final)
                print(f"Atacaste al enemigo por: " f"{daño_final:.1f} puntos de daño.")

        # Accion 2: Rafaga veloz

        elif opcion == "2":

            print("Iniciaste una rafaga veloz!")

            for golpe in range(3):
                if hp_enemigo > 0:
                    hp_enemigo -= 5
                    print("Golpe conectado por 5 de daño.")

                    print("La rafaga termino.")

        # Accion 3: Curar

        elif opcion == "3":

            if pociones > 0:
                hp_jugador += 30

                if hp_jugador > 100:
                    hp_jugador = 100

                pociones -= 1

                print("Usaste una pocion.")
                print(f"Tu vida actual es: {hp_jugador}")
            else:
                print("No quedan pociones!.")
                print("Perdiste el turno!.")

        # Verificar si el enemigo fue derrotado:

        if hp_enemigo <= 0:
            juego_activo = False
        else:
            # Turno automatico del enemigo

            turno_jugador = False

            hp_jugador -= daño_base_enemigo

            print(f"El enemigo te ataco por: {daño_base_enemigo} puntos de daño.")

            turno_jugador = True

# Resultado Final:

print("====================")
print(" FIN DE LA BATALLA")
print("====================")

if hp_jugador > 0 and hp_enemigo <= 0:
    print(f"VICTORIA: {nombre_gladiador} HA GANADO LA BATALLA!")
elif hp_jugador <= 0:
    print("DERROTA. HAS CAIDO EN COMBATE.")

