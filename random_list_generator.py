# Generates a random list - used for testing purposes
import random


def gen_list(min, max, length):
    rand_list = []
    for i in range(length):
        rand_list.append(random.randint(min, max))
    return rand_list
