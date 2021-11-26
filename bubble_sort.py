"""This is an example about bobble sort"""

import random

def bubble_sort(list_a):
    n = len(list_a)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if list_a[j] > list_a[j + 1]:
                list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]

    return list_a
    numbers.sort()
    return numbers[0]+numbers[1]
if __name__ == '__main__':
    size_of_list = int(input('list size? '))

    list_a = [random.randint(0, 100) for i in range(size_of_list)]   # create a random list
    print(list_a)

    list_a_sort = bubble_sort(list_a)
    print(list_a_sort)