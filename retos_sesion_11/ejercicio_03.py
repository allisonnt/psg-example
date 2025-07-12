tupla = (('canino', '🐶'), ('felino', '🐱'), ('aves', ['🐦', '🦅']))
diccionario = dict(tupla)
print(diccionario)

print("Eliminar clave 'aves'")
aves = diccionario.pop('aves')
print("Valor eliminado:", aves)
print(diccionario)

print("Modificar valor de 'felino'")
diccionario['felino'] = '🐈'
print(diccionario)

print("Cambiar la clave 'canino' por 'caninos' y su valor")
diccionario['caninos'] = ['🐶','🐕']
del diccionario['canino']
print(diccionario)