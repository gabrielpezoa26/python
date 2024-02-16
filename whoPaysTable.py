import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")

num_aleatorio = random.randint(0,4)
print(names[num_aleatorio])
