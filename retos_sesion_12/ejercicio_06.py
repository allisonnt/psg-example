print("Inicio calculadora básica")

numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))
operacion = input("Operación: ")

print("-------------")

if operacion == "+":
    resultado = numero1 + numero2
    if resultado == int(resultado):
        print("Resultado:", int(resultado))
    else:
        print("Resultado:", resultado)
elif operacion == "-":
    resultado = numero1 - numero2
    if resultado == int(resultado):
        print("Resultado:", int(resultado))
    else:
        print("Resultado:", resultado)
elif operacion == "*":
    resultado = numero1 * numero2
    if resultado == int(resultado):
        print("Resultado:", int(resultado))
    else:
        print("Resultado:", resultado)
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        if resultado == int(resultado):
            print("Resultado:", int(resultado))
        else:
            print("Resultado:", resultado)
    else:
        print("Error: No se puede dividir entre cero")
else:
    print("Operación no válida")

print("Fin")