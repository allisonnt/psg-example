
lista = ["Ana", "Luis", "Carlos", "José", "Elena", "Marta", "Pedro", "Lucía", "José", "Nadia"]
print(lista)

print("Sublista de índice 5 al 9 con paso 2 en 2")
sub_lista = lista[5:10:2]
print(sub_lista)
print(type(sub_lista))

print("¿Existe el nombre 'José' en la lista?")
print("José" in lista)

print("Sublista ordenada alfabéticamente A-Z")
sub_lista.sort()
print(sub_lista)

print("Lista original ordenada alfabéticamente descendente Z-A")
lista.sort(reverse=True)
print(lista)