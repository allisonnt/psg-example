a = True
b = True
resultado = (a or b) and not (a and b)
print(a, "   |", b, "   |", resultado)

a = True
b = False
resultado = (a or b) and not (a and b)
print(a, "   |", b, "  |", resultado)

a = False
b = True
resultado = (a or b) and not (a and b)
print(a, "  |", b, "   |", resultado)

a = False
b = False
resultado = (a or b) and not (a and b)
print(a, "  |", b, "  |", resultado)