def create_board():
    # Creates a fresh board
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    return board


def choose_symbol():
    # the function lets users choose their symbols
    player_1_symbol = input("Please enter which symbol you would like to use: 'X' or 'O': ").upper()
    if player_1_symbol == "X":
        player_2_symbol = "O"
    else:
        player_2_symbol = 'X'

    return player_1_symbol, player_2_symbol


def whose_turn_is_it(first_player, second_player):
    # function says whose turn it is to play
    if count % 2 == 0:
        return first_player
    elif count == 1:
        return second_player
    else:
        return second_player


# creating the board
board_in_play = create_board()
print(board_in_play)

# choosing the symbols for players
player_1, player_2 = choose_symbol()

# initiating count
count = 0
winner = False

while count < 9:
    player = whose_turn_is_it(player_1, player_2)
    print(f'Its your turn Player {player}')
    row = int(input("Please enter the row you would like to place your symbol. rows are counted "
                    "from top to bottom with the top row having a value of 0, middle row with 1 and bottom "
                    "row with a value 2: "
                    ))
    column = int(input("Please enter the column you would like to place your symbol"
                       "The columns are counted from left to right with the left most column having a "
                       "value of 0, middle column with 1 and the right most column having the value of 2: "
                       ))

    # Check if the rows or columns are out of board
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        print("Please input a valid value, row or column out of board ")
        row = int(input("Please enter the row you would like to place your symbol. rows are counted "
                        "from top to bottom with the top row having a value of 0, middle row with 1 and bottom "
                        "row with a value 2: "
                        ))
        column = int(input("Please enter the column you would like to place your symbol"
                           "The columns are counted from left to right with the left most column having a "
                           "value of 0, middle column with 1 and the right most column having the value of 2: "
                           ))

    # Check if the row and column is already filled
    while (board_in_play[row][column] == 'X') or (board_in_play[row][column] == 'O'):
        print("Please input a valid value, box is already filled!")
        row = int(input("Please enter the row you would like to place your symbol. rows are counted "
                        "from top to bottom with the top row having a value of 0, middle row with 1 and bottom "
                        "row with a value 2: "
                        ))
        column = int(input("Please enter the column you would like to place your symbol"
                           "The columns are counted from left to right with the left most column having a "
                           "value of 0, middle column with 1 and the right most column having the value of 2: "
                           ))

    board_in_play[row][column] = player
    print(board_in_play)

    # check the rows for a winner
    for row in range(0, 3):
        if board_in_play[row][0] == board_in_play[row][1] == board_in_play[row][2] == player:
            print(f"Player {player} won!!!")
            winner = True
            count = 10

    # check the columns for a winner
    for column in range(0, 3):
        if board_in_play[0][column] == board_in_play[1][column] == board_in_play[2][column] == player:
            print(f"Player {player} won!!!")
            winner = True
            count = 10

    # check the diagonals for a winner

    if board_in_play[0][0] == board_in_play[1][1] == board_in_play[2][2] == player:
        print(f"Player {player} won!!!")
        winner = True
        count = 10
    if board_in_play[0][2] == board_in_play[1][1] == board_in_play[2][0] == player:
        print(f"Player {player} won!!!")
        winner = True
        count = 10

    if count >= 9 and winner != True:
        print("It's a draw")

    count += 1
