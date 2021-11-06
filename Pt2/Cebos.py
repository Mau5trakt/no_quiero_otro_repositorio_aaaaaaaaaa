import random
map_objects = []
number_food = 10

for lista in range(number_food):
    position_x = random.randint(0,19)
    position_y = random.randint(0,14)
    vector_food = [position_x,position_y]
    map_objects.append(vector_food)


print(map_objects)

