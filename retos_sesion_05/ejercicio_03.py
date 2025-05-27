# Total de segundos
total_segundos = 1_000_000

# Cálculos
semanas = total_segundos // (7 * 24 * 60 * 60)
resto = total_segundos % (7 * 24 * 60 * 60)

dias = resto // (24 * 60 * 60)
resto %= (24 * 60 * 60)

horas = resto // (60 * 60)
resto %= (60 * 60)

minutos = resto // 60
segundos = resto % 60

# Mostrar resultados
print("Equivalente a:")
print(f"{semanas} semana(s)")
print(f"{dias} día(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")