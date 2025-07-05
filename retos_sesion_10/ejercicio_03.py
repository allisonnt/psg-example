tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]
set_fisica = set(tienda_fisica)
set_online = set(tienda_online)
ambos_canales = set_fisica.intersection(set_online)
solo_fisica = set_fisica.difference(set_online)
solo_online = set_online.difference(set_fisica)
print("Clientes que compraron en ambos canales:", ambos_canales)
print("Clientes que compraron solo en tienda física:", solo_fisica)
print("Clientes que compraron solo online:", solo_online)