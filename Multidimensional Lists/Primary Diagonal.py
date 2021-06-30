rows = int(input())

matrix = []

sum_of_diagonal = 0

for row in range(rows):
    matrix.append([int(n) for n in input().split()])
    sum_of_diagonal += matrix[row][row]

print(sum_of_diagonal)