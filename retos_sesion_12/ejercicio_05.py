print("Inicio Gestión de Contactos")

contactos = []

nombre = input("Nombre: ")
telefono = input("Teléfono: ")

if nombre and len(telefono) == 12:  
    contactos.append({"Nombre": nombre, "Teléfono": telefono})
    print("Contacto guardado")
else:
    print("Datos incorrectos")

print("Lista de contactos:", contactos)
print("Fin")