print("Inicio verificación de nombre y gustos musicales")

nombre = input("Ingrese su nombre: ")
gustos = input("Ingrese sus gustos musicales separados por coma: ")

if nombre:
    print("Nombre:", nombre)
else:
    print("Nombre no válido")

# Convertir gustos en lista
lista_gustos = gustos.split(",")

# Limpiar espacios en cada gusto
for i in range(len(lista_gustos)):
    lista_gustos[i] = lista_gustos[i].strip()

print("Gustos musicales:", ",".join(lista_gustos))

if 'rock' in lista_gustos:
    print("Tiene gusto por el rock")
else:
    print("No tiene gusto por el rock")

print("Fin")