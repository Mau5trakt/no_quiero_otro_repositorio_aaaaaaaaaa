"""donda = ""
while donda != "salir":
    donda = input("Escriba algo[salir para salir]")"""

productos = ["leche", "pollo", "gaseosa", "detergente", "galleta", "atun", "pasta", "paleta", "galleta","lista"]
milista = []
introducir = ""
while introducir != "salir":
    introducir = input("Ingrese lo que quiera añadir a la lista:")
    if introducir not in productos:
        print("No se encuentra en la lista")
    elif introducir == "lista":
        print("\n".join(productos))
    else:
        milista.append(introducir)


print("-\n".join(milista))