def introducir_producto():
    productos = ["leche", "pollo", "gaseosa", "detergente", "galleta", "atun", "pasta", "paleta", "galleta","lista"]
    milista =[]
    introducir = ""
    while introducir != "salir":
        introducir= input("Ingrese lo que desea comprar".lower())
        if introducir not in productos:
            print("No se encuentra en la lista escriba [Lista] para ver los productos disponibles")
        elif introducir == "lista":
            print(productos)
            introducir = ""
        else:
            milista.append(introducir)
            print("\n".join(milista))

    print(f"tu lista de compras es:{milista}")

def main():
    introducir_producto()

if __name__ == "__main__":
    main()