libro = {"titulo": "Harry Potter y la orden del Fenix","autor": "J.K. Rowling", "copias": 1}

titulo_buscado = "Harry Potter y la orden del Fenix"
autor_buscado = "J.K. Rowling"

if libro["titulo"] == titulo_buscado and libro["autor"] == autor_buscado:
    if libro["copias"] > 0:
        print("Pepito puede sacar el libro")
    else:
        print("No hay copias disponibles")
else:
    print("El libro no se encuentra en la biblioteca")










