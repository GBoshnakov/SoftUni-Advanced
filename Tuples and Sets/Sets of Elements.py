n, m = [int(x) for x in input().split()]

set_one = set()
set_two = set()

for _ in range(n):
    number = int(input())
    set_one.add(number)

for _ in range(m):
    number = int(input())
    set_two.add(number)

unique_elements = set_one.intersection(set_two)

print(*unique_elements, sep="\n")

