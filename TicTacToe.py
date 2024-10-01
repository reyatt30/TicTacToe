#-------Golbal Variables----------

#Game Board
board = ["-","-","-",       #   0 1 2
         "-","-","-",       #   3 4 5
         "-","-","-",]      #   6 7 8  

#If game is still going 
game_still_going = True

#Who won? Or Tie?
winner = None

#Who's turn is it?
current_player = "X"

# Display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Play Game of Tic Tac Toe
def play_game():
    #Displays the initial board
    display_board()

    # While the game is still going
    while game_still_going:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Checks if the game has ended
        check_if_over()

        # Flip to the other player
        flip_player()

    #The Game has ended
    if winner == "X" or winner == "O":
        print(f"{winner} won.")
    elif winner == None:
        print("Tie.")


# Handle a single turn of each player
def handle_turn(player):

    print(f"{player}'s turn.")
    position = input("Choose a position from 1-9: ") 

    valid = False

    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ") 

            #Takes the position and subtracts it by one to match the index
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there! Go again")

        #Puts the player on the board
    board[position] = player
    display_board() 

# Checks if the game is over
def check_if_over():
    check_for_winner()
    check_if_tie()
#Checks if the player won
def check_for_winner():

    #Accesses the Global Variable set outside of the function
    global winner

    #Check Rows
    row_winner = check_rows()
    #Check Columns
    column_winner = check_columns()
    #Check Diagonals 
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return
#Checks if it's a tie
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return
#Flips to the other persons turn
def flip_player():
    #Calls Global Variable from outside of the function
    global current_player
    #If the current player who just went is X, it flips to O
    if current_player == "X":
        current_player = "O"
    #If the current player who just went is O, it flips to X
    elif current_player == "O":
        current_player = "X"
    return

def check_rows(): 
    # Sets up the Global Variable
    global game_still_going
    # Checks if the rows are equal to each other
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    #If any row does have a match, flag that it is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Returns the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    # Sets up the Global Variable
    global game_still_going
    # Checks if the columns are equal to each other
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    #If any column does have a match, flag that it is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Returns the winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    # Sets up the Global Variable
    global game_still_going
    # Checks if the columns are equal to each other
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[6] == board[4] == board[2] != '-'
 
    #If any column does have a match, flag that it is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Returns the winner X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]

    return 


play_game() 