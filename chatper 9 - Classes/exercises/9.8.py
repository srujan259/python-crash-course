class User:
    """ Class to model a user """

    def __init__(self, first_name, last_name, age, gender, profession):
        """ Initializing user instance """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.profession = profession
        self.login_attempts = 0

    def describe_user(self):
        """ method to describe the user """
        print(f"User {self.first_name} {self.last_name} is of age {self.age} , gender {self.gender} and working in {self.profession}")

    
    def greet_user(self):
        """ Method to greet user """
        print(f"Hi {self.first_name}, its nice to know about you")

    def increment_login_attempts(self):
        """ Increment login attempts """
        self.login_attempts += 1
        print(f"Login attempts now is {self.login_attempts}")

    def reset_login_attempts(self):
        """ Reset login attempts """
        self.login_attempts = 0
        print(f"Login attempts after reset = {self.login_attempts}")

class Privileges():
    """ Class to model priviledges of a user """

    def __init__(self, priviledges=[]):
        self.priviledges = priviledges

    def show_privileges(self):
        """ Method to show priviledges of an admin """
        print("Below are the priviledges of an admin:")
        if self.priviledges:
            for p in self.priviledges:
                print(f"- {p}")
        else:
            print("user has no priviledges!!")
    


class Administrator(User):
    """ Model charesteristics of an administrator """

    def __init__(self, first_name, last_name, age, gender, profession):
        super().__init__(first_name, last_name, age, gender, profession)
        self.priviledges = Privileges()
    


admin1 = Administrator("srujan", "kottapally", 31, 'male', 'Devops' )
admin1.describe_user()
admin1.priviledges.show_privileges()
print("\nAdding privileges...")
admin1.priviledges.priviledges = ['can add post', 'can delete post', 'can ban a user']
admin1.priviledges.show_privileges()