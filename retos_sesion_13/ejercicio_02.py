print("Ejercicio 2: Primeros 20 múltiplos de 2 y 5")

numeros = []
i = 1

while len(numeros) < 20:
    if i % 10 == 0:
        numeros.append(i)
    i += 1

for numero in numeros:
    print(numero, end=" ")