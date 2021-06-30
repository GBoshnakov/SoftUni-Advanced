rows, cols = [int(n) for n in input().split(", ")]

matrix = []



for row in range(rows):
    matrix.append([int(n) for n in input().split(" ")])

for col in range(cols):
    sum_curr_col = 0
    for row in range(rows):
        sum_curr_col += matrix[row][col]

    print(sum_curr_col)