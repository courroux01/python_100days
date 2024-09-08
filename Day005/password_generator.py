import random

print("Welcome to the PyPasswordGenerator!")

letter_count = int(input("How many letters would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like?\n"))
number_count = int(input("How many numbers would you like?\n"))

letters = [chr(x) for x in range(65,91)] + \
          [chr(x) for x in range(97,123)]
          
symbols = [chr(x) for x in range(58,65)] + \
          [chr(x) for x in range(123,127)] + \
          [chr(x) for x in range(33,48)]
          
numbers = [chr(x) for x in range(48,58)]

letter_choices = [random.choice(letters) for _ in range(letter_count)]
symbol_choices = [random.choice(symbols) for _ in range(symbol_count)]
number_choices = [random.choice(numbers) for _ in range(number_count)]

total = letter_choices + symbol_choices + number_choices
print(total)

random.shuffle(total)
print(total)

print(f"Your password is: {''.join(total)}")
