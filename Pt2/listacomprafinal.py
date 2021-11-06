listac = []

item = None
print("Programa Lista de la compra\n")

while True:
    item= input("Qué desea comprar? [Q] para salir")
    if item == "Q":
        break
    elif item in listac:
        print(f"{item} ya se encuentra en la lista de la compra")
    else:
        if input(f"Desea añadir {item} a la lista de la compra (S/N)") == "S":
            listac.append(item)

print("La lista de la compra es: {}".format(listac))
