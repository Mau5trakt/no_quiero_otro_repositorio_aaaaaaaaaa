VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 95
SIZE_BARRA_DE_VIDA = 20
vida_pikachu = VIDA_INICIAL_PIKACHU
barras_de_vida_pikachu = int(vida_pikachu * SIZE_BARRA_DE_VIDA / VIDA_INICIAL_PIKACHU)
print("Pikachu: [{}{}]({}/{})".format("*" * barras_de_vida_pikachu, " " * (SIZE_BARRA_DE_VIDA - barras_de_vida_pikachu),
                                      vida_pikachu, VIDA_INICIAL_PIKACHU, vida_pikachu, VIDA_INICIAL_PIKACHU))

vida_squirtle = VIDA_INICIAL_SQUIRTLE
barras_de_vida_squirtle = int(vida_squirtle * SIZE_BARRA_DE_VIDA / VIDA_INICIAL_SQUIRTLE)
print("Squirtle: [{}{}]({}/{})".format("*" * barras_de_vida_squirtle, " " * (SIZE_BARRA_DE_VIDA - barras_de_vida_squirtle),
                                       vida_squirtle, VIDA_INICIAL_SQUIRTLE, vida_squirtle, VIDA_INICIAL_SQUIRTLE))