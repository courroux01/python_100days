
def get(s, reqs):
    while True:
        print(s)
        inp = input()
        
        if not all([each(inp) for each in reqs]):
            print("Invalid input. Please try again. ")
        else:
            return inp
        
def main():
    print("Welcome to the simple calculator.")
    
    first = float(get( \
        "Please enter the first number. ", 
        [ 
            lambda x: x.replace('.', '').isnumeric(),
        ]
    ))
    
    operator = get( \
        "Please enter the operator. ", 
        [
            lambda x: x in ['+', "-", '*', "/", "%", "**"],
        ]
    )
    
    second = float(get( \
        "Please enter the second number. ", 
        [ 
            lambda x: x.replace('.', '').isnumeric(),
        ]
    ))
    if(operator == '+'):
        print(f"{first} {operator} {second} is: {first + second}")   
    elif(operator == '-'):
        print(f"{first} {operator} {second} is: {first - second}")   
    elif(operator == '*'):
        print(f"{first} {operator} {second} is: {first * second}")   
    elif(operator == '/'):
        if second == 0:
            print(f"Cannot divide by zero.")
            try_again()
            return
        print(f"{first} {operator} {second} is: {first / second}")   
    elif(operator == '**'):
        print(f"{first} {operator} {second} is: {first ** second}")   
    elif(operator == '%'):
        if second == 0:
            print(f"Cannot get remainder by zero.")
            try_again()
            return
        print(f"{first} {operator} {second} is: {first + second}")    
    
def try_again():
    choice = get( \
        "Want to try again?",
        [
            lambda x: x in ['yes', 'no']
        ]
    )
    
    if(choice == 'yes'):
        main()
    else:
        print("Thank you for using this app by Abdullah Alojado")
main()