import random

class Dice:
    def __init__(self, diceCount):
        self.diceCount = diceCount
        self.min = 1
        self.max = 6

    def rollDice(self):
        totalSum = 0
        diceUsed = 0

        while diceUsed < self.diceCount:
            totalSum += random.randint(self.min, self.max)
            diceUsed += 1

        return totalSum