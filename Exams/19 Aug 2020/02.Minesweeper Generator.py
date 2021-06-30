SIZE = int(input())
bombs = int(input())


def in_range(row, col, size=SIZE):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


matrix = []

for row in range(SIZE):
    matrix.append([" "] * SIZE)

for _ in range(bombs):
    row, col = [int(el) for el in input()[1:-1].split(", ")]
    if in_range(row, col):
        matrix[row][col] = "*"


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_right": (-1, 1),
    "up_left": (-1, -1),
    "down_right": (1, 1),
    "down_left": (1, -1),
}
for row in range(SIZE):
    for col in range(SIZE):
        if matrix[row][col] == " ":
            current_bombs = 0
            for direction in directions:
                next_row = row + directions[direction][0]
                next_col = col + directions[direction][1]
                if in_range(next_row, next_col):
                    if matrix[next_row][next_col] == "*":
                        current_bombs += 1
            matrix[row][col] = current_bombs

for row in matrix:
    print(*row, sep=" ")