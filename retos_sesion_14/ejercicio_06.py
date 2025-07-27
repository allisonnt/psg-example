def separar_pares_impares(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

# Llamar función
lista = [10, 5, 20, 15, 25, 30]
pares, impares = separar_pares_impares(lista)
print("Pares:", pares)
print("Impares:", impares)