for fila in range(8):
    linea = ""
    for columna in range(8):
        if (fila + columna) % 2 == 0:
            linea = linea + "#"
        else:
            linea = linea + "*"
    print(linea)