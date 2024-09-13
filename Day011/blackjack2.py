import random

class Helpers:
    @staticmethod
    def get(s, reqs=[]):
        while True:
            print(s)
            inp = input()
            
            if not reqs or all([each(inp) for each in reqs]):
                return inp
                
            else:
                print("Invalid input. Please try again. ")
            
            
    @staticmethod
    def longline():
        print("======================================")
        
class Card:
    VALUES = [str(x) for x in range(2, 11)] + ['J', 'Q', 'K', 'A']
    SUITS = ['C', 'S', 'D', 'H']
    IS_FACING_UP = [True, False]
    
    def __init__(self, value, suit, isFacingUp):
        self.value = value  # Use the setter to validate and assign
        self.suit = suit    # Use the setter to validate and assign
        self.isFacingUp = isFacingUp  # Use the setter to validate and assign

    # Getter for __value
    @property
    def value(self):
        return self.__value

    # Setter for __value
    @value.setter
    def value(self, value):
        if value in Card.VALUES:
            self.__value = value
        else:
            raise ValueError(f"Invalid value: {value}. Must be one of {Card.VALUES}")

    # Getter for __suit
    @property
    def suit(self):
        return self.__suit

    # Setter for __suit
    @suit.setter
    def suit(self, suit):
        if suit in Card.SUITS:
            self.__suit = suit
        else:
            raise ValueError(f"Invalid suit: {suit}. Must be one of {Card.SUITS}")

    # Getter for __isFacingUp
    @property
    def isFacingUp(self):
        return self.__isFacingUp

    # Setter for __isFacingUp
    @isFacingUp.setter
    def isFacingUp(self, isFacingUp):
        if isFacingUp in Card.IS_FACING_UP:
            self.__isFacingUp = isFacingUp
        else:
            raise ValueError(f"Invalid value for isFacingUp: {isFacingUp}. Must be one of {Card.IS_FACING_UP}")

        
    def __repr__(self):
        return f'Value: {self.value}, Suit: {self.suit}, IsFacingUp: {self.isFacingUp}'
    
    def getGameValue(self, isOverTen=False):
        value = self.value
        
        if(value.isnumeric()):
            return int(value)
        elif(value == 'A'):
            if(isOverTen):
                return 1
            return 11
        else:
            return 10
        
    def hideCard(self):
        self.isFacingUp = False
    
    def showCard(self):
        self.isFacingUp = True
    
    def getCardArrayPicture(self):
        value, suit, isFacingUp = self.value, self.suit, self.isFacingUp
        
        card_picture = []
        if(isFacingUp):
            value, suit = (f'{value} ' if len(str(value)) < 2 else str(value), f'{suit}')
        
            card_picture.append(f'.------.')
            card_picture.append(f'| {value}   |')
            card_picture.append(f'|      |')
            card_picture.append(f'|      |')
            card_picture.append(f'|      |')
            card_picture.append(f'|   {suit}  |')
            card_picture.append(f'|______|')
        else:
            card_picture.append(f'.------.')
            card_picture.append(f'|      |')
            card_picture.append(f'|      |')
            card_picture.append(f'|      |')
            card_picture.append(f'|      |')
            card_picture.append(f'|      |')
            card_picture.append(f'|______|')
            
        return card_picture
    
class Player:
    def __init__(self, name, isDealer=False):
        self.__Cards = []
        self.__CardArrayPictures = []
        self.__value = 0
        self.__isDealer = isDealer
        self.name = name
        
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()
    
    # Getter for __Cards
    @property
    def cards(self):
        return self.__Cards

    # Setter for __Cards
    @cards.setter
    def cards(self, value):
        if isinstance(value, list):
            self.__Cards = value
        else:
            raise ValueError("cards must be a list")

    # Getter for __CardArrayPictures
    @property
    def cardArrayPictures(self):
        return self.__CardArrayPictures

    # Setter for __CardArrayPictures
    @cardArrayPictures.setter
    def cardArrayPictures(self, value):
        if isinstance(value, list):
            self.__CardArrayPictures = value
        else:
            raise ValueError("cardArrayPictures must be a list")

    # Getter for __value
    @property
    def value(self):
        return self.__value

    # Setter for __value
    @value.setter
    def value(self, value):
        if isinstance(value, (int, float)):
            self.__value = value
        else:
            raise ValueError("value must be an integer or float")
        
    # Getter for __isDealer
    @property
    def isDealer(self):
        return self.__isDealer

    # Setter for __isDealer
    @isDealer.setter
    def isDealer(self, value):
        if isinstance(value, bool):
            self.__Cards = value
        else:
            raise ValueError("isDealer must be a boolean")

    def addCard(self, card):
        self.cards.append(card)
        self.value += card.getGameValue()
        self.cardArrayPictures.append(card.getCardArrayPicture())
    
    def updateCardArrayPictures(self):
        self.cardArrayPictures = [card.getCardArrayPicture() for card in self.cards]
        
    def hideCards(self):
        self.cards = [card.hideCard() for card in self.cards]
        
    def showCards(self):
        self.cards = [card.showCard() for card in self.cards]
    
    def describe(self, isGameFinished=False):
        Helpers.longline()
        print(f"{self.name}'s Cards: ")
        
        print(f"Value: {self.value if(not isGameFinished) else ""}")
            
        if(self.isDealer):
            if isGameFinished:
                self.cards[0].isFacingUp = True

            else:
                self.cards[0].isFacingUp = False
            
        self.updateCardArrayPictures()
            
        for playerCard_picture in zip(*self.cardArrayPictures):
            for row in playerCard_picture:
                print(row, end=' ')
            print()
            
        Helpers.longline()
        
        
class Game:
    CARDS = [Card(value, suit, True) for value in Card.VALUES for suit in Card.SUITS]
    
    def __init__(self):
        self.__gameCards = [x for x in Game.CARDS]
        self.players = []
        self.roundCount = 0
        
        self.initializeGame()
        
    @property
    def gameCards(self):
        return self.__gameCards

    @gameCards.setter
    def gameCards(self, cards):
        if isinstance(cards, list):
            self.__gameCards = cards
        else:
            raise ValueError("gameCards must be a list of cards")
                             
    def getRandomCard(self, player):
        randomCard, self.gameCards = self.gameCards[0], self.gameCards[1:]
        player.addCard(randomCard)
        return randomCard
        
    def welcome(self):
        Helpers.longline()
        print('Welcome to blackjack! Created by Abdullah Alojado.')
        Helpers.longline()
        
    def initializeGame(self):
        # Randomize Deck
        random.shuffle(self.gameCards)
    
        # Initialize players
        numberOfPlayers = int(Helpers.get(
            "How many players are playing? Minimum 1.",
            [
                lambda x: x.isnumeric() and int(x) > 0
            ]
        ))
        
        for _ in range(numberOfPlayers):
            playerName = Helpers.get(
                "Enter player name: ",
            )
            
            newPlayer = Player(playerName)
            self.players.append(newPlayer)
            
        for player in self.players:
            self.getRandomCard(player)
            self.getRandomCard(player)        
        
        # Initialize dealer
        dealer = Player("Game Dealer", True)
        self.getRandomCard(dealer)
        self.getRandomCard(dealer)  
        
        self.players.append(dealer)
        
        Helpers.longline()
        self.playRound()
    
    def playRound(self, playerIndex=0, goNext=False):
        self.describeRound()
        self.roundCount += 1
        
        canContinue = self.canContinue(playerIndex)
        
        if((not canContinue) or (goNext)):
            playerIndex += 1
            
        if(playerIndex >= len(self.players)):
            self.showResults()
            return
            
        player = self.players[playerIndex]
        print(f"Round {self.roundCount}: {player} plays.")
        
        if(playerIndex < len(self.players) - 1):
            choice = Helpers.get(
                f'{player}, Hit or Stand?',
                [
                    lambda x: x in ['Hit', 'Stand']
                ]
            )
            
            if(choice == 'Hit'):
                self.hit(playerIndex)
            else:
                self.stand(playerIndex)
        
        else:
            if(player.value < 17):
                self.hit(playerIndex)
            else:
                self.stand(playerIndex)
            
    def describeRound(self):
        print("Current round cards: ")
        for player in self.players:
            player.describe()
            
    def hit(self, playerIndex):
        player = self.players[playerIndex]
        randomCard = self.getRandomCard(player)
        print(f"{player} hits: {randomCard}. ")
        self.describeRound()
        self.playRound(playerIndex)
    
    def stand(self, playerIndex):
        player = self.players[playerIndex]
        print(f"{player} stands. ")
        self.playRound(playerIndex, goNext=True)
    
    def canContinue(self, playerIndex, goNext=False):
        return self.players[playerIndex].value <= 21 if not goNext else False

    def showResults(self):
        print("here")
        pass
        
            
            
class NewGame:
    def __init__(self):
        Game()
        
if __name__ == '__main__':
    NewGame()

"""
           def describeRound(self, isUserTurn=False):
        print("You: ")
        self.user.describe(True)
        
        print("Dealer: ")
        self.dealer.describe(False)
        
    def userChoose(self):
        choice = Helpers.get(
            f'{self.user} Hit or Stand?',
            [
                lambda x: x in ['Hit', 'Stand']
            ]
        )
        
        if(choice == 'Hit'):
            self.hit(self.user)
        else:
            self.stand(self.user)
            
    def playRound(self, player, isFirstRound=False):
        if(isFirstRound):
            self.getRandomCard(self.user)
            self.getRandomCard(self.user)
            self.getRandomCard(self.dealer)
            self.getRandomCard(self.dealer, isHidden=True)
            self.describeRound()
            self.userChoose()
        elif(player == self.user):
            self.userChoose()
        else:
            self.dealerChoose()
        
    def dealerChoose(self):
        if(self.dealer.value == 21 and len(self.dealer.cards) == 2):
            self.stand(self.dealer)
        elif(self.dealer.value >= 17):
            self.stand(self.dealer)
        else:
            self.hit(self.dealer)
       
    def hit(self, player):
        Helpers.longline()
        randomCard = self.getRandomCard(player)
        print(f'{player} Hit: {randomCard.value} of {randomCard.suit}')
        self.describeRound()
        Helpers.longline()
        self.continueGame(player)

    def continueGame(self, player, isUserStood=False):
        if(isUserStood):
            player = self.dealer
            player.showCards()
            
        if(self.isValidGame(player)):
            self.playRound(player)
        else:
            self.showResults()
            
    def stand(self, player):
        Helpers.longline()
        print(f"{player} stood!")
        self.describeRound()
        Helpers.longline()
        self.continueGame(player, True)
        
    def isValidGame(self, player):
        return player.value <= 21

    def playDealerRounds(self):
        self.describeRound()
        
        if(self.dealer.value == 21):
            self.showResults()
        elif(self.dealer.value >= 17):
            print("Dealer stood!")
            self.showResults()
        else:
            print("Dealer Hit!")
            self.getRandomCard(self.dealer)
            self.playDealerRounds()
        
    def showResults(self):
        self.describeRound()
        
        if(self.user.value > 21):
            print("You lost: Your total is over 21.")
        elif(self.dealer.value == 21):
            if(self.user.value == 21 and len(self.dealer.cards) <= len(self.user.cards)):
                print("You lost: Dealer has better blackjack.")
            else:
                print("You won! You had a better blackjack.")
        elif(self.dealer.value > 21):
            print("You won: Dealer bricked.")
        elif(self.user.value >= self.dealer.value):
            print("You won: You had better hands than the dealer.")
        else:
            print("You lost: Dealer had better hands than you.")
        
        self.playAgain()
    
    def playAgain(self):
        choice = Helpers.get(
            "Play again? Yes or No.",
            [
                lambda x: x in ['Yes', 'No']
            ]
        )
        
        if(choice == 'Yes'):
            NewGame()
        else:
            print("Thank you for playing!")
            return
            """