print("Inicio cálculo de descuento")

edad = int(input("Ingrese la edad del cliente: "))
compra = float(input("Ingrese el monto de la compra: "))

if edad >= 18 and compra > 1000:
    descuento = 10
elif edad < 18 and compra > 500:
    descuento = 5
else:
    descuento = 2

print("Descuento aplicado:", descuento, "%")

print("Fin")