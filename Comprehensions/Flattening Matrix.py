matrix = [[int(n) for n in input().split(", ")] for _ in range(int(input()))]

nums = [el for sublist in matrix for el in sublist]



print(nums)