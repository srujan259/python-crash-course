""" A class that can be used to represent a car """

class Car:
    """ A simple attempt to represent a car """

    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """ Return A neatly formatted descripte name """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """ Print a statement showing the cars mileage """
        print(f"This car has {self.odometer_reading} miles on it.")

class Battery:
    """ A simple attempt to model a battery for an electic car """

    def __init__(self, battery_size=40):
        """ Initialize the battery attributes """
        self.battery_size = battery_size
    
    def describe_battery(self):
        """ Print statement describing the battery size """
        print(f"Battery of car is {self.battery_size}-kWH")

    def get_range(self):
        """ Print statement about the range this battery provides. """
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go {range} on full charge")

class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles. """

    def __init__(self, make, model, year):
        """ Initializes attributes of the parent class. """
        super().__init__(make, model, year)
        #instances as attribes
        self.battery = Battery()