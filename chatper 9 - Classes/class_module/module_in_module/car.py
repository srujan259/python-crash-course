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
