import random

def scissors():
    print('    ___________')
    print('---\'  ________)')
    print('          ______)')
    print('       (____)')
    print('       (____)')
    print('---.__(___)')
    
def rock():
    print('    _______')
    print('---\'  ____)')
    print('       _____)')
    print('       _____)')
    print('       ____)')
    print('---.__(___)')
    
def paper():
    print('    __________')
    print('---\'  _________)')
    print('       _________)')
    print('       _________)')
    print('       _________)')
    print('---._________)')
    
    
def game():
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
    computer_choice = int(random.random() * 3)
    
    choices = [rock, paper, scissors]
    
    choices[choice]()
    
    print("\nComputer Chose: \n")
    choices[computer_choice]()
    
    if(choice == 0):
        if(computer_choice == 0):
            print("Draw!")
        elif(computer_choice == 1):
            print("You Lose!")
        else:
            print("You Win!")
    elif(choice == 1):
        if(computer_choice == 0):
            print("You Win!")
        elif(computer_choice == 1):
            print("Draw!")
        else:
            print("You Lose!")
    else:
        if(computer_choice == 0):
            print("You Lose!")
        elif(computer_choice == 1):
            print("You Win!")
        else:
            print("Draw!")
    
    
game()