a = True
b = True
xnor = (a and b) or (not a and not b)
print("True xnor True =", xnor)

a = True
b = False
xnor = (a and b) or (not a and not b)
print("True xnor False =", xnor)

a = False
b = True
xnor = (a and b) or (not a and not b)
print("False xnor True =", xnor)

a = False
b = False
xnor = (a and b) or (not a and not b)
print("False xnor False =", xnor)