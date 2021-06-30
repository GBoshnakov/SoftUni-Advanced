numbers = [float(n) for n in input().split()]

result = {}

for el in numbers:
    if el not in result:
        result[el] = 0
    result[el] += 1

for key, val in result.items():
    print(f"{key} - {val} times")