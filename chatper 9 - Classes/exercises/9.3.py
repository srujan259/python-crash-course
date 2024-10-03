class User:
    """ Class to model a user """

    def __init__(self, first_name, last_name, age, gender, profession):
        """ Initializing user instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.profession = profession

    def describe_user(self):
        """ method to describe the user """
        print(f"User {self.first_name} {self.last_name} is of age {self.age} , gender {self.gender} and working as {self.profession}")

    
    def greet_user(self):
        """ Method to greet user """
        print(f"Hi {self.first_name}, its nice to know about you")


user1 = User('srujan', 'kumar', 31, 'male', 'IT')

user1.describe_user()
user1.greet_user()