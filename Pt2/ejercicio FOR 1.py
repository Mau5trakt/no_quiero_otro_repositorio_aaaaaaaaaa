texto_usuario = input("Introduzca un texto")
espacios = 0
puntos = 0
comas = 0
for texto in texto_usuario:
    if texto == " ":
        espacios +=1
    elif texto == ".":
        puntos +=1
    elif texto ==",":
        comas +=1

print(f"espacios: {espacios}\n puntos: {puntos} \n comas: {comas}")
