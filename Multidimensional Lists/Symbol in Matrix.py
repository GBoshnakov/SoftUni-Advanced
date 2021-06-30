rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([n for n in list(input())])

position = None

searched_symbol = input()


for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == searched_symbol:
            position = (row, col)
            print(position)
            exit()
print(f"{searched_symbol} does not occur in the matrix")