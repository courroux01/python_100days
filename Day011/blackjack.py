import random

VALUES = [str(x) for x in range(2, 11)] + ["J", "Q", "K", "A"]
SUITS = ["H", "S", "D", "C"]
CARDS = [[value, suit, True] for value in VALUES for suit in SUITS]

def generate_card_picture(card):
    value, suit, isFacingUp = card
    generated_card_picture = []
    
    if(isFacingUp):
        value, suit = (f'{value} ' if len(str(value)) < 2 else str(value), f'{suit}')
    
        generated_card_picture.append(f'.------.')
        generated_card_picture.append(f'| {value}   |')
        generated_card_picture.append(f'|      |')
        generated_card_picture.append(f'|      |')
        generated_card_picture.append(f'|      |')
        generated_card_picture.append(f'|   {suit}  |')
        generated_card_picture.append(f'|______|')
    else:
        generated_card_picture.append(f'.------.')
        generated_card_picture.append(f'|      |')
        generated_card_picture.append(f'|      |')
        generated_card_picture.append(f'|      |')
        generated_card_picture.append(f'|      |')
        generated_card_picture.append(f'|      |')
        generated_card_picture.append(f'|______|')
        
    return generated_card_picture

def get_card_value(card, isOverTen=False):
    value = card[0]
    if(value.isnumeric()):
        return int(value)
    elif(value == 'A'):
        if(isOverTen):
            return 1
        else:
            return 10
    else:
        return 10

def shuffle_cards():
    current_cards = [x for x in CARDS]
    random.shuffle(current_cards)
    return current_cards

def get_random_card(current_cards, card_count=1):
    return (current_cards[:card_count], current_cards[card_count:])

def hide_card(card):
    card[2] = False
    return card

def long_line():
    print("=======================================")
    
    
def print_round_card_values(player_cards, dealer_cards):
    player_value = 0
    dealer_value = 0
    
    for p_card, d_card in zip(player_cards, dealer_cards):
        player_value += get_card_value(p_card)
        dealer_value += get_card_value(d_card)
    
    print(f"Player: {player_value}, Dealer: {dealer_value}")

def get_round_card_pictures(player_cards, dealer_cards):
    return (
        [hide_card(c) for c in player_cards],
        [hide_card(dealer_cards[0]), dealer_cards[1:]]
    )
    
def print_round_cards(player_cards, dealer_cards):
    long_line()
    player_card_pictures = [generate_card_picture(card) for card in player_cards]
    dealer_card_pictures = [generate_card_picture(card) for card in dealer_cards]
    
    print("Player Cards:")
    for player_card_picture in zip(player_card_pictures[0], player_card_pictures[1]):
        for row in player_card_picture:
            print(row, end=' ')
        print()
               
    print("Dealer Cards:")
    for dealer_card_picture in zip(dealer_card_pictures[0], dealer_card_pictures[1]):
        for row in dealer_card_picture:
            print(row, end=' ')
        print()
    
    long_line()    
    
def get(s, reqs):
    while True:
        print(s)
        inp = input()
        
        if not all([each(inp) for each in reqs]):
            print("Invalid input. Please try again. ")
        else:
            return inp
        
def play_round(player_cards, dealer_cards, current_cards):
    long_line()
    while True:
        choice = get(
            "Hit or Stand?",
            [
                lambda x: x in ['Hit', 'Stand']
            ]
        )
        
        if choice == 'Hit':
            
    
def blackjack():
    current_cards = shuffle_cards()
    
    player_cards, current_cards = get_random_card(current_cards, 2)
    dealer_cards, current_cards = get_random_card(current_cards, 2)
    
    dealer_cards[0] = hide_card(dealer_cards[0])
    
    print_round_cards(player_cards, dealer_cards)
    print_round_card_values(player_cards, dealer_cards)
    
    play_round(player_cards, dealer_cards, current_cards)
    
    
    
blackjack()    

    
