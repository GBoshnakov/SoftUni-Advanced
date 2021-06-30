from collections import deque

number = int(input())

stack = deque()

for n in range(number):
    data = [int(n) for n in input().split()]

    if data[0] == 1:
        stack.append(data[1])

    elif data[0] == 2 and stack:
        stack.pop()
    elif data[0] == 3 and stack:
        print(max(stack))

    elif data[0] == 4 and stack:
        print(min(stack))

result = []

while stack:
    result.append(stack.pop())
print(*result, sep=", ")
