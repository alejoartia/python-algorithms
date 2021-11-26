"""example of binary search"""

goal = int(input('choise a number: '))
epsilon = 0.001
low = 0.0
high = max(1.0, goal)
respuesta = (high + low) / 2

while abs(response**2 - goal) >= epsilon:
    print(f'low={low}, high={high}, response={response}')
    if response**2 < goal:
        low = response
    else:
        high = response

    response = (high + low) / 2

print(f'the sqrt of  {goal} is {response}')