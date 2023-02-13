# Blackjack

import random

# Gloabal variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
        'Queen':10, 'King':10, 'Ace':11}

# Rules
# 1. Blackjack hands are scored by their total points. 
# 2. The hand with the highest total wins as long as it doesn't exceed 21.
# 3. A hand with a higher total than 21 is called 'BUSTED'. 
# 4. Cards 2 through 10 are worth their face value, and face cards (jack, queen, king) are also worth 10.
#    An ace's value is 11 unless this would cause the player to bust, in which case it is worth 1. 
# 5. A hand in which an ace's value is counted as 11 is called a SOFT HAND, 
#    because it cannot be busted if the player draws another card.
# 6. Note that if the player busts he loses, even if the dealer also busts 
#    (therefore Blackjack favors the dealer). 
# 7. If both the player and the dealer have the same point value, it is called a "PUSH", 
#    and neither player nor dealer wins the hand.
# 8. A two-card hand of 21 (an ace plus a ten-value card) is called a "blackjack" or a "natural", 
#    and is an automatic winner. A player with a natural is usually paid 1.5 on his bet. 
# 9. The rules specify that the cards must be dealt from a shoe containing either four or six packs 
#    of cards. In this case, just use 3.
# 10. If the score of the player hand is equal or less than 16, has to take one more card.


# The play goes as follows:

# If the dealer has blackjack and the player doesn't, DEALER WINS (paid DOUBLE on his bet).
# If the player has blackjack and the dealer doesn't, PLAYER WINS.
# If both the player and dealer have blackjack then it's a PUSH.
# If neither side has blackjack, then each player plays out his hand, one at a time.
# When all the players have finished the dealer plays his hand.

# The player's options for playing his or her hand are:
# Hit: Take another card.
# Stand: Take no more cards.

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

        # due to clause 9
        for _ in range(3):
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
# .extend(new) -> 'new' es el nombre de una lista, se agrega por def al final. 
#                 Extend es para agregar múltiples items

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.actual_score = [0,0]
        self.actual_status = ''
    
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
    
    def score(self):
        # The actual score of the player
        self.actual_score = [0,0]
        # actual hand
        for card in range(len(self.all_cards)):   
            self.actual_score[0] += self.all_cards[card].value
        # ace hand
        ace_count = 0 
        for card in range(len(self.all_cards)):  
            if self.all_cards[card].value == 11:
                ace_count += 1
        # 2. Check actual hand and possible hand with ace
        hand = self.actual_score[0]
        if ace_count != 0:
            hand_n_aces = hand - (ace_count * 10)
            self.actual_score[1] = hand_n_aces
        else: self.actual_score[1] = hand
        # 3. Check possible status
        self.status()

    def status(self):
        hand = self.actual_score[0]
        hand_n_aces = self.actual_score[1]
        if hand > 21 and hand_n_aces > 21:
            self.actual_status = 'B' # Busted!
        elif hand == 21 or hand_n_aces == 21:
            self.actual_status = 'W' # Winner!
        elif hand < 21 or hand_n_aces < 21:
            self.actual_status = 'S' # Saved! 

    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards.'

# Shows the actual hand
def show_hand(hand):
    for card in range(len(hand)):   
        print("- "+str(hand[card]))
    
# Asking for the bet
def take_bet(credit):
    while True:
        bet = int(input("How much will you bet? "))   #   5.0
        if bet <= credit:
            print("\nWell done!, let's play with your {} credits.".format(bet))
            break
        else: 
            print("NOT reasonable. Try again!")
    return bet


def prize(status, bet, credit):
    
    if status == 'W':
        credit += bet
        print("\n¡WOW!, You're so LUCKY!")
        s = "profit:"
    elif status == 'L':   
        credit -= bet
        print("\nSorry, DEALER WINS")
        s = "loss:"
    else:  # 'D' for double winning!
        credit += bet * 2
    print("Your {} {}, and your new credit {}".format(s,bet, credit))
    return credit
    
# ---------------------------------------------------------------------------------------------

# Game Logic

# Game Setup
player_one = Player("One")
dealer = Player("Dealer")

new_deck = Deck()
new_deck.shuffle()
len(new_deck.all_cards)

# print(len(dealer.all_cards))
# print(len(player_one.all_cards))

# Initialize CREDIT
credit = 100   # For default

round_counter = 0
game_On = True
stand = False
while game_On:
    print("\nRound: {}".format(round_counter))
    print("Your actual credit is {}".format(credit))

    new_deck.shuffle()

    if round_counter == 0:
        
        # Asking for BET
        bet = take_bet(credit)

        # Deal two cards to the Dealer and two cards to the Player
        for x in range(2):
            player_one.add_cards(new_deck.deal_one())
            dealer.add_cards(new_deck.deal_one())
    
        # Showing Dealer's One Card face Up
        print("\nDealer's face up card...")
        print(dealer.all_cards[0])

    # Showing Player's cards
    print("\n> Your cards player...")
    show_hand(player_one.all_cards)
    
    # Check status: WINNER/BUSTED/SAVED and score
    player_one.score()
    dealer.score()
    
    # Player Actual Status:
    status_player = player_one.actual_status
    # Dealer Actual Status:
    status_dealer = dealer.actual_status
    
    # Player's possible hands score
    p_hand = player_one.actual_score[0]
    p_ace_hand = player_one.actual_score[1]
    # Dealer's hand score
    d_hand = dealer.actual_score

    # Ask player next move if it's allowed
    if status_player == 'S' and p_hand > 16 or p_ace_hand > 16:
        print("\nPlayer, what would be your next move?...")
        while True: 
            move = input("HIT or STAND? (H/S):")
            move = move.upper()
            if move == 'H':
                new_deck.shuffle()
                player_one.add_cards(new_deck.deal_one())
                player_one.score()
                if sum(d_hand) <= 32:
                    dealer.add_cards(new_deck.deal_one())
                    dealer.score()
                break
            elif move == 'S':       
                print("Hmm, good hand?")
                stand = True
                # Showing Dealer's cards
                print("\n> Dealer's Hand:")
                show_hand(dealer.all_cards) 
                break
            else: 
                print("Huh?, try again!")
    elif status_player == 'S' and p_hand <= 16 and p_ace_hand <= 16:
        print("\nPlayer with no rights haha...")
        new_deck.shuffle()
        player_one.add_cards(new_deck.deal_one())
        player_one.score()
        if sum(d_hand) <= 32:
                    dealer.add_cards(new_deck.deal_one())
                    dealer.score()
    
    # Dealers hand updated
    d_hand = dealer.actual_score

    # Determine the winner and adjust the Player's chips accordingly
    new_status = player_one.actual_status
    
    p_full_hand = player_one.actual_score
    keep_playing_ask = False
    if new_status == 'W' and d_hand[0] != 21 and d_hand[1] != 21:
        # Scenario 1
        if len(player_one.all_cards) == 2:
            print("\n¡WOW!, you got a ¡NATURAL WINNING!")
            credit = prize('W', bet, credit)
        else: 
            print("\n¡WOW!, you got a ¡DOUBLE WINNING!")
            print("Recover your bet and plus Dealer's bet HAHA")
            credit = prize('D', bet, credit)
        keep_playing_ask = True
    elif new_status == 'W' and (d_hand[0] == 21 or d_hand[1] == 21):
        # Scenario 2
        print("\nSorry, It's a PUSH!...")
        print("You keep your credit as {}".format(bet, credit))
        keep_playing_ask = True
    elif new_status == 'S' and d_hand[0] == 21 or d_hand[1] == 21:
        # Scenario 3
        credit = prize('L', bet, credit)
        keep_playing_ask = True
    elif new_status == 'B':
        # Scenario 4
        print("\nBUSTED!")
        credit = prize('L', bet, credit)
        keep_playing_ask = True
    elif new_status == 'S' and stand == True:
        # Scenario 5
        best_play = max(p_full_hand)
        if best_play > 21:
            if p_full_hand.index(best_play) == 0:
                best_play = p_full_hand[1]
            else: best_play = p_full_hand[0]
        best_dealer_hand = max(d_hand)
        if best_dealer_hand > 21:
            if d_hand.index(best_dealer_hand) == 0:
                best_dealer_hand = d_hand[1]
            else: best_dealer_hand = d_hand[0]
        if best_play > best_dealer_hand or best_dealer_hand > 21:
            credit = prize('W', bet, credit)
        else: 
            credit = prize('L', bet, credit)
        keep_playing_ask = True

    round_counter += 1

    # show actual player score
    # print("\n<< Player Actual Score >> : "+str(player_one.actual_score))

    # Asks player if he still wanna play
    while keep_playing_ask == True: 
        
        # Showing Dealer's cards since there was already a winner
        if stand == False:
            print("\n> Dealer's Hand:")
            show_hand(dealer.all_cards)
        # Showing Dealer's cards since there was already a winner
        print("\n> Player's Hand:") 
        show_hand(player_one.all_cards)

        # Reset the rounds
        round_counter = 0
        player_one.all_cards.clear()
        dealer.all_cards.clear()
        player_one.actual_status = ''
        stand = False
        
        # Player it's out of credit?
        if credit > 0:
            # If it's not ask if player wanna keep playing
            play = input("\nDo you wanna keep playing? (Y/N) ")
            play = play.upper()
            if play == 'Y':
                game_On = True
                keep_playing_ask = False
            elif play == 'N':     
                
                game_On = False
                keep_playing_ask = False
            else: 
                print("Huh?, try again!")
        else:
            print("\nOh noooo... You are out of credit\n\
            Thank you for play. See you later...")
            game_On = False
            keep_playing_ask = False

