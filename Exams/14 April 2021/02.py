rows, cols = 7, 7


def check_if_valid(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False


def calculate_sum_current_pos(row, col):
    total_points = int(matrix[0][col]) + int(matrix[row][0]) + int(matrix[row][cols-1]) + int(matrix[rows-1][col])
    return total_points


def calculate_points(row, col):
    if check_if_valid(row, col):
        if matrix[row][col] == "D":
            return calculate_sum_current_pos(row, col) * 2
        elif matrix[row][col] == "T":
            return calculate_sum_current_pos(row, col) * 3
        elif matrix[row][col].isdigit():
            return int(matrix[row][col])
        elif matrix[row][col] == "B":
            return 501
    else:
        return 0


players = [el for el in input().split(", ")]
players_points = [501, 501]
matrix = [[el for el in input().split()] for _ in range(rows)]
is_winner = False
throws_counter = 0


while not is_winner:
    throws_counter += 1
    for player in range(2):
        row, col = [int(el.strip("()")) for el in input().split(", ")]
        current_player = players[player]
        current_plr_points = players_points[player]
        if (current_plr_points - calculate_points(row, col)) <= 0:
            is_winner = True
            break
        else:
            players_points[player] -= calculate_points(row, col)


print(f"{current_player} won the game with {throws_counter} throws!")


