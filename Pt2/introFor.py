a = [1,2,3,4,5,6,7,8,9]
for item in a:
    print(item)

lista_de_la_compra = ["Leche","Pollo","Arroz"]
for objeto in lista_de_la_compra:
    print(f"Hoy voy a comprar {objeto}")

vocales = ["a","e",'i','o','u']
frase = "hola, hoy estoy aprendiendo python"
vocales_encontradas = 0


for letra in frase:
    if letra in vocales:
        vocales_encontradas =+ 1

print(f"se han encontrado {vocales_encontradas} vocales")