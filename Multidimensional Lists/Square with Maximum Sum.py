import sys

rows, cols = [int(n) for n in input().split(", ")]

matrix = []

for row in range(rows):
    matrix.append([int(n) for n in input().split(", ")])

max_position = None
current_max = -sys.maxsize

for row in range(rows - 1, 0, -1):

    for col in range(cols - 1, 0, -1):
        current_sum = matrix[row][col] + matrix[row-1][col] + matrix[row][col-1] + matrix[row-1][col-1]
        if current_sum >= current_max:
            current_max = current_sum
            max_position = [matrix[row-1][col-1], matrix[row-1][col], matrix[row][col-1], matrix[row][col]]

print(f"{max_position[0]} {max_position[1]} \n{max_position[2]} {max_position[3]}")
print(current_max)

