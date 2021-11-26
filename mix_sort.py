"""This is an example about mix sort without a library"""

import random


def mix_sort(list_a):
    if len(list_a) > 1:
        middle = len(list_a) // 2
        left = list_a[:middle]
        rigth = list_a[middle:]
        print(left, '*' * 5, rigth)

        # llamada recursiva en cada mitad
        mix_sort(left)
        mix_sort(rigth)

        # Iteradores para recorrer las dos sublist_as
        i = 0
        j = 0
        # Iterador para la list_a principal
        k = 0

        while i < len(left) and j < len(rigth):
            if left[i] < rigth[j]:
                list_a[k] = left[i]
                i += 1
            else:
                list_a[k] = rigth[j]
                j += 1

            k += 1

        while i < len(left):
            list_a[k] = left[i]
            i += 1
            k += 1

        while j < len(rigth):
            list_a[k] = rigth[j]
            j += 1
            k += 1

        print(f'left {left}, rigth {rigth}')
        print(list_a)
        print('-' * 50)

    return list_a


if __name__ == '__main__':
    size_list = int(input('De que tamano sera la lista? '))

    list_a = [random.randint(0, 100) for i in range(size_list)]
    print(list_a)
    print('-' * 20)

    sorted_list = mix_sort(list_a)
    print(sorted_list)