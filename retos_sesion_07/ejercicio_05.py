texto = input("Ingresa una frase: ")
texto_normalizado = texto.lower().replace(" ", "")
es_palindromo = texto_normalizado == texto_normalizado[::-1]
print("¿Es un palíndromo?", es_palindromo)