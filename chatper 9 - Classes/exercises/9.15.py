

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
        return winning_ticket
    
    def lottery_chance(self, winning_ticket):
        """ Method to check how hard it is to get my winning ticket """
        count = 0
        win_number = 0
        while win_number < 4:

            pulled_item = choice(self.random_list)
            if pulled_item in winning_ticket:
                print(f"Found {pulled_item} in {winning_ticket}")
                self.random_list.remove(pulled_item)
                count += 1
                win_number += 1
            else:
                count += 1
        print(f"It tool {count} pulls to to win")


import string
from random import choice
random_list = list(range(1,11))
first_5_lowercase = list(string.ascii_lowercase[:5])
random_list.extend(first_5_lowercase)

lottery = RandomLetters(random_list)
winning_ticket = lottery.randomletter()
lottery.lottery_chance(winning_ticket)