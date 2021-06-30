n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()

    ascii_sum = 0

    for el in name:
        ascii_sum += ord(el)

    if (int(ascii_sum / i)) % 2 == 0:
        even_set.add(ascii_sum // i)
    else:
        odd_set.add(ascii_sum // i)

result = ""

if sum(even_set) == sum(odd_set):
    result = even_set | odd_set
    print(*result, sep=", ")

elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
    print(*result, sep=", ")

elif sum(even_set) > sum(odd_set):
    result = even_set.symmetric_difference(odd_set)
    print(*result, sep=", ")