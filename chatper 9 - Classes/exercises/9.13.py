from random import randint

class Die:
    def __init__(self, sides, no_of_rolls):
        self.sides = sides
        self.no_of_roles = no_of_rolls

    def roll_die(self):
        """ Method to print random number from n sided die """
        result = []
        for n in range(self.no_of_roles):
            num = randint(1, self.sides)
            result.append(num)
        print(f"Die was rolled {self.no_of_roles} and the results are : {result}")
    


die1 = Die(6,10)
die1.roll_die()
die2 = Die(20, 10)
die2.roll_die()