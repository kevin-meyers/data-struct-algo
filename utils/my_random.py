import random

def shuffle(l):
    last_index = len(l) - 1

    while(last_index):
        rand_index = round(random.random() * last_index)
        l[rand_index], l[last_index] = l[last_index], l[rand_index]

        last_index -= 1
