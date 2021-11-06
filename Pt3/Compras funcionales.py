
SALIDA = "SALIR"

def preguntar_usuario():
    return input(f"Introduce un producto, [{SALIDA}] para salir ")


def main():
    lista_compra = []

    input_usuario = preguntar_usuario()

    while input_usuario != SALIDA:
        lista_compra.append(input_usuario)
        print("\n".join(lista_compra))
        input_usuario = preguntar_usuario()



    #savefile = guardar()
    #guardar = open("compra.txt", "w")
    #guardar.write("\n".join(lista_compra))
    #guardar.close()


if __name__ == "__main__":
    main()