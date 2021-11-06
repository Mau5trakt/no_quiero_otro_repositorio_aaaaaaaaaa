def potencia(base, *exponente):
    if exponente:
        numero = 2 ** exponente
        return numero
    else:
        a = base ** 2
        return a

def main():
    print(potencia(25))
    print(potencia (2, 8))


if __name__ == "__main__":
    main()