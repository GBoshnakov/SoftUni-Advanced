ROWS = int(input())


def create_matrix_find_snake(rows):
    matrix = []
    snake_row = None
    snake_col = None
    for i in range(rows):
        matrix.append(list(input()))
        if "S" in matrix[i]:
            snake_row = i
            snake_col = matrix[i].index("S")
    return matrix, snake_row, snake_col


def is_in_range(row, col, rows = ROWS):
    if 0 <= row < rows and 0 <= col < rows:
        return True
    return False


def snake_moves(row, col, new_row, new_col):
    global matrix
    matrix[row][col] = "."
    matrix[new_row][new_col] = "S"
    return new_row, new_col

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


matrix, snake_row, snake_col = create_matrix_find_snake(ROWS)
food_quantity = 0
is_over = False

while food_quantity < 10:
    command = input()
    new_row = snake_row + directions[command][0]
    new_col = snake_col + directions[command][1]
    if is_in_range(new_row, new_col):
        if matrix[new_row][new_col] == "*":
            food_quantity += 1
            snake_row, snake_col = snake_moves(snake_row, snake_col, new_row, new_col)
        elif matrix[new_row][new_col] == "B":
            matrix[snake_row][snake_col] = "."
            matrix[new_row][new_col] = "."
            for i in range(ROWS):
                for j in range(ROWS):
                    if matrix[i][j] == "B":
                        matrix[i][j] = "S"
                        snake_row = i
                        snake_col = j
        else:
            snake_row, snake_col = snake_moves(snake_row, snake_col, new_row, new_col)
    else:
        matrix[snake_row][snake_col] = "."
        is_over = True
        break


if is_over:
    print("Game over!")
    print(f"Food eaten: {food_quantity}")
else:
    print("You won! You fed the snake.")
    print(f"Food eaten: {food_quantity}")

for row in matrix:

    print(*row, sep="")
