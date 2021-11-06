lista_de_la_compra = []
item = ''

while item !='Q':
    item = input('Que desea agregar a la lista de la compra (Q para salir)?').upper()
    if item == 'Q':
        break
    else:
        confirmar_item = ''
        while confirmar_item not in ['S','N']:
            confirmar_item = input(f'desea agregar {item.lower()} a la lista de la compra (S/N)?').upper()
            if item in lista_de_la_compra:
                en_lista = ''
                while en_lista not in ['S', 'N']:
                    en_lista = input(f'Ya se ha agregado {item.lower()} a la lista, desea agregar otro articulo?(S/N)').upper()
                    if en_lista == 'S':
                        item = ''
                    elif en_lista == 'N':
                        item = 'Q'
            else:
                lista_de_la_compra.append(item)
                item = ''


print(f'La lista de la compra es {lista_de_la_compra}')