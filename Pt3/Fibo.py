def fibo(numero):
    secuencia = [0,1]
    contador = 2
    for i in range (numero):
        h = secuencia[contador -2] + secuencia[contador-1]
        secuencia.append(h)
        contador +=1
    print(secuencia[-1])
    return

def main():
    fibo(14)


if __name__ == "__main__":
    main()