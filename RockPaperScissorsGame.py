from Contestant import Contestant
from Human import Human
from Computer import Computer

def main():
    print("LET'S PLAY ROCK-PAPER-SCISSORS!!\n")
    name = input("What is your name? ")
    human = Human(name)
    computer = Computer()
    cont = "yes"
    
    # rounds
    while cont.lower() == "yes":
        human.setChoice(input("Rock, Paper, Scissors? "))
        computer.makeChoice()
        print("The computer chose " + computer.getChoice())
        
        # determine winner of round
        humanChoice = human.getChoice()
        compChoice = computer.getChoice()
        if ((humanChoice == "Paper" and compChoice == "Rock")
            or (humanChoice == "Rock" and compChoice == "Scissors")
            or (humanChoice == "Scissors" and compChoice == "Paper")):
            winner = human
        elif (humanChoice == compChoice):
            winner = None
        else:
            winner = computer
        if winner:
            print("The winner is " + winner.getName())
            winner.addScore()
        else:
            print("Cats Game!")
        cont = input("Want to play another round? (yes/no)")
    
    #calculating winner
    if human.getScore() > computer.getScore():
        winner = human
        loser = computer
    elif human.getScore() == computer.getScore():
        winner = None
        loser = None
    else:
        winner = computer
        loser = human
    if winner:
        print("Thanks for playing!! " + winner.getName() + " is the winner." )
        print(winner.getName() + ":  " + str(winner.getScore()) + "\n" + loser.getName() + ":  "  + str(loser.getScore()))
    else:
        print("Thanks for playing!! Your game ended as a cats game, tied at " + str(human.getScore()))
        
main()
