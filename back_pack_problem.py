"""This is a resolution of the bag problem (problema del morral)"""

def bagpack(size_bag, weigth, values, n):

    if n == 0 or size_bag == 0:
        return 0

    if weigth[n - 1] > size_bag:
        return bagpack(size_bag, weigth, values, n - 1)

    return max(values[n - 1] + bagpack(size_bag - weigth[n - 1], weigth, values, n - 1),
                bagpack(size_bag, weigth, values, n - 1))


if __name__ == '__main__':
    values = [60, 100, 120]
    weigth = [10, 20, 30]
    size_bag = 5
    n = len(values)

    result = bagpack(size_bag, weigth, values, n)
    print(result)