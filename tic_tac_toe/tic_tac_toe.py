# A tic tac toe game that can be played against the computer or another player

# Global variables
board = [" "] * 10
game_state = True
announce = ""


def play_game():
    reset_board()
    global announce

    # Set marks
    X = "X"
    O = "O"
    while True:
        # Show board
        print("\n" * 100)
        display_board()

        # Player X turn
        game_state, announce = player_choice(X)
        print(announce)
        if game_state == False:
            break

        # Player O turn
        game_state, announce = player_choice(O)
        print(announce)
        if game_state == False:
            break

    # Ask player for a rematch
    rematch = input("Would you like to play again? y/n ")
    if rematch == "y":
        play_game()
    else:
        print("Thanks for playing!")


# Note: Game will ignore the 0 index
def reset_board():
    global board, game_state
    board = [" "] * 10
    game_state = True


def display_board():
    """This function prints out the board so the numpad can be used as a reference"""
    # Clear current cell output
    print("\n" * 100)
    # Print board
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])


def player_choice(mark):
    global board, game_state, announce
    # Set game blank game announcement
    announce = ""
    # Get Player Input
    mark = str(mark)
    # Validate input
    ask_player(mark)

    # Check for player win
    if win_check(board, mark):
        print("\n" * 100)
        display_board()
        announce = mark + " wins! Congratulations"
        game_state = False

    # Show board
    print("\n" * 100)
    display_board()

    # Check for a tie
    if full_board_check(board):
        announce = "Tie!"
        game_state = False

    return game_state, announce


def win_check(board, player):
    """Check Horizontals, Verticals, and Diagonals for a win"""
    return (
        win_check_horizontal(board, player)
        or win_check_vertical(board, player)
        or win_check_diagonal(board, player)
    )


def win_check_horizontal(board, player):
    return (
        (board[7] == board[8] == board[9] == player)
        or (board[4] == board[5] == board[6] == player)
        or (board[1] == board[2] == board[3] == player)
    )


def win_check_vertical(board, player):
    return (
        (board[7] == board[4] == board[1] == player)
        or (board[8] == board[5] == board[2] == player)
        or (board[9] == board[6] == board[3] == player)
    )


def win_check_diagonal(board, player):
    return (board[1] == board[5] == board[9] == player) or (
        board[3] == board[5] == board[7] == player
    )


def ask_player(mark):
    """Asks player where to place X or O mark, checks validity"""
    global board
    req = "Choose where to place your " + mark + ": "
    while True:
        try:
            choice = int(input(req))
        except ValueError:
            print("Sorry, please input a number between 1-9.")
            continue

        if choice not in range(1, 10):
            print("Sorry, please input a number between 1-9.")
            continue

        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print("That space isn't empty!")


def full_board_check(board):
    """Function to check if any remaining blanks are in the board"""
    return " " not in board[1:]


play_game()

# End of program
