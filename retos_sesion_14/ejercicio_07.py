tablero = [[" " for i in range(3)] for j in range(3)]
turno = "X"

while True:
    print("Juega", turno)
    fila = int(input("Fila 0-2: "))
    columna = int(input("Columna 0-2: "))
    
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = turno
    else:
        print("Casilla ocupada")
        continue
    
    # Mostrar tablero
    for fila_tablero in tablero:
        print(fila_tablero)
    
    # Revisar ganador simple
    if (tablero[0][0] == tablero[0][1] == tablero[0][2] != " " or
        tablero[1][0] == tablero[1][1] == tablero[1][2] != " " or
        tablero[2][0] == tablero[2][1] == tablero[2][2] != " " or
        tablero[0][0] == tablero[1][0] == tablero[2][0] != " " or
        tablero[0][1] == tablero[1][1] == tablero[2][1] != " " or
        tablero[0][2] == tablero[1][2] == tablero[2][2] != " " or
        tablero[0][0] == tablero[1][1] == tablero[2][2] != " " or
        tablero[0][2] == tablero[1][1] == tablero[2][0] != " "):
        print("¡Gana", turno, "!")
        break
    
    # Cambiar turno
    if turno == "X":
        turno = "O"
    else:
        turno = "X"

        