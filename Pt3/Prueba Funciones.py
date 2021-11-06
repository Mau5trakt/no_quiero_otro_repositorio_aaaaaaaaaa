def medir_largo(iterable, *args, sumar_todo=False):
    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        if sumar_todo:
            largos = sum(largos)
        return largos
    return len(iterable)

def main():
    valor = input("Ingrese un texto")
    print(medir_largo(valor, sumar_todo=True))

if __name__ == "__main__":
    main()