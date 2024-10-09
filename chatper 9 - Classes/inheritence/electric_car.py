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

class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles. """

    def __init__(self, make, model, year):
        """ Initializes attributes of the parent class. """
        super().__init__(make, model, year)
        self.battery_size = 40
    
    def describe_battery(self):
        """ Method to describe battery of an electric car """
        print(f"Battery of car {self.make} {self.model} is {self.battery_size}-kWH")


my_ev6 = ElectricCar("kia", "ev6", 2024)
print(my_ev6.get_descriptive_name())
my_ev6.describe_battery()