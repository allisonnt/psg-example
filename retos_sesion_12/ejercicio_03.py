print("Inicio Colección de Autos")

# Colección de Jhon
autos_jhon = {"Ferrari", "Lamborghini", "Porsche", "Bugatti", "McLaren"}

# Colección de Jess
autos_jess = {"Ferrari", "Lamborghini", "Tesla", "Ford", "Chevrolet"}

print("Autos de Jhon:", autos_jhon)
print("Autos de Jess:", autos_jess)

# Autos en común (intersección de conjuntos)
autos_comunes = autos_jhon & autos_jess  # operador "&" es válido en conjuntos

if autos_comunes:  # si el conjunto no está vacío
    print("Autos en común:", autos_comunes)
else:
    print("No tienen autos en común")

print("Fin")