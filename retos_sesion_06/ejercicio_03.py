print("Tarjeta | Huella | Puerta se abre")
print("-------------------------------")

for tarjeta in [0, 1]:
    for huella in [0, 1]:
        abrir = tarjeta ^ huella  # XOR lógico
        print(f"   {tarjeta}     |   {huella}    |       {abrir}")