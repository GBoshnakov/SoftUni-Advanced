rows, cols = [int(n) for n in input().split(", ")]

matrix = []

sum_of_elements = 0

for i in range(rows):
    matrix.append([int(n) for n in input().split(", ")])
    sum_of_elements += sum(matrix[i])

print(sum_of_elements)
print(matrix)