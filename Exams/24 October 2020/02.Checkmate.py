SIZE = 8


def create_matrix(rows=SIZE):
    matrix = []
    for row in range(rows):
        matrix.append([el for el in input().split()])
    return matrix


def check_range(row, col, size=SIZE):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def check_queens_move(row, col, matrix):
    horizontal = horizontally(row, col, matrix)
    vertical = vertically(row, col, matrix)
    first_diag = first_diagonal(row, col, matrix)
    second_diag = second_diagonal(row, col, matrix)

    return any([horizontal, vertical, first_diag, second_diag])


def horizontally(row, col, matrix):
    check = []
    for j in range(col+1, col+8):
        if check_range(row, j) and matrix[row][j] == "K":
            check.append(True)
            break
        elif check_range(row, j) and matrix[row][j] == "Q":
            check.append(False)
            break

    for j in range(col-1, col-8, -1):
        if check_range(row, j) and matrix[row][j] == "K":
            check.append(True)
            break
        elif check_range(row, j) and matrix[row][j] == "Q":
            check.append(False)
            break
    return any(check)


def vertically(row, col, matrix):
    check = []
    for i in range(row+1, row+8):
        if check_range(i, col) and matrix[i][col] == "K":
            check.append(True)
            break
        elif check_range(i, col) and matrix[i][col] == "Q":
            check.append(False)
            break
    for i in range(row-1, row-8, -1):
        if check_range(i, col) and matrix[i][col] == "K":
            check.append(True)
            break
        elif check_range(i, col) and matrix[i][col] == "Q":
            check.append(False)
            break
    return any(check)


def first_diagonal(row, col, matrix):
    check = []
    for n in range(1, 8):
        if check_range(row+n, col+n) and matrix[row+n][col+n] == "K":
            check.append(True)
            break
        elif check_range(row+n, col+n) and matrix[row+n][col+n] == "Q":
            check.append(False)
            break
    for n in range(-1, -8, -1):
        if check_range(row+n, col+n) and matrix[row+n][col+n] == "K":
            check.append(True)
            break
        elif check_range(row+n, col+n) and matrix[row+n][col+n] == "Q":
            check.append(False)
            break
    return any(check)


def second_diagonal(row, col, matrix):
    check = []
    for n in range(1, 8):
        if check_range(row+n, col-n) and matrix[row+n][col-n] == "K":
            check.append(True)
            break
        elif check_range(row+n, col-n) and matrix[row+n][col-n] == "Q":
            check.append(False)
            break
    for n in range(1, 8):
        if check_range(row-n, col+n) and matrix[row-n][col+n] == "K":
            check.append(True)
            break
        elif check_range(row-n, col+n) and matrix[row-n][col+n] == "Q":
            check.append(False)
            break
    return any(check)


def play(matrix):
    is_safe = True
    for row in range(SIZE):
        for col in range(SIZE):
            if matrix[row][col] == "Q":
                if check_queens_move(row, col, matrix):
                    print([row, col])
                    is_safe = False
    return is_safe


matrix = create_matrix()
is_safe = play(matrix)

if is_safe:
    print("The king is safe!")
