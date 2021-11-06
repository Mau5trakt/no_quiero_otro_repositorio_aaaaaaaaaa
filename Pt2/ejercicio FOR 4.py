lista = []
numero = ""
suma = 0
while numero != "Q":
    numero = input("Introduzca un numero(Q para salir)")
    if numero.isnumeric() == True:
        numero = int(numero)
        lista.append(numero)
        suma += numero

print(f"el numero menor es: {min(lista)} y el numero mayor es: {max(lista)}, la suma es {suma} y el promedio es {suma/len(lista)}")
