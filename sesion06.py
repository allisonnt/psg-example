print ("Tipos de datos booleanos")
print (True)
print (False)
#Operaciones aritmeticas con booleanos
print (True + True)
print (True * True)
print (True * False)
print (True + False)
print (False * False)

print ("Numeros y booleanos")
print (10 + True)
print (10 + False)
print (10 * True)
print (10 * False)

print ("Declarar variables booleanas")
var_booleana = True
print (var_booleana)
print (type(var_booleana))
var_booleana = False
print (var_booleana)
print (type(var_booleana))

print ("Declarar variables booleanas")
var_booleana = bool(1)
print (var_booleana)
print (type(var_booleana))
var_booleana = bool(0)
print (var_booleana)
print (type(var_booleana))
var_booleana = bool(-15)
print (var_booleana)
print (type(var_booleana))

print ("Operadores de comparacion")
print (10 == 10)
print (10 != 10)
print (10 < 10)
print (10 > 10)
print (10 <= 10)
print (10 >= 10)
a = 10
b = 10
print (a is b)
print (a is not b)

print ("Asignacion de variables")
x = 10
mayor_que_cero = x > 0
print (mayor_que_cero)
diferente_de_10 = x != 10
print (diferente_de_10)
print (type(diferente_de_10))

print ("Operaciones logicos")
print (True and True)
print (True and False)
print (False or True)
print (False or False)
print (not True)
print (not False)


print ("Operaciones logicos y prioridad")
print (False and False or True)
print (False and (False or True))
print (not True  and False or True)
print (not (True and False or False))
print (not True and (False or False))
print (not True and False or False)

print ("Operador AND")
print (True and True)
print (True and False)
print (False and True)
print (False and False)

print ("Operador OR")
print (True or True)
print (True or False)
print (False or True)
print (False or False)

print ("Operador NOT")
print (not True)
print (not False)

print ("Operador NAND")
print (not (True  and True))
print (not (True and False))
print (not (False or False))
print (not (False or False))

print ("Operador NOR")
print (not (True  or True))
print (not (True or False))
print (not (False or True))
print (not (False or False))

print ("Operador XOR")
a = True
b = False
print ((a or b) and not (a and b))
a = True
b = True
print ((a or b) and not (a and b))


print ("Ejemplo de uso Sensor y Bateria")
sensor = True
bateria = True
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = True
bateria = False
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = True
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = False
print (sensor, "and", bateria, "=", sensor and bateria)

# EJEMPLO 1
x = 20
print (x >= 0 and x <= 100)

# EJEMPLO 2
nota_1 = 15
nota_2 = 20
nota_3 = 16
nota_aprobacion = 50
print (nota_1 + nota_2 + nota_3 > nota_aprobacion)

# Ejemplo 3
numero = 15
divisor_1 = 3
divisor_2 = 5
divisor_3 = 2
print (numero % divisor_1 == 0 and numero % divisor_2 == 0 and not (numero % divisor_3 ==0))

print ("Cortocircuito con operador and")
x = 1
y = 0
print (x > 2 and (x/y) > 2)
print (x > 0 and (x/y) > 0)


