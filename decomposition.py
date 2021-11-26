"""This is an example about how to use decomposition"""

def comprehensive_enumeration(goal):
    response = 0

    while response ** 2 < goal:
        response += 1

    if response ** 2 == goal:
        print(f'the sqrt of {goal} is {response}')
    else:
        print(f'{goal} without sqrt')


def aproximation(goal, epsilon):
    step = epsilon ** 2
    response = 0.0
    iterations = 0

    while abs(response ** 2 - goal) >= epsilon and response <= goal:
        response += step
        iterations += 1

    if abs(response ** 2 - goal) >= epsilon:
        print(f'doesnt find sqrt {goal}')
    else:
        print(f'the sqrt of {goal} is {response}')


def binary_search(goal, epsilon):
    low = 0.0
    high = max(1.0, goal)
    response = (high + low) / 2

    # absolute = abs(response**2 - goal)
    # print(f'absoluto: {absoluto}')

    while abs(response ** 2 - goal) >= epsilon:
        print(f'low={low}, high={high}, response={response}')
        if response ** 2 < goal:
            low = response
        else:
            high = response
        response = (high + low) / 2

        print(f'the sqrt of {goal} is {response}')


option = int(input(
    f'Choose the ordering algorithm to find the square root of your number \n 1. Comprehensive Enumeration \n 2. aproximation \n 3. Binary search \n'))

if option == 1:
    print('1. Comprehensive Enumeration')
    number = int(input('* Digit a number: '))
    comprehensive_enumeration(number)
elif option == 2:
    print('2. aproximation')
    number = int(input('* Digit a number: '))
    epsilon_parameter = float(input('* Digit a epsilon: '))
    aproximation(number, epsilon_parameter)
elif option == 3:
    print('3. binary search')
    number = int(input('* digit a number: '))
    epsilon_parameter = float(input('* Digit a epsilon: '))
    binary_search(number, epsilon_parameter)
else:
    print('not valid option')
