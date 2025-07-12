alimentos = {
    "carne": ["gato", "perro"],
    "zanahoria": ["conejo"]
}
print(alimentos)

alimentos.update(pescado=["gato", "perro"])
alimentos.update(hueso=["perro"])
alimentos.update(lechuga=["conejo", "cuy"])
alimentos.update(maíz=["gallina", "cuy"])
print("Después de añadir más alimentos:")
print(alimentos)

print("¿Existe la comida 'trigo'?")
existe_trigo = 'trigo' in alimentos
print(existe_trigo)

print("Eliminar 'zanahoria'")
del alimentos['zanahoria']
print(alimentos)