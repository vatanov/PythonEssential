class Car:
    def __init__(self, name, color, quantity):
        self.name = name
        self.color = color
        self.quantity = quantity

class Salon:
    def __init__(self, salon_name, Car):
        self.salon_name = salon_name
        self.Car = Car

    def sell_car(self):
        if self.Car.quantity > 0:
            self.Car.quantity -= 1
            print ("Car {} is sold!".format(self.Car.name))
        else:
            print ("There are no cars {} in the salon!".format (self.Car.name))


honda = Car("Honda", "White", 2)

liga = Salon("Liga", honda)
liga.sell_car()
print(honda.quantity)

liga = Salon("Liga", honda)
liga.sell_car()
print(honda.quantity)

liga = Salon("Liga", honda)
liga.sell_car()
print(honda.quantity)