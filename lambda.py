"""This is a basic example of lambda"""

lista_a = lambda x: print(list(i for i in x))
x = [1, 2, 3]


def lista_aB(x):
    for i in x:
        print(i)

lista_a(x)

suma = lambda x,y,z: print(x+y+z)

x=1
y=2
z=3

suma(x,y,z)