import string
mayus = string.ascii_uppercase
texto = input("Itroduzca un texto")
mayuscula = 0

for letra in texto:
    if letra in mayus:
        mayuscula += 1

print(f"mayusculas: {mayuscula}")