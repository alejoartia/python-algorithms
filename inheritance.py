"""This is an example of inheritance"""
class Rectangle:

    def __init__(self, base, high):
        self.base = base
        self.high = high

    def area(self):
        return self.base * self.high

class Cuadrado(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)


if __name__ == '__main__':
    Rectangle = Rectangle(base=3, high=4)
    print(Rectangle.area())

    cuadrado = Cuadrado(side=5)
    print(cuadrado.area())