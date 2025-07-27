def calcular(numero1, numero2, operacion):
    if operacion == "+":
        return numero1 + numero2
    elif operacion == "-":
        return numero1 - numero2
    elif operacion == "*":
        return numero1 * numero2
    elif operacion == "/":
        return numero1 / numero2
    else:
        return "Operación no válida"

# Llamar función
resultado = calcular(10, 5, "+")
print(resultado)