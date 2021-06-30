import sys

def find_sum_3x3(row, col):
    sum = 0
    current_matrix = []
    for i in range(row, row + 3):
        current_matrix.append([])
        for j in range(col, col + 3):
            sum += matrix[i][j]
            current_matrix[i - row].append(matrix[i][j])
    return sum, current_matrix

rows, cols = [int(n) for n in input().split()]

matrix = []
max_3x3 = []
current_max = -sys.maxsize

for row in range(rows):
    matrix.append([int(n) for n in input().split()])

for row in range(0, rows - 2):
    for col in range(0, cols - 2):
        total_sum, mtr = find_sum_3x3(row, col)
        if total_sum > current_max:
            current_max = total_sum
            max_3x3 = mtr

print(f"Sum = {current_max}")

for i in range(3):
    for j in range(3):
        print(max_3x3[i][j], end=" ")
    print()