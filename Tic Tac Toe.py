# Tic Tac Toe Game

# We need to import randint for PC positions
from random import randint

# Variables Globales
taked = []
symbols_selected = []
matrix = []
counter = 0
welcome = 0
winner = 'Not yet'

# Start Button
game_status = 'On'

# This function is used to welcome the user to the game and to select the symbol [X/O]
def welcoming():
    symbol = ''
    avatars = [' ', ' ']
    welcome = True
    
    while welcome == True:
        
        symbol = input("¡HI!, Let's play TIC TAC TOE\nSelect your symbol: 'X' or 'O': ")
        symbol = symbol.upper()

        if symbol != 'O' and symbol != 'X':
            print("Ooops... symbol not vaild. TRY AGAIN...\n")
            welcome = True
        else: 
            if symbol == 'X':
                avatars = ['X','O']
            else: avatars = ['O','X']
            print("\nOK, Let's start XD\nYou will be the < {} >, and I the < {} > mark.\n".format(avatars[0], avatars[1]))
            welcome = False
            return avatars

# This function is for when it is the player's turn to select where to mark.
# This function checks if the entered input is valid and if it is a digit (range: 1-9).
def player_choice():
      
      # Variables
      choice = 'Wrong' 

      # Conditional variables
      within_range = False
      valid_range = range(1,10) # (1-9)

      # Two conditions to check
      while choice.isdigit() == False or within_range == False:
            choice = input('Please choose a number (1-9): ')
            
            # DIGIT CHECK
            if choice.isdigit() == False:
                print("That's not a digit darling...\n")
                within_range = False
            else: # RANGE CHECK
                if int(choice) in valid_range:
                    within_range = True
                    return int(choice)
                else: 
                    print("Sorry, you are out of acceptable range (1-9).\n")
                    within_range = False

# This function checks whether the point to be marked is empty or not.  
def empty_check(pick, records):
    empty = 0
    
    for i in records:
        if pick == i:
            empty = 1     # The position has already been chosen
            break
        else: 
            empty = 0     # Position is available
    
    if empty == 1:
        print("This is already marked, try again...\n")

    return empty

# It displays the current "screen"
def display_game(record):
    
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']
    
    matrix_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    # Odd are the player
    for i in record[0::2]:
    
        if i <= 3:
            row1[i-1] = player_sym
        elif i > 3 and i <= 6:
            row2[i-4] = player_sym 
        else:
            row3[i-7] = player_sym 
    
    # Pairs are the PC
    for i in record[1::2]:
    
        if i <= 3:
            row1[i-1] = pc_sym
        elif i > 3 and i <= 6:
            row2[i-4] = pc_sym 
        else:
            row3[i-7] = pc_sym 
    
    # Creates the list of the matrix
    for i in range(0,3):
        matrix_list[i] = row1[i]
        matrix_list[i+3] = row2[i]
        matrix_list[i+6] = row3[i]
    
    print("The current display:\n")
    print(row1[0]+' | '+row1[1]+' | '+row1[2])
    print("---------")
    print(row2[0]+' | '+row2[1]+' | '+row2[2])
    print("---------")
    print(row3[0]+' | '+row3[1]+' | '+row3[2])
    print("")
    return matrix_list

# This function will register the position chosen by the player... 
# after validating that the place is available, is a digit and within the range (1-9).
def recording():
    exit = False
    while exit == False:
        sel = player_choice()
        
        if empty_check(sel,taked) == 0:
            taked.append(sel)
            exit = True
        else:
            print("Reintenta con otro...\n")

# This function executes the position to be marked by the PC.
# After validating that the place is available.
def pc_turn():
    ranFlag = 'F'

    while ranFlag == 'F':
        pc = randint(1,9)
        
        if pc in taked:
            ranFlag = 'F'
        else: 
            ranFlag = 'T'
            taked.append(pc)
    print("EL valor elegido por la pc es: {}\n".format(pc))

# Check if the list is having 3 equal marks         
def isEqual(x):
    return all(i == x[0] for i in x)

# This function checks if the matrix is full, for the probability of a tie
def GameOver(matrix):
    Full_Flag = all(i != ' ' for i in matrix)
    # Returns TRUE if tha matrix is FULL
    return Full_Flag

# This function returns the winner symbol
def winner_test(current_display, player, pc):
    
    player_sym = player
    pc_sym = pc
    winner_sym = ''

    # Creates the rows from the matrix   
    # Horizontals
    row1 = current_display[0:3]
    row2 = current_display[3:6]
    row3 = current_display[6:9]
    # Diagonals
    row4 = [row1[0], row2[1], row3[2]]
    row5 = [row1[2], row2[1], row3[0]]
    # Verticals
    row6 = [row1[0], row2[0], row3[0]]
    row7 = [row1[1], row2[1], row3[1]]
    row8 = [row1[2], row2[2], row3[2]]

    # Time to check if there's already a winner
    # Horizontals
    if isEqual(row1) == True:
        winner_sym = row1[0]
    elif isEqual(row2) == True:
        winner_sym = row2[0]
    elif isEqual(row3) == True:
        winner_sym = row3[0]
    # Diagonals
    elif isEqual(row4) == True:
        winner_sym = row1[0]
    elif isEqual(row5) == True:
        winner_sym = row1[2]
    # Verticals
    elif isEqual(row6) == True:
        winner_sym = row1[0]
    elif isEqual(row7) == True:
        winner_sym = row1[1]
    elif isEqual(row8) == True:
        winner_sym = row1[2]
            
    # This conditional prints the winner 
    if winner_sym == pc_sym:
        print('La PC te ha superado, que sad "Homo Sapiens"\n')
        winner_sym = 'Yes'
    elif winner_sym == player_sym:
        print("¡Genial!, has superado a la PC crack.\n")
        winner_sym = 'Yes'
    else:
        winner_sym = 'Not yet'
    
    return winner_sym


# This function asks the player if he/she wants to continue playing
def GameON():
    looping  = True
    
    while looping == True: 
        decision = input("\nDo you want to keep playing (Y/N)?... ")
        decision = decision.upper()

        if decision != 'Y' and decision != 'N':
            print("\nOoops... I don't get it. RETRY AGAIN...\n")
            looping = True
        else: 
            if decision == 'Y':
                decision = 'On'
                print("\nLet's play!\n")
                looping = False
            else: 
                decision = 'Off'
                print("\nGoodbye!\n")
                looping = False
    
    return decision


# Tic Tac Toe Game
# ---------------------------------------------------------------------------------------------------

while game_status == 'On':
    
    if welcome == 0:
        
    # Welcome to the player, the player chooses his symbol
        symbols_selected = welcoming() 
        player_sym = symbols_selected[0]
        pc_sym = symbols_selected[1]
        welcome += 1
  
    # The player chooses the position to mark
    recording()

    # Turn of PC
    if counter < 4:
        pc_turn()

    # Rewrite all and update the game display.
    # Show current display so the player can choose again
    matrix = display_game(taked) 

    # Who wins? 
    winner = winner_test(matrix, player_sym, pc_sym)
    
    # If the matrix is full and no winner found, it's a TIE!
    full = GameOver(matrix)

    if winner == 'Not yet' and full == True:
        winner = 'Tie'
        print("This sucks, we're even.\n") 

    counter += 1

    # Reset & asks if you want to keep playing
    if winner == 'Yes' or winner == 'Tie':
        # Reset variables
        counter = 0
        taked.clear()
        symbols_selected.clear()
        matrix.clear()
        winner = 'Not yet'
        # Keep playing?
        game_status = GameON()
        if game_status == 'Off':
            print("*****************************************\n")
            welcome = 0    