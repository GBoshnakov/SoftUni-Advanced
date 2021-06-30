def get_magic_triangle(n):
    triangle = []
    for row in range(n):
        triangle.append([])
        for col in range(0, row+1):
            if row == 0 or row == 1:
                triangle[row].append(1)
            elif col == 0 or col == row:
                triangle[row].append(1)
            else:
                triangle[row].append(triangle[row-1][col-1] + triangle[row-1][col])

    return triangle


print(get_magic_triangle(5))


# from math import factorial
#
#
# def get_magic_triangle(n):
#     triangle = []
#     for i in range(n):
#         triangle.append([])
#         for j in range(i + 1):
#             fact = factorial(i) // (factorial(j) * factorial(i - j))
#             triangle[i].append(fact)
#
#     return triangle
#
#
# print(get_magic_triangle(5))