class Restaurant:
    """ Structure of my restaurant """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initializes when the instance is created """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name} is the best in hyderabad with {self.cuisine_type} cuisine ")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now OPEN!!")

    def read_number_served(self):
        """ Read number of customer served """
        print(f"Total customers served is {self.number_served}")
    
    def set_number_served(self, served):
        """ Set number of customers served"""
        self.number_served = served
    
    def increment_number_served(self, increment_number):
        """ Increment number served """
        self.number_served += increment_number


class IceCreamStand(Restaurant):
    """ Icecream Class  """

    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours
    
    def display_flavours(self):
        """ Flavours for icecream stand """
        print(f"\nFlavours of the icecream restaurant {self.restaurant_name} :")
        for flavour in self.flavours:
            print(f"- {flavour}")

icecream = IceCreamStand("Polarbear", "Dessert", ["chocolate", "strawberry", "mango"])
icecream.describe_restaurant()
icecream.display_flavours()