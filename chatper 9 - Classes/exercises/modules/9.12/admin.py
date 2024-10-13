from user import User

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
