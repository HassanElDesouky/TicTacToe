
# Tic Tac Toe
"""
Analyzing the project:
    board of 9 cells
    the user will navigate to his desired cell
    he will type either X or O in a the cell
    if the user get three Xs or Os in an order (H/V/Crossed)
        will win
    else
        will lose
    if the game ended and either of the users have the three Xs or Os in an order
        the game will end and no one will be countered as a winner

"""

# draw board function


def draw_board():
    board: str = ""
    for _ in range(3):
        board += "|"
        board += "_"
        board += "|"
        for __ in range(2):
            board += "_"
            board += "|"
        board += "\n"
    return board

# main

# print new line


print("")


# get the board and print it
board = draw_board()
print(board)

# keep tracking of how many times the user entered a value
user_input_counter = 0

# update the game
while user_input_counter < 9:
    # update user input counter
    user_input_counter += 1

    # vars
    cell_position = int(input())
    user = input()
    counter = 0
    # new board as a temp
    temp_board = ""

    # update the board with the new user's input value
    for c in board:
        if c == '_':
            counter += 1
            if counter == cell_position:
                temp_board += user
            else:
                temp_board += "_"
        else:
            temp_board += c

    # assign the new board to the original board
    board = temp_board
    print(board)

    # array of pure user inputs
    test = [c for c in board if c != "|" and c != "\n"]
    print(test)