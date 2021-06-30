rows = int(input())

matrix = []

sum_primary_diagonal = 0
sum_secondary_diagonal = 0

for row in range(rows):
    matrix.append([int(n) for n in input().split()])

    sum_primary_diagonal += matrix[row][row]
    sum_secondary_diagonal += matrix[row][rows-row - 1]

print(abs(sum_primary_diagonal - sum_secondary_diagonal))