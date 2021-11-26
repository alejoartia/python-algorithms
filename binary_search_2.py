"""This is an example of binary searching"""

import random

def binary_search(list_a, start, end, goal):
    print(f'searching {goal} beetwen {list_a[start]} and  {list_a[end-1]}')
    if start > end:
        return False

    half = (start + end) // 2

    if list_a[half] == goal:
        return True
    elif list_a[half] < goal:
        return binary_search(

            list_a, half+1, end, goal)
    else:
        return binary_search(list_a, start, half-1, goal)

if __name__ == '__main__':
    tamano_de_list_a = int(input('what is the list size?'))
    goal = int(input('what number you whant to find?'))

    list_a = sorted([random.randint(0, 100) for i in range(tamano_de_list_a)])

    finded = binary_search(list_a, 0, len(list_a), goal)

    print(list_a)
    print(f'The element {goal} {"is" if finded else "is not"} in the list')
