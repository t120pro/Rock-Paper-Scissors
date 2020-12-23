from Contestant import Contestant

class Human(Contestant):
    def setChoice(self, choice):
        while choice.capitalize() not in Contestant.options:
            choice = input("Please enter a valid option: Rock, Paper, or Scissors ")
        self._choice = choice.capitalize()
