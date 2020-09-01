class Car():
    """This is class to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.color = 'White'
        self.odometer_reading = 0  # in miles

    # getter(return) and setter(assign a new value, method with parameter)
    def get_description(self):
        msg = f"Your car: \n\tmanufacturer: {self.make}\n\tmodel: {self.model}\n\tYear: {self.year}\n\tColor: {self.color}"
        return msg

    def set_color(self, new_color: str):
        print(f"Changing the color {self.color} to {new_color}")
        self.color = new_color

    def read_odometer(self):
        """Gets the odometer miles of the car."""
        msg = f"Car has {self.odometer_reading} miles on it."
        return msg

    def set_odometer(self, new_miles):
        if new_miles >= self.odometer_reading:
            print(f"Setting odometer reading from {self.odometer_reading} to {new_miles}")
            self.odometer_reading = new_miles
        else:
            print(f"You can not roll back odometer from {self.odometer_reading} to {new_miles}.")

    def increment_odometer(self, miles):
        """Adding :param miles to odometer_reading"""
        if miles > 0:
            print(f"Incrementing odometer with more {miles} miles")
            # self.odometer_reading = self.odometer_reading + miles
            self.odometer_reading += miles
        else:
            print(f"Negative value can not be passed to odometer : {miles}.")


class ElectricCar(Car):  # Inheriting Car class
    """Represents Electric car, inherits all features of Car."""

    def __init__(self, make, model, year):
        """Child class constructor, OVERRIDING(rewrite) the parent constructor"""
        super().__init__(make, model, year)  # calling the constructor of parent class
        self.battery_size = 80
        # self.make = make
        # self.model = model

    def get_description(self): # Overriding the parent method
        msg = f"Your car: \n\tmanufacturer: {self.make}\n\tmodel: {self.model}\n\t" \
              f"Year:{self.year}\n\tColor: {self.color}\n\tBattery size: {self.battery_size}"
        return msg

    def test_method(self):
        print(self.get_description())  # current class get_description() method, with battery_size
        print(super().get_description())  # parent class get_description() method
        #  'this' keyword in java is used as 'self' in python
