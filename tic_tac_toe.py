from random import randrange

def display_board(board):
    line = "+-------+-------+-------+"
    empty = "|       |       |       |"
    print(line)
    for row in board:
        print(empty)
        print("|   " + str(row[0]) + "   |   " + str(row[1]) + "   |   " + str(row[2]) + "   |")
        print(empty)
        print(line)

def enter_move(board):
    while True:
        move = input("Enter your move: ")
        if not move.isdigit():
            print("Invalid input. Enter a number from 1 to 9.")
            continue
        move = int(move)
        if move < 1 or move > 9:
            print("Invalid number must be between 1 and 9.")
            continue
        row = (move - 1) // 3
        col = (move - 1) % 3
        if board[row][col] in ('X', 'O'):
            print("That square is already taken.")
            continue
        board[row][col] = 'O'
        return

def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ('X', 'O'):
                free.append((row, col))
    return free

def victory_for(board, sign):
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False


def draw_move(board):
    free = make_list_of_free_fields(board)
    choice = free[randrange(len(free))]
    row, col = choice
    board[row][col] = 'X'


board = [[1, 2, 3],
         [4, 'X', 6],
         [7, 8, 9]]

display_board(board)

while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("You won!")
        break

    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("The computer won!")
        break

    if len(make_list_of_free_fields(board)) == 0:
        print("It's a tie!")
        break

