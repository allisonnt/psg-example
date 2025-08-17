print("Inicio Descuento Tienda")

edad = int(input("Ingrese su edad: "))
compra = float(input("Ingrese el monto de su compra: "))

if edad > 60 and compra > 1000:
    print("Se aplica un descuento del 20%")
elif edad >= 18 and edad <= 60 and compra > 500:
    print("Se aplica un descuento del 10%")
else:
    print("Se aplica un descuento del 2%")

print("Fin")