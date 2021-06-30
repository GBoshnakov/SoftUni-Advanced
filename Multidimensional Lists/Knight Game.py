rows = int(input())


def check_knight_attacks(row, col, matrix):
    matches = 0
    rows_pos = [-2, -2, 2, 2, 1, 1, -1, -1]
    cols_pos = [-1, 1, -1, 1, -2, 2, -2, 2]

    for i in range(len(rows_pos)):
        if 0 <= row - rows_pos[i] < len(matrix) and 0 <= col - cols_pos[i] < len(matrix):
            if matrix[row - rows_pos[i]][col - cols_pos[i]] == "K":
                matches += 1
    return matches


matrix = []
counter = 0
for row in range(rows):
    matrix.append(list(input()))

while True:
    knight_position = []
    max_matches = 0

    for row in range(rows):
        for col in range(rows):
            if matrix[row][col] == "K":
                matches = check_knight_attacks(row, col, matrix)
                if matches > max_matches:
                    max_matches = matches
                    knight_position = [row, col]

    if knight_position:
        matrix[knight_position[0]][knight_position[1]] = "0"
        counter += 1
    else:
        break

print(counter)
