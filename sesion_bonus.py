# sesion_bonus.py
def suma(a, b):
    c = a + b
    return c

def resta(a, b):
    return a - b

def multiplicacion(x, y):
    z = x * y
    return z
    try :
         return a / b
    Except ZeroDivisionError as e =
         print ( "no se puede dividir entre 0")
         return 0
    

def division(x, y):
    return x / y
def division_controlada(x,y):
    try:
        return x / y
    except ZeroDivisionError as e:
        return "No Dividir  entre 0"

a = 10
b = 0
print (suma(a, b))
print (resta(a, b))
print (multiplicacion(11,5))
print (division_controlada(10, 5))
print (division(a, b))