print("Welcome to the tip calculator!")

total = float(input(f"What was the total bill? $"))

while(True):
    tip = int(input(f"How much tip would you like to give? 10, 12, or 15? "))

    if(tip not in (10,12,15)):
        print("Please select between the three options.")
    else: 
        break

split = int(input(f"How many people to split the bill? "))

each = total / split

print(f"Each person should pay: ${each:.2f}")


