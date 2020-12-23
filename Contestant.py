class Contestant():
    options = ["Rock", "Paper", "Scissors"]
        
    def __init__(self, name):
        self._name = name
        self._score = 0
        
    def getChoice(self):
        return self._choice
    def getName(self):
        return self._name
    def getScore(self):
        return self._score
    
    def setChoice(self, choice):
        self._choice = choice.capitalize()
    def setName(self, name):
        self._name = name
        
    def addScore(self):
        self._score += 1
    
    def __str__(self):
        return self._name


