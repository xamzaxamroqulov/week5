# from classes.cars import *
from classes.cars import Car, ElectricCar
from collections import OrderedDict

car1 = Car('toyota', 'highlander', '2020')
print(car1.get_description())
car1.set_color('Red')
print(car1.get_description())
print(car1.read_odometer())

car1.odometer_reading = 1000
print(car1.read_odometer())
print(car1.odometer_reading)

# car1.odometer_reading = 800   # not good practice
car1.set_odometer(800)  # we can put logic in the method
print(car1.read_odometer())
print(car1.odometer_reading)

car1.set_odometer(1500)
print(car1.read_odometer())

car1.increment_odometer(-500)
assert  car1.read_odometer() == 1500
print(car1.read_odometer())

car1.increment_odometer(400)
print(car1.read_odometer())

ecar1 = ElectricCar('Tesla', 'Model Y', '2020')
print(ecar1.get_description())
ecar1.set_color('Blue')
print(ecar1.get_description())
print('-----------------------')
ecar1.test_method()
# ecar1.battery_size

#  Object Oriented Programming
#  - Class, Object
#  - constructor (__init__() )
#  - Inheritance (single class, multiple class)
    #   - relationship between Parent and Child : Parent >> Child
    # car1.battery_size, car1.test_method()  parent does not have access to child attributes/methods
#  - self keyword, super() method , difference
#  - Overriding(due Inheritance) - rewriting parent attributes/method in child class
#   - FYI: check: java method to overload, using the same name with different parameters
