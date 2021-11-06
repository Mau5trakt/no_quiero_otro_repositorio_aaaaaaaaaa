def texto():
    escribir = []
    item = ""
    while item != "SALIR":
        item = input("Ingrese un producto para añadir a la lista, SALIR para salir: ")
        if item != "SALIR":
            escribir.append(item)
            print("\n".join(escribir))
        else:
            break
    return escribir

def guardar(escribir):
    b = input("Escriba el nombre con el que quiere guardar el archivo")
    with open(b+".txt", "w") as mi_archivo:
        mi_archivo.write("\n".join(escribir))

def main():
    escribir = texto()
    escribir = str(escribir)
    guardar(escribir)




if __name__ == "__main__":
    main()