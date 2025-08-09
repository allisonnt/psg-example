print("\n🏧 Inicio Cajero Automático")

class FondosInsuficientesError(Exception):
    pass

saldo = 500  # saldo disponible

while True:
    try:
        monto = input("Ingrese monto a retirar: ")
        if monto == "salir":
            break
        monto = float(monto)

        if monto > saldo:
            raise FondosInsuficientesError("Fondos insuficientes")
        if monto > 1000:
            raise Exception("Monto excede el límite por transacción")

        saldo -= monto
        print("💰 Retiro exitoso. Saldo restante:", saldo)

    except FondosInsuficientesError as e:
        print("🚫 Error:", e)
    except ValueError:
        print("🔢 Error: Ingrese solo números")
    except Exception as e:
        print("💀 Error:", e)
    finally:
        print("Saldo actual:", saldo)

print("🏧 Fin Cajero Automático")