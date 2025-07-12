arca = {
    "🐶": 2,  
    "🐱": 2, 
    "🐯": 2,  
    "🐵": 2,  
    "🦄": 0,  
    "🦒": 1   
}

print("Arca inicial:", arca)

arca.update({
    "🦓": 2, 
    "🐘": 2,  
    "🦜": 2   
})

print("\nArca después de agregar 3 especies más:", arca)

animal_list = []

for animal, count in arca.items():
    animal_list.extend([animal] * count)

print("\nLista de animales en el arca:", animal_list)


dragon_exists = "🐲" in arca
print("\n¿Existe el dragón 🐲 en el arca?", dragon_exists)


arca.pop("🦄", None) 

print("\nArca después de eliminar el unicornio 🦄:", arca)

arca["🦒"] = 2

print("\nArca después de actualizar la jirafa 🦒 cuenta hasta 2:", arca)

arca.clear()

print("\nArca después del diluvio (debe estar vacía):", arca)