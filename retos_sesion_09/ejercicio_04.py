#parte 1
productos = ["Bon Bon Bum", "Oreo", "Chizitos", "Sublime", "Princesa"]
precios = [0.5, 1.2, 0.8, 1.5, 1.0]

print("Productos:")
print(productos)
print("Precios:")
print(precios)

print("Agregar 2 productos nuevos al final")
productos.append("Snickers")
precios.append(1.8)

productos.append("Galleta Chin Chin")
precios.append(0.7)

print(productos)
print(precios)

print("Eliminar 'Bon Bon Bum' de las listas")
indice = productos.index("Bon Bon Bum")
productos.pop(indice)
precios.pop(indice)

print(productos)
print(precios)

print("¿Cuánto cuesta 'Oreo' y 'Chizitos'?")
indice_oreo = productos.index("Oreo")
print("Oreo cuesta:", precios[indice_oreo])

indice_chizitos = productos.index("Chizitos")
print("Chizitos cuesta:", precios[indice_chizitos])

print("Producto más caro y más barato")
precio_max = max(precios)
indice_max = precios.index(precio_max)
print("Más caro:", productos[indice_max], "->", precio_max)

precio_min = min(precios)
indice_min = precios.index(precio_min)
print("Más barato:", productos[indice_min], "->", precio_min)

#parte 2
productos = ["Oreo", "Chizitos", "Sublime", "Princesa", "Snickers", "Galleta Chin Chin"]
precios = [1.2, 0.8, 1.5, 1.0, 1.8, 0.7]

print("Productos:")
print(productos)
print("Precios:")
print(precios)

print("¿Cuántos productos tienes en total?")
print(len(productos))

print("¿Cuánto cuestan todos los productos?")
print(sum(precios))

print("Ordenar productos y precios del más barato al más caro")

ordenado = sorted(zip(precios, productos))

precios_ordenados = [precio for precio, producto in ordenado]
productos_ordenados = [producto for precio, producto in ordenado]

print("Productos ordenados:")
print(productos_ordenados)
print("Precios ordenados:")
print(precios_ordenados)

print("Eliminar todos los productos de las listas")
productos.clear()
precios.clear()

print("Productos:")
print(productos)
print("Precios:")
print(precios)