#n = int(input())

matrix = [[int(el) for el in input().split(", ") if int(el) % 2 == 0]for i in range(int(input()))]

print(matrix)