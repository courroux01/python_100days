import random


LIVES = 6

def get_words():
    with open("C:\\Users\\aedul\\OneDrive\\Desktop\\Python100\\Day007\\1000words.txt", 'r') as f:
        return [x.strip() for x in list(filter(lambda x: len(x) > 5, f.readlines()))]

print(get_words())
    
def logo():
    print(" _")
    print("| |")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __")
    print("| '_ \\ / _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|")
    print("                    __/ |")
    print("                   |____| ")

def hangman(fails=0):
    if(fails==0):
        print(" +---+")
        print(" |   |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
    elif(fails==1):
        print(" +---+")
        print(" |   |")
        print(" 0   |")
        print("     |")
        print("     |")
        print("     |")
    elif(fails==2):
        print(" +---+")
        print(" |   |")
        print(" 0   |")
        print(" |   |")
        print("     |")
        print("     |")
    elif(fails==3):
        print(" +---+")
        print(" |   |")
        print(" 0   |")
        print(" |\\  |")
        print("     |")
        print("     |")
    elif(fails==4):
        print(" +---+")
        print(" |   |")
        print(" 0   |")
        print("/|\\  |")
        print("     |")
        print("     |")
    elif(fails==5):
        print(" +---+")
        print(" |   |")
        print(" 0   |")
        print("/|\\  |")
        print("  \\  |")
        print("     |")
    else:
        print(" +---+")
        print(" |   |")
        print(" 0   |")
        print("/|\\  |")
        print("/ \\  |")
        print("     |")
    print(f"*******************************{6-fails}/6 LIVES LEFT*******************************")
        
        
def game():
    logo()
    word = list(random.choice(get_words()))
    template = ['_']*len(word)
    fails=0
    
    while(True):
        print(f"Word to guess: {''.join(template)}")
        letter = input("Guess a letter: ")
        
        if(letter in word):
            indexes = [i for i in range(len(word)) if word[i] == letter]
            template = [letter if j in indexes else template[j] for j in range(len(template))]
            word = [x if x != letter else letter for x in word]
            print(f"You guessed {letter}, and it is part of the word.")
        else:
            print(f"You guessed {letter}, and it is not part of the word. You lose a life.")
            fails += 1
        hangman(fails)
        
        if(template == word):
            print(f"You won! The word is {''.join(word)}." )
            break
        
        if(fails == LIVES):
            print(f"You lost! The word is {''.join(word)}.")
            break
            
game()
            
            