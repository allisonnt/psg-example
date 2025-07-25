print("Ejercicio 4: Verificador de palíndromos")
while True:
    frase = input("Ingrese una frase: ")
    if "salir" in frase:
        break
    invertida = ""
    for letra in frase:
        invertida = letra + invertida  # construimos la frase invertida al inicio
    if frase == invertida:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
print("Fin del programa")