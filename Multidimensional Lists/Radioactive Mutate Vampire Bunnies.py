def check_is_valid_pos(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False


def rabbit_breeding(positions, matrix, is_loser):
    for row, col in positions:
        counter = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if counter % 2 != 0:
                    if check_is_valid_pos(i, j):
                        if matrix[i][j] == ".":
                            matrix[i][j] = "B"
                        elif matrix[i][j] == "P":
                            matrix[i][j] = "B"
                            is_loser = True
                counter += 1
    return matrix, is_loser


def player_movement(sign, row, col, matrix, is_winner, is_loser):
    if sign == "U":
        if not check_is_valid_pos(row-1, col):
            is_winner = True
            matrix[row][col] = "."
            return row, col, is_winner, is_loser

        elif matrix[row-1][col] == "B":
            is_loser = True
            matrix[row][col] = "."
            return row - 1, col, is_winner, is_loser
        else:
            matrix[row][col] = "."
            matrix[row-1][col] = "P"
            return row - 1, col, is_winner, is_loser

    elif sign == "D":
        if not check_is_valid_pos(row + 1, col):
            is_winner = True
            matrix[row][col] = "."
            return row, col, is_winner, is_loser
        elif matrix[row + 1][col] == "B":
            is_loser = True
            matrix[row][col] = "."
            return row + 1, col, is_winner, is_loser
        else:
            matrix[row][col] = "."
            matrix[row + 1][col] = "P"
            return row + 1, col, is_winner, is_loser

    elif sign == "L":
        if not check_is_valid_pos(row, col - 1):
            is_winner = True
            matrix[row][col] = "."
            return row, col, is_winner, is_loser
        elif matrix[row][col - 1] == "B":
            is_loser = True
            matrix[row][col] = "."
            return row, col - 1, is_winner, is_loser
        else:
            matrix[row][col] = "."
            matrix[row][col-1] = "P"
            return row, col - 1, is_winner, is_loser

    elif sign == "R":
        if not check_is_valid_pos(row, col + 1):
            matrix[row][col] = "."
            is_winner = True
            return row, col, is_winner, is_loser
        elif matrix[row][col + 1] == "B":
            is_loser = True
            matrix[row][col] = "."
            return row, col + 1, is_winner, is_loser
        else:
            matrix[row][col] = "."
            matrix[row][col+1] = "P"
            return row, col + 1, is_winner, is_loser


def create_matrix_find_player(rows):
    pos1, pos2 = None, None
    matrix = []
    for row in range(rows):
        matrix.append([el for el in list(input()) if el in ".PB"])
        if "P" in matrix[row]:
            pos1, pos2 = row, matrix[row].index("P")
    return pos1, pos2, matrix


rows, cols = [int(el) for el in input().split()]


player_pos_row, player_pos_col, matrix = create_matrix_find_player(rows)


is_winner = False
is_loser = False


command_as_string = input()

for command in command_as_string:
    if is_winner or is_loser:
        break
    player_pos_row, player_pos_col, is_winner, is_loser = player_movement(command, player_pos_row, player_pos_col, matrix, is_winner, is_loser)
    rabbits_positions = []

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "B":
                rabbits_positions.append((i, j))

    matrix, is_loser = rabbit_breeding(rabbits_positions, matrix, is_loser)


for i in range(rows):
    print(*matrix[i], sep="")


if is_winner:
    print(f"won: {player_pos_row} {player_pos_col}")
elif is_loser:
    print(f"dead: {player_pos_row} {player_pos_col}")
