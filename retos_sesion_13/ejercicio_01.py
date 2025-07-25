print("Ejercicio 1: Sucesión de Lucas")

lucas = [2, 1]  # valores iniciales

for i in range(2, 20):
    siguiente = lucas[i - 1] + lucas[i - 2]
    lucas.append(siguiente)

for numero in lucas:
    print(numero, end=" ")