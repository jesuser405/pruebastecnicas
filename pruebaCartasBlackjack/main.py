import random

# Valores posibles de las cartas
VALOR_CARTAS = {2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'AS'}

# Valores numéricos de las cartas
VALOR_NUM_CARTAS = {
    2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 
    10: 10, 'J': 10, 'Q': 10, 'K': 10, 'AS': 11
}

# Función para repartir una carta aleatoria del mazo
def repartir_carta(mazo_cartas):
    return mazo_cartas.pop(random.randint(0, len(mazo_cartas) - 1))

# Función para iniciar una partida, creando el mazo y repartiendo cartas iniciales
def iniciar_partida():
    # Crear un mazo con 4 copias de cada carta
    mazo_cartas = [carta for carta in VALOR_CARTAS for _ in range(4)]
    # Repartir dos cartas al jugador y dos a la casa
    mano_jugador = [repartir_carta(mazo_cartas), repartir_carta(mazo_cartas)]
    mano_casa = [repartir_carta(mazo_cartas), repartir_carta(mazo_cartas)]
    return mazo_cartas, mano_jugador, mano_casa

# Función para calcular la suma de las cartas en una mano
def suma_cartas(mano):
    suma = sum(VALOR_NUM_CARTAS[carta] for carta in mano)  # Sumar valores de las cartas
    num_ases = mano.count('AS')  # Contar cuántos ases hay en la mano
    
    # Ajustar el valor de los ases si la suma supera 21
    while suma > 21 and num_ases > 0:
        suma -= 10
        num_ases -= 1
    
    return suma

# Función para determinar el ganador entre el jugador y la casa
def determinar_ganador(mano_jugador, mano_casa):
    suma_jugador = suma_cartas(mano_jugador)
    suma_casa = suma_cartas(mano_casa)
    
    # Comparar las sumas y determinar el resultado
    if suma_jugador > 21:
        return "La casa gana (jugador se pasó)"
    if suma_casa > 21:
        return "El jugador gana (casa se pasó)"
    if suma_jugador > suma_casa:
        return "El jugador gana"
    if suma_casa > suma_jugador:
        return "La casa gana"
    return "Empate"

# Función principal para jugar al juego
def jugar():
    while True:
        print("\n--- Nuevo Juego ---")
        print("Presiona 'p' para pedir carta, 's' para plantarte, 'q' para salir")
        
        # Iniciar una nueva partida
        mazo, jugador, casa = iniciar_partida()
        
        # Mostrar las cartas iniciales del jugador y una carta de la casa
        print("\nTus cartas:", jugador, "Suma:", suma_cartas(jugador))
        print("Casa muestra:", [casa[0], "?"])  # Solo muestra una carta de la casa
        
        # Turno del jugador
        while suma_cartas(jugador) <= 21:
            accion = input("\n¿Qué deseas hacer? [p/s/q]: ").lower()
            
            if accion == 'p':  # Pedir carta
                jugador.append(repartir_carta(mazo))
                print("\nTus cartas:", jugador, "Suma:", suma_cartas(jugador))
                if suma_cartas(jugador) > 21:
                    print("¡Te has pasado de 21!")
                    break
            elif accion == 's':  # Plantarse
                break
            elif accion == 'q':  # Salir del juego
                return
            else:  # Opción no válida
                print("Opción no válida. Usa 'p', 's' o 'q'")
        
        # Turno de la casa (solo si el jugador no se pasó)
        if suma_cartas(jugador) <= 21:
            while suma_cartas(casa) < 17:  # La casa pide cartas hasta tener al menos 17
                casa.append(repartir_carta(mazo))
        
        # Mostrar resultados finales
        print("\n--- Resultado Final ---")
        print("Tus cartas:", jugador, "Suma:", suma_cartas(jugador))
        print("Cartas de la casa:", casa, "Suma:", suma_cartas(casa))
        print(determinar_ganador(jugador, casa))

# Ejecutar el juego si el archivo se ejecuta directamente
if __name__ == "__main__":
    jugar()