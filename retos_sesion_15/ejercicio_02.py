print("\n🍎 Inicio Canasta de Frutas")

class FrutaInvalidaError(Exception):
    pass

frutas_permitidas = ['🍅', '🍇', '🍈', '🍉', '🍊', '🍌', '🍍', '🍑']
canasta = []

while True:
    try:
        fruta = input("Ingrese una fruta: ")
        if fruta == "salir":
            break
        if fruta not in frutas_permitidas:
            raise FrutaInvalidaError("Fruta no permitida")
        canasta.append(fruta)
    except FrutaInvalidaError as e:
        print("🚫 Error:", e)
    except Exception as e:
        print("💀 Error inesperado:", e)
    else:
        print("🎉 Fruta agregada")
    finally:
        print("Canasta actual:", canasta)

print("🍎 Fin Canasta de Frutas")