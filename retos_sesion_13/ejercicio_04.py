print("Ejercicio 4")
while True:
    frase = input("Ingrese una frase: ")
    if "salir" in frase:
        break
    # Convertir todo a minúsculas y quitar espacios para comparar
    frase_limpia = frase.replace(" ", "").lower()
    print("Palíndromo" if frase_limpia == frase_limpia[::-1] else "No es palíndromo")
print("Fin")