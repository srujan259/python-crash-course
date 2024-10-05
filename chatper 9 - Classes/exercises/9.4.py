class Restaurant:
    """ Structure of my restaurant """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initializes when the instance is created """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name} is the best in hyderabad with {self.cuisine_type} ")
        print (f"\n{self.restaurant_name} is famous for biryani")

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


fav_res = Restaurant('paradise', 'indian')
print(fav_res.restaurant_name)
print(fav_res.cuisine_type)

fav_res.describe_restaurant()
fav_res.open_restaurant()
fav_res.set_number_served(25)
fav_res.read_number_served()
fav_res.increment_number_served(26)
fav_res.read_number_served()