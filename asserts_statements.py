"""This is a program about how to use the asserts statements for errors"""

def divisor(num):
    divisors =[i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():

    num = input(f'put a number: ')
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisor(int(num)))
    print("program finished")


if __name__ =='__main__':
    run()