print("Inicio Sesión en la App")

# Definimos usuarios y contraseñas en un diccionario
usuarios = {
    "admin": "admin123",
    "user1": "user123",
    "user2": "user123",
    "user3": "user123"
}

# Pedir credenciales al usuario
nombre = input("Usuario: ")
contrasena = input("Contraseña: ")

# Verificar si el usuario existe y la contraseña coincide
if nombre in usuarios and usuarios[nombre] == contrasena:
    print("Acceso Aprobado")
else:
    print("Acceso Denegado")

print("Fin")