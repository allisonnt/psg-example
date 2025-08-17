print("Inicio Sesión")

usuarios = {
    "admin": "admin123",
    "user1": "user123",
    "user2": "user123",
    "user3": "user123"
}

usuario = input("Usuario: ")
contraseña = input("Contraseña: ")

if usuario in usuarios:               
    if usuarios[usuario] == contraseña:
        print("Acceso permitido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no existe")

print("Fin")