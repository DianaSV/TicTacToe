# https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

row_line = " ---"
column_line = "|"

def print_table(board):
    table_size = len(board) + 1
    for i in range(0, table_size):
        for j in range(0, table_size - 1):
            print(row_line, end='')
        print()
        if i == table_size - 1:
            break
        for j in range(0, table_size):
            if j < table_size - 1:
                print(column_line, "X" if board[i][j] == 1 else "O" if board[i][j] == 2 else " ", "", end='')
            else:
                print(column_line)

def check_rows(board):
    result = 0
    for row in range(len(board)):
        if board[row][0] != 0 and board[row][0] == board[row][1] == board[row][2]:
            result = board[row][0]
            break
    return result


def check_cols(board):
    result = 0
    for col in range(len(board[0])):
        if board[0][col] != 0 and board[0][col] == board[1][col] == board[2][col]:
            result = board[0][col]
            break
    return result


def check_diagonal(board):
    result = 0
    if board[0][0] != 0 and board[0][0] == board[1][1] == board[2][2]:
        result = board[0][0]
    if board[0][2] != 0 and board[0][2] == board[1][1] == board[2][0]:
        result = board[0][0]

    return result


def check_winner(board):
    result = check_diagonal(board)
    if result != 0:
        return result

    result = check_rows(board)
    if result != 0:
        return result

    result = check_cols(board)
    if result != 0:
        return result

    return result


def fillSpot(board, playerNum):
    result = 0
    spotTaken = True
    while(spotTaken):
        location = input("*** Player " + str(playerNum) + " ***: Please select empty location(Example: 1,3): ")
        before_comma_num = location.split(",")[0]
        after_comma_num = location.split(",")[1]
        # Verify location entered is correct
        while not before_comma_num.strip().isdigit() or not after_comma_num.strip().isdigit() \
                or int(before_comma_num) < 1 or int(before_comma_num) > len(board)\
                or int(after_comma_num) < 1 or int(after_comma_num) > len(board):
            location = input("Location doesn't exist, re-enter(Example: 2,3): ")
            before_comma_num = location.split(",")[0]
            after_comma_num = location.split(",")[1]

        if board[int(location[0]) - 1][int(location[len(location)-1])-1] == 0:
            board[int(location[0]) - 1][int(location[len(location) - 1])-1] = playerNum
            spotTaken = False
        else:
            print("This spot is already taken! Choose another one...")
    result = check_winner(board)

    return result

def create_new_board():
    board_size = int(input("Enter the size of game you want to play with! Must be odd and higher then 1: "))
    while board_size < 3 or board_size % 2 == 0:
        board_size = int(input("Wrong input! Enter a size higher then 1 and have to be ODD number: "))

    gameBoard = []
    for i in range(0, board_size):
        new = []
        for j in range(0, board_size):
            new.append(0)
        gameBoard.append(new)
    print_table(gameBoard)

    return gameBoard


gameBoard = create_new_board()

player1 = 1
player2 = 2
final_result = 0
for i in range(0, 9):
    if i % 2 == 0:
        result = fillSpot(gameBoard, player1)
    else:
        result = fillSpot(gameBoard, player2)
    print_table(gameBoard)
    if result != 0:
        print("********** The WINNER is Player ", result, "!!! **********")
        break
    if i == 8:
        print("No winner :( ")

