
def logo():
    print("  ,adPPYba,  ,adPPYYba,   ,adPPYba,  ,adPPYba,  ,adPPYba,   8b,dPPYba, ")
    print("a8'      ''  ''     'Y8  a8P_____88  I8[    ''  ''    'Y8   88P'  'Y8  ")
    print("8b           ,adPPPPP88  8PP'''''''   ''Y8BA,   ,adPPPPP88  88         ")
    print("'8a     ,aa  88,    ,88  '8b,   ,aa  'aa   ]8I  88,    ,88  88         ")
    print("''Ybbd8*''   '8bbdP'Y8    ''Ybbd8''  ''YbbdP''  ''8bbdP'Y8  88         ")

    print()

    print("                               88                                      ")
    print("                              88                                       ")
    print("                              88                                       ")
    print("  ,adPPYba,  88  8b,adPPYba,  88,dPPYba,    ,adPPYba,  8b,dPPYba,      ")
    print("a8'      ''  88  88P'    '8a  88'     '88  a8P_____88  88P'  'Y8       ")
    print("8b           88  88       d8  88       88  8PP'''''''  88              ")
    print("'8a     ,aa  88  88b,   ,a8'  88       88  '8b,   ,aa  88              ")
    print("''Ybbd8*''   88  88'Ybbdp''  '88       88  ''Ybbd8''   88              ")
    print("                 88                                                    ")
    print("                 88                                                    ")
    
        
ascii_a = 97
ascii_z = 122
total_letters = 26
        
        
def encode(message, shift):
    encoded = []
    for char in message:
        char_ascii = ((ord(char)+shift) % ascii_z)
        if(char_ascii < ascii_a):
            char_ascii += ascii_a
        encoded.append(chr(char_ascii))
            
    return ''.join(encoded) 
    
        
def decode(message, shift):
    decoded = []
    for char in message:
        char_ascii = ((ord(char)-shift) % ascii_z)
        if(char_ascii <= ascii_a):
            char_ascii += total_letters
        decoded.append(chr(char_ascii))
            
    return ''.join(decoded) 
    
     
def main():
    while True:
        while True:
            print("Type 'encode' to encrypt, or 'decode' to decrypt: ")
            choice1 = input()

            if not choice1 in ['encode', 'decode']:
                print("Invalid choice.")
            else: break
        
        while True:
            print("Type your message:")
            message = input()
            
            if not all(char.isalpha() and char.islower() for char in message):
                print("This cypher only supports english lowercase letters.")
            else: break
        
        while True:
            print("Type the shift number: ")
            shift = input()
            
            try:
                shift = int(shift)
            except:
                print("Invalid shift number. Choose a number.")

            if shift < 0:
                print("Invalid shift number. Choose a positive number.")
            else: break    
        
        if choice1 == 'encode':
            print(f"Here's the encoded result: {encode(message, shift)}")
        else:
            print(f"Here's the decoded result: {decode(message, shift)}")
        
        while True:
            print("Type 'yes' if you want to go again, Othewise type no.")
            choice2 = input()
            
            if choice2 not in ['yes', 'no']:
                print("Invalid choice.")
            else: break
        
        if choice2 == 'no': break
        
main()