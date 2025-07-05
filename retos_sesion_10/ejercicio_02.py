ropa_deportiva = ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
ropa_formal = ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]
set_deportiva = set(ropa_deportiva)
set_formal = set(ropa_formal)
tienda_nueva = set_deportiva.union(set_formal)
print("Prendas combinadas para la nueva tienda:")
print(tienda_nueva)