string = input()
rows = int(input())


def check_in_range(row, col, size=rows):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def apply_new_player_position(matrix, new_row, new_col, player):
    player_row, player_col = player
    matrix[new_row][new_col] = "P"
    matrix[player_row][player_col] = "-"
    player = [new_row, new_col]
    return matrix, player


def player_movement(command, matrix, string, player):
    player_row, player_col = player
    if command == "down":
        if check_in_range(player_row+1, player_col):
            if matrix[player_row+1][player_col].isalpha():
                string += matrix[player_row+1][player_col]
                matrix, player = apply_new_player_position(matrix, player_row+1, player_col, player)
                return matrix, string, player
            else:
                matrix, player = apply_new_player_position(matrix, player_row+1, player_col, player)
                return matrix, string, player
        else:
            if string:
                string = string[:-1]
            return matrix, string, player
    elif command == "up":
        if check_in_range(player_row - 1, player_col):
            if matrix[player_row - 1][player_col].isalpha():
                string += matrix[player_row-1][player_col]
                matrix, player = apply_new_player_position(matrix, player_row - 1, player_col, player)
                return matrix, string, player
            else:
                matrix, player = apply_new_player_position(matrix, player_row - 1, player_col, player)
                return matrix, string, player
        else:
            if string:
                string = string[:-1]
            return matrix, string, player
    elif command == "left":
        if check_in_range(player_row, player_col-1):
            if matrix[player_row][player_col-1].isalpha():
                string += matrix[player_row][player_col-1]
                matrix, player = apply_new_player_position(matrix, player_row, player_col - 1, player)
                return matrix, string, player
            else:
                matrix, player = apply_new_player_position(matrix, player_row, player_col - 1, player)
                return matrix, string, player
        else:
            if string:
                string = string[:-1]
            return matrix, string, player
    elif command == "right":
        if check_in_range(player_row, player_col + 1):
            if matrix[player_row][player_col + 1].isalpha():
                string += matrix[player_row][player_col + 1]
                matrix, player = apply_new_player_position(matrix, player_row, player_col + 1, player)
                return matrix, string, player
            else:
                matrix, player = apply_new_player_position(matrix, player_row, player_col + 1, player)
                return matrix, string, player
        else:
            if string:
                string = string[:-1]
            return matrix, string, player



matrix = []
player_pos = []
for row in range(rows):
    matrix.append(list(input()))
    if "P" in matrix[row]:
        player_pos = [row, matrix[row].index("P")]


for _ in range(int(input())):
    command = input()
    matrix, string, player_pos = player_movement(command, matrix, string, player_pos)


print(string)
for row in matrix:
    print(*row, sep="")
