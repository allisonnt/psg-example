arca = {"🐶": 2, "🐱": 2, "🐯": 2, "🐵": 2, "🦄": 0, "🦒": 1}

arca.update({"🦊": 2, "🐸": 2, "🦅": 2})

print("Animales en el arca:")
for especie, cantidad in arca.items():
    print(f"{especie}: {cantidad}")

if "🐲" in arca:
    print("El dragón 🐲 está en el arca.")
else:
    print("El dragón 🐲 NO está en el arca.")

arca.pop("🦄", None)  

arca["🦒"] = 2

for clave in list(iter(arca.keys())):  # se usa list() porque no se puede modificar directo al iterar
    arca.pop(clave)

print("El arca después del diluvio:", arca)