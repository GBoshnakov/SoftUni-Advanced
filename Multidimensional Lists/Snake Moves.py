from collections import deque
rows, cols = [int(n) for n in input().split()]

matrix = deque()
snake = input()
index = 0

for row in range(rows):
    matrix.append(deque())
    for col in range(cols):
        for i in range(index, index + 1):
            if row % 2 == 0:
                matrix[row].append(snake[i])
            else:
                matrix[row].appendleft(snake[i])
        index += 1
        if index == len(snake):
            index = 0

for row in range(rows):
    print("".join(matrix[row]))

