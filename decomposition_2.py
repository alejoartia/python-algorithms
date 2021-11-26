"""This is an example about how to do decomposition"""
class Automobil:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._state = 'staying'
        self._motor = Motor(cylinders=4)

    def speed_up(self, type='slow'):
        if type == 'fast':
            self._motor.gas_injection(10)
        else:
            self._motor.gas_injection(3)

        self._state = 'in_movement'


class Motor:

    def __init__(self, cylinders, type='gas'):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0

    def gas_injection(self, quantity):
        pass