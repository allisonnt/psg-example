habitats = {
    "polo norte": {
        "especies": {"oso polar", "morsa", "ballena"}
    },
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"}
    }
}
print(habitats)

habitats.update(desierto={"especies": {"camello", "fennec"}})
habitats.update(sabana={"especies": {"elefante", "león"}})
print("Después de añadir hábitats:")
print(habitats)

print("¿Existe el hábitat 'amazonas'?")
existe_amazonas = 'amazonas' in habitats
print(existe_amazonas)

especies_amazonas = habitats["amazonas"]["especies"]
nuevo_conjunto = set(especies_amazonas)  
nuevo_conjunto = nuevo_conjunto.union({"anaconda"})  

habitats["amazonas"]["especies"] = nuevo_conjunto

print("Amazonas actualizado con anaconda:")
print(habitats["amazonas"])