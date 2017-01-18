"""
Project: Rock-paper-scissors-lizard-Spock template
Implementation by Roni Rengit for a course in Coursera

The key idea of this program is to equate the strings
"rock", "paper", "scissors", "lizard", "Spock" to numbers
as follows:

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
"""
from random import randrange

def name_to_number(name):
    """Converts player choice into player number"""
    names={'rock': 0, 'spock': 1, 'paper': 2, 'lizard': 3, 'scissors': 4}    
    if name in names:
         return int(names[name])
    else:
        print("Please choose either 'Rock', 'Spock', 'Paper', 'Lizard' or 'Scissors'")
        game()
    
def number_to_name(number):
    """Converts computer number into computer choice"""
    numbers = {0 : 'rock', 1: 'spock', 2: 'paper', 3: 'lizard', 4: 'scissors'}
    if number in numbers:
        return numbers[number]
    else:
        print("Please choose numbers in the range of 0 - 4")
    
def rpsls(player_choice): 
    """Computes difference between computer choice and player choice
    and produces a result"""

    print("")
    print("Player Chooses ", player_choice.upper())
    player_number = name_to_number(player_choice.lower())

    comp_number = randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print("Computer chooses ", comp_choice.upper())

    difference = (comp_number - player_number) % 5
    
    if difference in [1, 2]:
        print("Computer wins!")
    elif difference in [3, 4]:
        print("Player wins!")
    else:
        print("Player and Computer are Tie!")
        
    while True:
        repeat = input("\nDo you want to play again('Y' or 'N'): ")
        if repeat in ['Y', 'y']:
            player_choice = input("Your choose?: ")
            player_choice= player_choice.strip()
            rpsls(player_choice)
        elif repeat in ['N', 'n']:
            print("Thank you for playing.")
            input()
            exit()
        else:
            print("The question was Yes or No!!!.\nRestarting game....")
            game()
            

# Game Interface
def game():

    print(30 * "*" + "ROCK - PAPER - SPOCK - LIZARD - SCISSORS" + 30 * '*')
    print(5 * "\t" +"INSTRUCIONS")
    print("RPSLS is a zero-sum hand game usually played between two people, in this case you will be playing \
          \nagainst the computer. You have to choose either ROCK, PAPER, SPOCK, LIZARD or SCISSORS. Best of luck.")
    print("Program created for your pleassure by Roni Rengit")
    print(100 * '*' + "\n")
    player_choice = input("Your choice?: ")
    player_choice = player_choice.strip()
    rpsls(player_choice)

# Start game
game()
