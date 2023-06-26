# A tic tac toe game that can be played against the computer or another player

import random

from board import Board

# Global variables
board = Board()
game_state = True
announce = ""

play_against_computer = False
player_mark = "Not set yet"


def play_game():
    reset_game()
    global announce, play_against_computer, player_mark

    # ask player if he wants to play against the computer
    play_against_computer = (
        input("Do you want to play against the computer? y/n ") == "y"
    )

    # ask player if he wants to be X or O
    player_mark = input("Do you want to be X or O? ").upper()
    while player_mark not in ["X", "O"]:
        player_mark = input("Please choose X or O: ").upper()

    # Set marks
    mark_x = "X"
    mark_o = "O"
    while True:
        # Show board
        print("\n" * 100)
        display_board()

        if play_against_computer:
            # Player X turn
            game_state, announce = player_choice(mark_x)
            print(announce)
            if game_state is False:
                break

            # Player O turn
            game_state, announce = computer_choice(mark_o)
            print(announce)
            if game_state is False:
                break
        else:
            # Player X turn
            game_state, announce = player_choice(mark_x)
            print(announce)
            if game_state is False:
                break

            # Player O turn
            game_state, announce = player_choice(mark_o)
            print(announce)
            if game_state is False:
                break

    # Ask player for a rematch
    rematch = input("Would you like to play again? y/n ")
    if rematch == "y":
        play_game()
    else:
        print("Thanks for playing!")


# Note: Game will ignore the 0 index
def reset_game():
    global board, game_state, play_against_computer
    board = Board()
    game_state = True
    play_against_computer = False


def display_board():
    """This function prints out the board so the numpad can be used as a reference"""
    # Clear current cell output
    print("\n" * 100)
    # Print board
    print(repr(board) + "\n")


def player_choice(mark):
    global board, game_state, announce
    # Set game blank game announcement
    announce = ""
    # Get Player Input
    mark = str(mark)
    # Validate input
    ask_player_for_move(mark)

    # Check for player win
    if board.get_winner() == mark:
        print("\n" * 100)
        display_board()
        announce = mark + " wins! Congratulations"
        game_state = False

    # Show board
    print("\n" * 100)
    display_board()

    # Check for a tie
    if board.is_full():
        announce = "Tie!"
        game_state = False

    return game_state, announce


def computer_choice(mark):
    global board, game_state, announce
    # Set game blank game announcement
    announce = ""
    # Get Player Input
    mark = str(mark)

    # search for a winning move
    search_for_best_move(mark)

    # Check for player win
    if board.get_winner() == mark:
        print("\n" * 100)
        display_board()
        announce = mark + " wins! Congratulations"
        game_state = False

    # Show board
    print("\n" * 100)
    display_board()

    # Check for a tie
    if board.is_full():
        announce = "Tie!"
        game_state = False

    return game_state, announce


def search_for_best_move(mark):
    """Search for the best move to make"""
    global board
    # search for a winning move
    for i in range(1, 10):
        if board[i] == " ":
            board[i] = mark
            if board.get_winner() == mark:
                return
            else:
                board[i] = " "

    # search for a blocking move
    if mark == "X":
        mark = "O"
    else:
        mark = "X"
    for i in range(1, 10):
        if board[i] == " ":
            board[i] = mark
            if board.get_winner() == mark:
                board[i] = "O"
                return
            else:
                board[i] = " "

    # search for a random move

    return make_random_move(random)


def make_random_move(random):
    while True:
        i = random.randint(1, 9)
        if board[i] == " ":
            board[i] = "O"
            return


def win_check(board, player):
    """Check Horizontals, Verticals, and Diagonals for a win"""
    return board.get_winner() == player


def ask_player_for_move(mark):
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


print("Welcome to Tic Tac Toe!")
play_game()

# End of program
