def xnor(a, b):
    return not (a ^ b)  # XOR con ^, luego negamos

# Pruebas
print(xnor(0, 0))  # True
print(xnor(0, 1))  # False
print(xnor(1, 0))  # False
print(xnor(1, 1))  # Tru