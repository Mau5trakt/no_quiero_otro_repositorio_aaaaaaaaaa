import random
import os
VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 95
SIZE_BARRA_DE_VIDA = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE
while vida_squirtle and vida_pikachu >0:
    #Inicia el combate

    #Turno de pikachu
    print('Turno de Pikachu')
    ataque_pikachu = random.randint(1, 2)
    if ataque_pikachu== 1:
        #Bola Voltio
        print('Pikachu ataca con Bola Voltio')
        vida_squirtle -=10

    elif ataque_pikachu== 2:
        print('Pikachu ataca con Onda Trueno')
        vida_squirtle -=11

    barras_de_vida_pikachu = vida_pikachu * SIZE_BARRA_DE_VIDA /VIDA_INICIAL_PIKACHU
    print(f'Pikachu [{"*"* int(barras_de_vida_pikachu)}{" " * int((10 - barras_de_vida_pikachu))}]({vida_pikachu}/{VIDA_INICIAL_PIKACHU})')

    barras_de_vida_squirtle = vida_squirtle * SIZE_BARRA_DE_VIDA / VIDA_INICIAL_SQUIRTLE
    print(f'Squirtle [{"*" * int(barras_de_vida_squirtle)}{" " * int((SIZE_BARRA_DE_VIDA - barras_de_vida_squirtle))}]({vida_squirtle}/{VIDA_INICIAL_SQUIRTLE})')
    input('Enter para continuar...\n\n')
    os.system('cls')

#Turno Squirtle
    print('Turno Squirtle')
    ataque_squirtle = ''
    while ataque_squirtle not in ['P','B','A','N']:
        ataque_squirtle = input('Que ataque deseas realizar? [P]lacaje, [B]urbuja, Pistola[A]gua:, Hacer [N]ada' ).upper()
        if ataque_squirtle == 'P':
            print('Squirtle ataca con Placaje')
            vida_pikachu -=10
        elif ataque_squirtle == 'B':
            print('Squirtle ataca con burbuja')
            vida_pikachu -= 12
        elif ataque_squirtle == 'N':
            print('No has hecho nada')
        else:
            print('Squirtle ataca con Pistola Agua')
            vida_pikachu -=11

        if vida_pikachu < 0:
            vida_pikachu = 0

        if vida_squirtle < 0:
            vida_squirtle = 0

        barras_de_vida_pikachu = vida_pikachu * SIZE_BARRA_DE_VIDA / VIDA_INICIAL_PIKACHU
        print(
            f'Pikachu [{"*" * int(barras_de_vida_pikachu)}{" " * int((SIZE_BARRA_DE_VIDA - barras_de_vida_pikachu))}]({vida_pikachu}/{VIDA_INICIAL_PIKACHU})')

        barras_de_vida_squirtle = vida_squirtle * SIZE_BARRA_DE_VIDA / VIDA_INICIAL_SQUIRTLE
        print(
            f'Squirtle [{"*" * int(barras_de_vida_squirtle)}{" " * int((SIZE_BARRA_DE_VIDA - barras_de_vida_squirtle))}]({vida_squirtle}/{VIDA_INICIAL_SQUIRTLE})')
        input('Enter para continuar...\n\n')
        os.system('cls')

if vida_pikachu > vida_squirtle:
    print('Pikachu gana!')
else:
    print('Squirtle gana!')