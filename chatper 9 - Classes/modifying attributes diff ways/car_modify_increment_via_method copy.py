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

    def update_odometer(self, mileage):
        """ Update odomter reading.
            Reject the change if it attempts to roll odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an aodometer!")
    
    def increment_odometer(self, miles):
        """ Add the given amount to the odometer reading"""
        if not miles < 0:
            self.odometer_reading += miles
        else:
            print("Cant roll back odometer")

my_new_car = Car('audi','a4', 2024)
print(my_new_car.get_descriptive_name())

# Modifying an Attribute’s Value via method

my_new_car.update_odometer(2500)
my_new_car.read_odometer()

my_new_car.increment_odometer(1500)
my_new_car.read_odometer()