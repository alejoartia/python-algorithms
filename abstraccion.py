"""This is an example of abstraction"""
class washmachine:

    def __init__(self):
        pass

    def wash(self, temperature='hot'):
        self._filling_tank(temperature)
        self._add_soap()
        self._wash()
        self._spinnig()

    def _filling_tank(self, temperature):
        print(f'filling the tank with water {temperature}')

    def _add_soap(self):
        print('putting soap')

    def _wash(self):
        print('washing clothes')

    def _spinnig(self):
        print('Spinning clothes')


if __name__ == '__main__':
    lavadora = washmachine()
    lavadora.wash()