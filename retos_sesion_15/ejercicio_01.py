print("📟 Inicio Calculadora")
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b

while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1 == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2 == "salir":
            break

        num1 = float(num1)
        num2 = float(num2)

        print("➕ Suma:", sumar(num1, num2))
        print("➖ Resta:", restar(num1, num2))
        print("✖️ Multiplicación:", multiplicar(num1, num2))
        print("➗ División:", dividir(num1, num2))

    except ZeroDivisionError as e:
        print("0️⃣ Error:", e)
    except ValueError as e:
        print("🔢 Error: Debe ingresar solo números")
    except Exception as e:
        print("💀 Error inesperado:", e)
print("📟 Fin Calculadora")