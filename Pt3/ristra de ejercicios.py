#1 la string más larga: introducir una cantidad de string y este va a devolver el string mas largo
def larguita(*args):
    if args:
        larga = [""]
        for cadena in args:
            if len(cadena) > len(larga[0]):
                larga.pop(0)
                larga.append(cadena)
            elif len(cadena) < len(larga[0]):
                pass
        print(larga)

#2 Sumando a la lista: crear una funcion que sume un conjunto de numeros

def suma (*args):
    if args:
        suma = 0
        for a in args:
            suma += a
        print(suma)


larguita("junya","watanabi")

# par o impar

def es_impar(numero):
    if numero % 2 == 0:
        print(False)
    else:
        print(True)

es_impar(2)
es_impar(3)