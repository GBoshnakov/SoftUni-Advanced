from functools import reduce


def multiply(*args):
    result = 1
    result *= reduce(lambda x, y: x * y, args)
    return result


# def multiply(*args):
#     result = 1
#     for el in args:
#         result *= el
#     return result

print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
