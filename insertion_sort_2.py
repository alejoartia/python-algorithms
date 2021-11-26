"""This is an example about insertion sort"""
def insertion_sort(list_a):

    for index in range(1, len(list_a)):
        current_value = list_a[index]
        actual_position = index

        while actual_position > 0 and list_a[actual_position - 1] > current_value:
            list_a[actual_position] = list_a[actual_position - 1]
            actual_position -= 1

        list_a[actual_position] = current_value