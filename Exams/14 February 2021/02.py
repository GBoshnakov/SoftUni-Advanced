def create_matrix_find_player(rows):
    pos1, pos2 = None, None
    matrix = []
    for row in range(rows):
        matrix.append([el for el in input().split()])
        for i in range(len(matrix[row])):
            if matrix[row][i].isdigit():
                matrix[row][i] = int(matrix[row][i])
        if "P" in matrix[row]:
            pos1, pos2 = row, matrix[row].index("P")
    return pos1, pos2, matrix


def check_if_valid_position(row, col):
    if 0 <= row < rows and 0 <= col < rows:
        return True
    return False


def check_player_movement(row, col, command, matrix):
    if command == "up":
        if check_if_valid_position(row-1, col) and matrix[row-1][col] != "X":
            return True
        return False
    elif command == "down":
        if check_if_valid_position(row + 1, col) and matrix[row + 1][col] != "X":
            return True
        return False
    elif command == "left":
        if check_if_valid_position(row, col-1) and matrix[row][col-1] != "X":
            return True
        return False
    elif command == "right":
        if check_if_valid_position(row, col+1) and matrix[row][col+1] != "X":
            return True
        return False


def player_collecting_points(row, col, matrix, command, points, positions):
    if command == "up":
        points += matrix[row-1][col]
        positions.append([row-1, col])
        matrix[row - 1][col] = "P"
        matrix[row][col] = 0
        return row-1, col, matrix, points, positions
    elif command == "down":
        points += matrix[row + 1][col]
        positions.append([row + 1, col])
        matrix[row + 1][col] = "P"
        matrix[row][col] = 0
        return row + 1, col, matrix, points, positions
    elif command == "left":
        points += matrix[row][col-1]
        positions.append([row, col-1])
        matrix[row][col-1] = "P"
        matrix[row][col] = 0
        return row, col-1, matrix, points, positions
    elif command == "right":
        points += matrix[row][col + 1]
        positions.append([row, col + 1])
        matrix[row][col + 1] = "P"
        matrix[row][col] = 0
        return row, col + 1, matrix, points, positions


rows = int(input())
points_positions = []
total_points = 0
is_winner = False
is_loser = False

player_row, player_col, matrix = create_matrix_find_player(rows)


while True:
    command = input()
    if check_player_movement(player_row, player_col, command, matrix):
        player_row, player_col, matrix, total_points, points_positions = player_collecting_points(player_row, player_col, matrix, command, total_points, points_positions)
        if total_points >= 100:
            is_winner = True
            break
    else:
        is_loser = True
        break

if is_loser:
    print(f"Game over! You've collected {total_points//2} coins.")
    print(f"Your path:")
    print(*points_positions, sep="\n")

if is_winner:
    print(f"You won! You've collected {total_points} coins.")
    print(f"Your path:")
    print(*points_positions, sep="\n")

# print(total_points)
# print(matrix)
