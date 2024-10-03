class Restaurant:
    """ Structure of my restaurant """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initializes when the instance is created """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name} is the best in hyderabad with {self.cuisine_type} ")
        print (f"\n{self.restaurant_name} is famous for biryani")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now OPEN!!")


fav_res = Restaurant('paradise', 'indian')
print(fav_res.restaurant_name)
print(fav_res.cuisine_type)

fav_res.describe_restaurant()
fav_res.open_restaurant()