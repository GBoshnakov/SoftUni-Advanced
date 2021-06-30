rows = int(input())

matrix = []

sum_of_alive_cells = 0
counter_alive_cells = 0

for row in range(rows):
    matrix.append([int(n) for n in input().split()])

bombs = input().split(" ")

for el in bombs:
    row, col = int(el[0]), int(el[2])
    bomb_strenght = matrix[row][col]
    if bomb_strenght > 0:
        for i_bomb in range(row - 1, row + 2):
            for j_bomb in range(col - 1, col + 2):
                if 0 <= i_bomb < rows and 0 <= j_bomb < rows:
                    if matrix[i_bomb][j_bomb] > 0:
                        matrix[i_bomb][j_bomb] -= bomb_strenght


for i in range(rows):
    for j in range(rows):
        if matrix[i][j] > 0:
            sum_of_alive_cells += matrix[i][j]
            counter_alive_cells += 1

print(f"Alive cells: {counter_alive_cells}")
print(f"Sum: {sum_of_alive_cells}")

for i in range(rows):
    for j in range(rows):
        print(matrix[i][j], end=" ")
    print()




