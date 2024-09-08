print("Welcome to Treasure Island. Your mission is to find the treasure.")

def game():
    choice1 = input("Left or Right? ")
    if(choice1 != "Left"):
        print("Game Over.")
        return
    
    choice2 = input("Swim or Wait? ")
    if(choice2 != "Wait"):
        print("Game Over.")
        return
    
    choice3 = input("Which Door? ")
    if(choice3 != "Yellow"):
        print("Game Over.")
        return
    
    print("You Win!")
    
game()
    