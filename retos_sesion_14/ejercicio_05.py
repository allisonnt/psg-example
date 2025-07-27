def contar_vocales(cadena):
    contador = 0
    for letra in cadena:
        if letra in "aeiouAEIOU":
            contador = contador + 1
    return contador

# Llamar función
resultado = contar_vocales("Python es un lenguaje de programación")
print(resultado)