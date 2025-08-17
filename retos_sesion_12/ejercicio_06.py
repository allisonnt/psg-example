print("Inicio Calculadora")

# Pedir entrada al usuario
entrada = input("Operación (numero1, numero2, operación): ")

# Separar los datos usando coma
datos = entrada.split(",")  # ['10', '5', '+']

if len(datos) == 3:  # Validar que ingresó 3 elementos
    num1 = float(datos[0].strip())
    num2 = float(datos[1].strip())
    operacion = datos[2].strip()

    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2:  # truthiness para evitar división por 0
            resultado = num1 / num2
        else:
            resultado = "Error: División entre 0"
    else:
        resultado = "Operación inválida"

    print("Resultado:", resultado)
else:
    print("Entrada incorrecta, debe tener formato: numero1, numero2, operación")

print("Fin")