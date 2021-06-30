rows, cols = [int(n) for n in input().split()]

matrix = []

for row in range(rows):
    matrix.append([el for el in input().split()])

data = input()

while data != "END":
    try:
        command, first, second, third, fourth = data.split()
        if command == "swap":
            matrix[int(first)][int(second)], matrix[int(third)][int(fourth)] = \
                matrix[int(third)][int(fourth)], matrix[int(first)][int(second)]
            for row in range(rows):
                for col in range(cols):
                    print(matrix[row][col], end=" ")
                print()
        else:
            print("Invalid input!")
    except:
        print("Invalid input!")

    data = input()




