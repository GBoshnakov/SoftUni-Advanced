with open("./files/numbers.txt") as files:
    result = [int(el) for el in files.read().split()]
    print(sum(result))