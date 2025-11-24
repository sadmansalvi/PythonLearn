import random

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second   #for returning a tuple we dont need parentheses

dice = Dice()     #instance of the class Dice
print(dice.roll())


