#pedir el nombre y saludar
def adquirenombre():
    name = input("Introduzca su nombre: \n")
    return name

def saludar(name):
    print(f"Hola, {name}")


def main():
    print("Hello Bozzo")
    name = adquirenombre()
    saludar(name)

if __name__ == "__main__":
    main()