"""This is an example of lineal searching"""

import random

def lineal_search(list_a, goal):
    match = False

    for element in list_a:
        if element == goal:
            match = True
            break

    return match

if __name__ == '__main__':
    size_list = int(input('whats is the size list_a?'))
    goal = int(input('waht number you want to find'))

    list_a = [random.randint(0, 100)for i in range(size_list)]

    finded = lineal_search(list_a, goal)
    print(list_a)
    print(f'El element {goal} {"is" if finded else "is nor"} in the list')