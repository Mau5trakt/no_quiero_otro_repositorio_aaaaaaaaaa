#Tabla de multiplicar

numero = int(input("Introduzca el numero de la tabla que quiere saber"))

for resultado in range(1,13):
    tabla = f"{numero} * {resultado} = {resultado * numero}"
    if resultado % 2 == 0:
        print(f"|{numero} * {resultado} = {resultado * numero} |")
    #print(f"|{numero} * {resultado} = {resultado * numero } |" )