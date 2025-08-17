frutas = ['🍅','🍇','🍈','🍉','🍊','🍌','🍍','🍌','🍊','🍉','🍈','🍇','🍅','🍅','🍇']

# Función para contar las frutas
def contar_frutas(lista_frutas):
    contador = {}
    for fruta in lista_frutas:
        if fruta in contador:
            contador[fruta] += 1
        else:
            contador[fruta] = 1  # inicia en 1, no en 0
    return contador

# Función para imprimir el conteo de frutas
def imprimir_conteo(conteo):
    for fruta, cantidad in conteo.items():  # .items() para obtener (clave, valor)
        sufijo = "" if cantidad == 1 else "s"
        print(f"Hay {cantidad} {fruta}{sufijo}.")

# Llamando a las funciones
conteo_frutas = contar_frutas(frutas)
imprimir_conteo(conteo_frutas)