vocales = ["a", "e", "i", "o", "u"]
frase = "Hola, estoy aprendiendo python"
encontradas = 0

for letra in frase:
    if letra in vocales:
        encontradas +=1
        print(f"He encontrado una {letra} ")

print(f"Vocales encontradas: {encontradas}")
