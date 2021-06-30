rows = int(input())

matrix = [[int(el) for el in input().split()]for n in range(rows)]

data = input()

while data != "END":
    command, row, col, value = data.split()
    row, col, value = int(row), int(col), int(value)
    if 0 <= row < rows and 0 <= col < rows:
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    data = input()


for row in matrix:
    print(*row)

print(''.join([str(el) for el in matrix]))