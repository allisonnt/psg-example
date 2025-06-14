texto = input("Escribe tu pregunta (solo palabras, sin signos): ")
pregunta = tuple(texto)
pregunta_con_signos = ('¿', ) + pregunta + ('?', )
print("Pregunta como tupla:", pregunta_con_signos)
pregunta_repetida = pregunta_con_signos * 2
print("Pregunta repetida:", pregunta_repetida)