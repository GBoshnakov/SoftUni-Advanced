from functools import reduce
# def operate(operator, *args):
#     if operator == "+":
#         result = reduce(lambda x, y: x+y, args)
#     elif operator == "-":
#         result = reduce(lambda x, y: x-y, args)
#     elif operator == "*":
#         result = reduce(lambda x, y: x*y, args)
#     elif operator == "/":
#         result = reduce(lambda x, y: x/y, args)
#     return result


def operate(operator, *args):
    return eval(reduce(lambda x, y: f"{x}{operator}{y}", args))


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))