
respuesta = ""
while respuesta not in ["A","B","C"]:

    respuesta = input("¿Qué opción prefieres?[A,B,C]\n")

    if respuesta == 'A':
        print("Has Elegido bien.")
    elif respuesta == 'B':
        print("Podrías haber elegido algo mejor.")
    elif respuesta == 'C':
        print("Respuesta equivocada.")
    else:
        print("No se ha dado una respuesta con sentido :/")