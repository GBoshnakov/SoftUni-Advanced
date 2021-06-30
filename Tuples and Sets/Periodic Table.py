n = int(input())
unique_elements = set()

for _ in range(n):
    # elements = input().split()
    # for el in elements:
    #     unique_elements.add(el)
    unique_elements = unique_elements.union(set(input().split()))

print(*unique_elements, sep="\n")