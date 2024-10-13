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

    def  fill_gas_tank(self):
        """ Fill gas tank """
        print("Its time to fill the gas tank!")

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

    def upgrade_battery(self):
        """ Check and upgrade battery size """
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles. """

    def __init__(self, make, model, year):
        """ Initializes attributes of the parent class. """
        super().__init__(make, model, year)
        #instances as attribes
        self.battery = Battery()
    


my_ev6 = ElectricCar("kia", "ev6", 2024)
print(my_ev6.get_descriptive_name())
my_ev6.battery.battery_size = 40
my_ev6.battery.describe_battery()
my_ev6.battery.get_range()
#now upgrading the battery to increase range
my_ev6.battery.upgrade_battery()
my_ev6.battery.get_range()