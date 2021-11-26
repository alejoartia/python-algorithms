# RAIZ CUADRADA NO EXACTA
"""This is an example about how to get a not exact sqrt"""
goal = int(input('choise a number: '))
epsilon = 0.001
step = epsilon**2
response = 0.0

while abs(response**2 - goal) >= epsilon and response <= goal:
    print(abs(response**2 - goal), response)
    response += step

if abs(response**2 - goal) >= epsilon:
    print(f'doesnt fin sqrt {goal}')
else:
    print(f'the sqrt of {goal} is aproximaly {response}')