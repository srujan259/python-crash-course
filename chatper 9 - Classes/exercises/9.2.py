class Restaurant:
    """ Structure of my restaurant """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initializes when the instance is created """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name} is the best in hyderabad with {self.cuisine_type} ")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now OPEN!!")


fav_res = Restaurant('paradise', 'indian')
fav_res.describe_restaurant()


ancy_fav = Restaurant('kamat', 'meals')
ancy_fav.describe_restaurant()

