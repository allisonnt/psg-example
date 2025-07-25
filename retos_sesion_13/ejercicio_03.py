print("Ejercicio 3: Felicitaciones a los aprobados")

estudiantes = [('Miguel', 51), ('Daniel', 80), ('Virginia', 90), ('Franco', 40), ('Flabio', 30)]

for estudiante in estudiantes:
    if estudiante[1] >= 51:
        print(f"¡Felicidades {estudiante[0]}! Aprobaste con {estudiante[1]}")