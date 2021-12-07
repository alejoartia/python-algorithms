"""This is an example of a decorator in python"""

def smart_divide(func):
    def inner(a,b):
        a=a*2
        b=b*2
        return func(a,b)
    return inner


@smart_divide
def divide(a, b):
    print(f'{a} y {b}')


if __name__=='__main__':
    divide(2,4)
