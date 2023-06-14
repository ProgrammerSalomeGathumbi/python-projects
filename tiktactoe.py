#!/usr/bin/python3
"""
This is a tictactoe game to practice my python.
"""
from os import system, name
from time import sleep

board = [' '] * 9
current_player = 'X'  # Assuming 'X' always starts the game


def clear_screen():
    """Clears the terminal screen"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def display_board():
    """Function to display the game board"""
    clear_screen()
    print("------------")
    for i in range(0, 9, 3):
        print("| " + board[i] + " | " + board[i+1] + " | " + board[i+2] + " |")
        print("--------------")


def get_player_move():
    """Handles players input"""
    position = input("Enter your move (1-9): ")

    if position.isdigit():
        position = int(position) - 1
        if position in range(9) and board[position] == ' ':
            return position
        else:
            print("Invalid move. Please try again.")
            return get_player_move()
    else:
        print("Sorry, that is not a valid input. Please try again.")
        return get_player_move()


def update_board(position, symbol):
    """Update the board with the player's symbol at the chosen position"""
    board[position] = symbol


def check_win():
    """Implement the logic to check for a win"""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combination in winning_combinations:
        a, b, c = combination
        if board[a] == board[b] == board[c] != ' ':
            return True  # Win condition met

    return False


def check_tie():
    """Check if the game ended in a tie"""
    return ' ' not in board


def play_game():
    """Main game loop"""
    global current_player
    clear_screen()
    print("Welcome to Tic-Tac-Toe!")

    current_player = input("Choose your symbol (X or O): ").upper()
    while current_player not in ['X', 'O']:
        print("Invalid symbol. Please choose 'X' or 'O'.")
        current_player = input("Choose your symbol (X or O): ").upper()
    while True:
        display_board()
        print("It's Player", current_player, "'s turn.")
        position = get_player_move()
        update_board(position, current_player)
        if check_win():
            display_board()
            print("Player", current_player, "wins!")
            break
        elif check_tie():
            display_board()
            print("It's a tie!")
            break
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        reset_game()
        play_game()


def reset_game():
    """Resets the game board"""
    global board
    board = [' '] * 9


play_game()
