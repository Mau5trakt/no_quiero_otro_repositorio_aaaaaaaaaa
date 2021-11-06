import readchar
import os
import random
POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]
tail = []
tail_length = 0
map_objects = []
number_food = 11

#for lista in range(number_food):
 #   new_position = [random.randint(0, MAP_WIDTH), random.randint(0,MAP_HEIGHT)]
  #  if new_position not in map_objects:
   #     map_objects.append(new_position)

while len(map_objects) < number_food:
    new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)


while True:

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None


            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length +=1

                if tail_in_cell:
                    exit("Haz muerto")



            print(f"{char_to_draw}", end= "  ")
        print("|")


    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print(f"Cola {tail}")
    print(my_position)

    #Ask user where he wants to move
    #direction = input("Donde te quieres mover?[WASD]:")
    direccion = readchar.readchar().decode()
    print(direccion)

    if direccion == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -=1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direccion == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] +=1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direccion == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -=1
        my_position[POS_X] %= MAP_WIDTH
    elif direccion == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] +=1
        my_position[POS_X] %= MAP_WIDTH
    elif direccion =="q":
        break

    os.system("cls")
