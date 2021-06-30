def even_odd(*args):
    args = list(args)
    operator = args.pop()
    filtered = []
    if operator == "even":
        filtered = filter(lambda x:x % 2 == 0, args)
    elif operator == "odd":
        filtered = filter(lambda x:x % 2 == 1, args)

    return list(filtered)

print(even_odd(1, 2, 3, 4, 5, 6, "even"))

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))