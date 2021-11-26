"""This is an example about how to do polimorfism"""
class Person:

    def __init__(self, name):
        self.name = name

    def avanza(self):
        print('walking')


class Biker(Person):

    def __init__(self, name):
        super().__init__(name)

    def avanza(self):
        print('riding by bycicle')


def main():
    person = Person('David')
    person.avanza()

    biker = Biker('Daniel')
    biker.avanza()


if __name__ == '__main__':
    main()