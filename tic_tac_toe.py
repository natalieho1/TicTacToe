'''
Purpose: A tic tac toe game that runs in the terminal.
Author: Natalie Ho 
Date: April 20, 2025
'''

def print_board(board):
    '''
    Prints out the board for players to see. 
    '''
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")

def get_player_move(board, player_name, player_symbol):
    '''
    Asks players to choose where to put an X or O. 
    '''
    # set a while loop so the player can only enter a valid move
    while True:
        try:
            move = int(input(f"{player_name} ({player_symbol}) choose a position (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Choose a number from 1 to 9.")
            elif board[move - 1] != " ":
                print("That spot is already taken. Try again.")
            else:
                # subtract 1 because players will use positions 1-9 but indexing uses 0-8. 
                return move - 1
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_win(board, symbol):
    '''
    Check for wins. 
    '''
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == symbol for i in condition):
            return True
    return False

def check_tie(board):
    '''
    Check for ties. 
    '''
    return all(space != " " for space in board)

player1_name = input("Enter name for Player 1 (X): ")
player2_name = input("Enter name for Player 2 (O): ")


board = [" " for _ in range(9)]

current_name = player1_name
current_symbol = "X"

while True:
    print_board(board)
    move = get_player_move(board, current_name, current_symbol)
    board[move] = current_symbol

    # check if game is over
    if check_win(board, current_symbol):
        print_board(board)
        print(f"🎉 {current_name} ({current_symbol}) wins!")
        break
    # check if there is a tie 
    elif check_tie(board):
        print_board(board)
        print("It’s a tie!")
        break

    # Switch players
    if current_symbol == "X":
        current_symbol = "O"
        current_name = player2_name
    else:
        current_symbol = "X"
        current_name = player1_name
