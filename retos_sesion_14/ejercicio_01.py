def promedio(calificaciones):
    suma = 0
    cantidad = 0
    for nota in calificaciones:
        suma = suma + nota
        cantidad = cantidad + 1
    promedio = suma / cantidad
    return promedio

# Llamar función
notas = [50, 75, 80, 91, 70]
resultado = promedio(notas)
print(resultado)