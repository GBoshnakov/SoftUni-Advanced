from functools import reduce

def func_executor(*args):
    result = []
    for func, arg in args:
        current_func = func(*arg)
        result.append(current_func)

    return result


def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

def substract_numbers(num1, num2):
    return num1 - num2



print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4)), (substract_numbers, (10, 9))))

