'''
Создайте иерархию классов транспортных средств.
В общем классе опишите общие для всех транспортных средств поля, в наследниках – специфичные для них.
Создайте несколько экземпляров. Выведите информацию о каждом транспортном средстве.
'''

class Vehicle():
    def __init__(self, name):
        self.name = name
        self.has_wheels = False
        self.has_wings = False
        self.can_fly = False
        self.can_run = False
        self.can_float = False

    def show_properties(self):
        print('Vehicle name:', self.name)
        print ('Vehicle class:', self.__class__.__name__)
        print('This vehicle has wheels:', self.has_wheels)
        print('This vehicle has wings:', self.has_wings)
        print('This vehicle can fly:', self.can_fly)
        print('This vehicle can run:', self.can_run)
        print('This vehicle can float:', self.can_float)
        print('-----------')


class AirVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.can_fly = True


class Aircraft(AirVehicle):
    def __init__(self, name):
        super().__init__(name)
        self.has_wheels = True
        self.has_wings = True


class Helicopter(AirVehicle):
    def __init__(self, name):
        super().__init__(name)
        self.has_wheels = True


def main():
    boeing_737 = Aircraft('Boeing-737')
    boeing_737.show_properties()

    comanche = Helicopter('Sikorsky RAH-66 Comanche')
    comanche.show_properties()


if __name__ == '__main__':
    main()