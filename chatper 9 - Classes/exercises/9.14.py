

class RandomLetters:
    """ Class to pick random number """
    def __init__(self, random_list):
        """ init method """
        self.random_list = random_list
    
    def randomletter(self):
        """ Method to pick random letters """
        winning_ticket = []
        while len(winning_ticket)<4:
            pulled_item = choice(self.random_list)

            if pulled_item not in winning_ticket:
                print(f" We pulled {pulled_item}")
                winning_ticket.append(pulled_item)
        
        print(f"Winning ticket is {winning_ticket}")


import string
from random import choice
random_list = list(range(1,11))
first_5_lowercase = list(string.ascii_lowercase[:5])
random_list.extend(first_5_lowercase)

lottery = RandomLetters(random_list)
lottery.randomletter()