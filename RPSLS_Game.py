"""
Program Name: CLASS IMPLEMENTATION OF ROCK-PAPER-SCISSORS-SPOCK-LIZARD GAME
Author: Roni Rengit
"""

from random import randint

class rpsls(object):


    def __init__(self, player_choice):

        self.option = {0:'rock', 1:'Spock', 2:'paper',3:'lizard', 4:'scissors'}
        self.player_choice = player_choice

        print('You have choosen {}'.format(self.option[self.player_choice]))
        comp_choice = randint(0,4)
        print('Computer has chosen {}'.format(self.option[comp_choice]))

        difference = (comp_choice - self.player_choice) % 5

        if difference in [1, 2]:
            print("Computer wins!")
        elif difference in [3, 4]:
            print("Player wins!")
        else:
            print("Player and Computer are Tie!")

def main():
    """Game Menu"""

    print("RPSLS is a zero-sum hand game usually played between two people.\nIn this case you will be playing against the computer.\nYou have to choose either ROCK, PAPER, SPOCK, LIZARD or SCISSORS. Best of luck.\n")
    play_again = True
    while play_again == True:

        num = input("Choose either {0:'rock', 1:'Spock', 2:'paper, 3:'lizard', 4:'scissors'}")
        if num.isdecimal() and int(num) < 5:
            player_play = rpsls(int(num))
            exit = input("Do you want to play again?")
            if exit not in ['Yes', 'yes', 'y', 'Y']: play_again = False
        else:
            print("Error: Won't accept strings or incorrect option!!!!")

if __name__ == '__main__':
    main()
else:
    main()
