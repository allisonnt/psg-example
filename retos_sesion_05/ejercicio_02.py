# EJERCICIO 02
# Lista de temperaturas en Fahrenheit
temperaturas_f = [25, 300, 76]

# Convertir y mostrar cada temperatura
for f in temperaturas_f:
    c = (f - 32) * 5 / 9
    print(f"{f}°F = {c:.2f}°C")
    