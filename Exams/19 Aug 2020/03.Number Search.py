def numbers_searching(*args):
    args = sorted(args)
    duplicates = set()
    missing_number = None

    for i in range(len(args)):
        if i + 1< len(args):
            if args[i] == args[i+1]:
                duplicates.add(args[i])
            elif not args[i] + 1 == args[i+1]:
                missing_number = args[i] + 1

    return [missing_number, sorted(list(duplicates))]


print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))