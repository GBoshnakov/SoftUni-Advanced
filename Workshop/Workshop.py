ROWS = 6
COLS = 7


def create_board(rows=ROWS):
    return [[0] * 7 for _ in range(rows)]


def check_if_column_in_range(col, board, cols=COLS):
    if 0 <= col < cols and board[0][col] == 0:
        return True
    return False


def find_lowest_free(board, col_indx):
    for row in range(len(board)-1, -1, -1):
        if board[row][col_indx] == 0:
            return row
    return -1


def apply_player_choice(board, player, row, col):
    board[row][col] = player
    return board


def print_board(board):
    for row in board:
        print(row)


def is_player_winner(board, player, row, column, rows=ROWS, columns=COLS):

    horizontal = []
    for col_index in range(column-3, column+1):
        temp_list = []
        for i in range(col_index, col_index + 4):
            temp_list.append(True if i in range(columns) and board[row][i] == player else False)
        horizontal.append(all(temp_list))

    vertical = []
    for row_index in range(row - 3, row + 1):
        temp_list = []
        for i in range(row_index, row_index + 4):
            temp_list.append(True if i in range(rows) and board[i][column] == player else False)
        vertical.append(all(temp_list))

    primary_diagonal = []
    row_index_start = row - 3
    col_index_start = column - 3
    for _ in range(4):
        temp_list = []
        for i in range(4):

            temp_list.append(True if row_index_start + i in range(rows) and col_index_start+i in range(columns) and
                                     board[row_index_start + i][col_index_start+i] == player else False)
        row_index_start += 1
        col_index_start += 1
        primary_diagonal.append(all(temp_list))

    secondary_diagonal = []
    row_index_start = row - 3
    col_index_start = column + 3
    for _ in range(4):
        temp_list = []
        for i in range(4):
            temp_list.append(True if row_index_start + i in range(rows) and col_index_start - i in range(columns) and
                                     board[row_index_start + i][col_index_start - i] == player else False)
        row_index_start += 1
        col_index_start -= 1
        secondary_diagonal.append(all(temp_list))

    result = [
        any(horizontal),
        any(vertical),
        any(primary_diagonal),
        any(secondary_diagonal)
    ]

    return any(result)


def play(board, player=1):
    while True:
        print(f"Player {player}, please choose a column")
        column = int(input()) - 1

        if check_if_column_in_range(column, board):
            row = find_lowest_free(board, column)
            board = apply_player_choice(board, player, row, column)
            print_board(board)

            if is_player_winner(board, player, row, column):
                print(f"The winner is player {player}")
                break

            player = 2 if player == 1 else 1
        else:
            print(f"Invalid column")
            continue


board = create_board()
for el in board:
    print(el)
play(board)