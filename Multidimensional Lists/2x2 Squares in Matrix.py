def find_if_square(row, col):
    values = [matrix[row][col], matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1]]
    if all(val == values[0] for val in values):
        return True
    return False

rows, cols = [int(n) for n in input().split()]

matrix = []

for row in range(rows):
    matrix.append([n for n in input().split()])

count_squares = 0

for row in range(0, rows - 1):
    for col in range(0, cols - 1):
        if find_if_square(row, col):
            count_squares += 1

print(count_squares)


