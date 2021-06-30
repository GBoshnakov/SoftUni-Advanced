rows, cols = [int(n) for n in input().split()]

matrix = [[f"{chr(97 + row)}{chr(97 + col + row)}{chr(97 + row)}" for col in range(cols)]for row in range(rows)]


for sublist in matrix:

    print(*[text for text in sublist], sep=" ")