tablero = [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(fila)

def verificar_ganador(jugador):

    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def tablero_lleno():
    for fila in tablero:
        for casilla in fila:
            if casilla == " ":
                return False
    return True

def tres_en_raya():
    jugador = "X"
    while True:
        print("Turno de:", jugador)
        mostrar_tablero()
        
        fila = int(input("Ingresa fila (0-2): "))
        columna = int(input("Ingresa columna (0-2): "))
        
        if tablero[fila][columna] != " ":
            print("Casilla ocupada. Intenta otra vez.")
            continue
        
        tablero[fila][columna] = jugador
        
        if verificar_ganador(jugador):
            mostrar_tablero()
            print("¡Ganó el jugador:", jugador, "!")
            break
        
        if tablero_lleno():
            mostrar_tablero()
            print("¡Empate!")
            break
        
        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

tres_en_raya()