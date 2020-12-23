import random
from Contestant import Contestant

class Computer(Contestant):
    def __init__(self):
        super().__init__("Computer")
    def makeChoice(self):
        self._choice = random.choice(Contestant.options)
