# EJEMPLO 1
frase = "   Mario Benedetti   "
limpia = frase.strip()
print("Con .strip():", limpia)

# EJEMPLO 2
poema = "el sur también existe"
titulo = poema.title()
print("Con .title():", titulo)

# EJEMPLO 3
texto = "Te espero donde siempre"
posicion = texto.find("donde")
print("Con .find():", posicion)

# EJEMPLO 4
palabra = "poesia"
print("Con .isalpha():", palabra.isalpha())

# EJEMPLO 5
frase = "cuando el corazón habla, la razón calla"
palabras = frase.split()
print("Con .split():", palabras)