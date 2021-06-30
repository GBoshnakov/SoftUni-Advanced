start = int(input())
end = int(input())

filtered_nums = [el for el in range(start, end + 1) if [d for d in range(2, 11) if el % d == 0]]

print(filtered_nums)