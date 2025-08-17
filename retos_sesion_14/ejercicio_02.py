def calcular(numero1, numero2, operacion):
    if operacion == "+":
        return numero1 + numero2
    elif operacion == "-":
        return numero1 - numero2
    elif operacion == "*":
        return numero1 * numero2
    elif operacion == "/":
        if numero2 == 0:
            return "Error: División entre 0"
        else:
            return numero1 / numero2
    else:
        return "Operación no válida"
    
    

