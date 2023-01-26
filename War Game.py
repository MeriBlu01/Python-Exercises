#  Milestone Project 2

# WAR game
import random 
# from random import shuffle

# Global variables for Card Class
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# Card Class

# Suit, Rank, Value
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    # Let's define what we want to print
    def __str__(self):
        return self.rank + " of " + self.suit


# Deck Class

# Instantiate a new deck
#   Create all 52 Card objects
#   Hold as a list of Card objects
# Shuffle a Deck through a method call
#   Random library shuffle() function
# Deal cards from the Deck object
#   Pop method from cards list

class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # Create the Card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# Player Class 

# The last thing we need to think about is 
# tranlating a Deck/Hand of cards with a top
# and bottom, to a Python list.

# .append("x") -> Agrega a x al final de la lista, append es sólo para un item. 
#                 Porque append puede crear listas anidadas.
# .extend(new) -> 'new' es el nombre de una lista, se agrega por def al final. extend es para agregar múltiples items

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        # To delete the top card.
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)


    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards.'


# Game Logic

# Game Setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# len(player_two.all_cards)
# len(player_two.all_cards)

game_on = True
# Counter
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    # Check if there's already a winner.
    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print('\nPlayer One, out of cards!, Player Two ¡WINS!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('\nPlayer Two, out of cards!, Player One ¡WINS!')
        game_on = False
        break
    
    # Otherwise, the game is still on!

    # START A NEW ROUND
    # and reset the current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # Check the player's cards against each other
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            # No longer at "war", time for next round
            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            # No longer at "war", time for next round
            at_war = False
        else:
            print("War!")
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First, check to see if a player is out of cards:

            if len(player_one.all_cards) < 5:
                print("\nPlayer One unable to declare war")
                print("Player TWO WINS!")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("\nPlayer Two unable to declare war")
                print("Player ONE WINS!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                # Higher value means shorter games
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

            

# ------------------------------------
two_hearts = Card("Hearts", "Two")
print(two_hearts)
# -------------------------------------
new_deck = Deck()
# new_deck.all_cards
first_card = new_deck.all_cards[0] 
print(first_card)

new_deck.shuffle()

last_card = new_deck.all_cards[-1] 
print(last_card)

my_card = new_deck.deal_one()
print(my_card)
len(new_deck.all_cards)
# ------------------------------------
new_player = Player("Mely") 
print(new_player)

new_player.add_cards(my_card)

print(new_player)
print(new_player.all_cards[0])
print(new_player.all_cards[1])

new_player.remove_one()