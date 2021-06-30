def find_even(nums):
    evens = []
    for el in nums:
        if el % 2 == 0:
            evens.append(el)
    return evens


def find_odd(nums):
    odds = []
    for el in nums:
        if el % 2 != 0:
            odds.append(el)
    return odds

command = input()
nums = [int(el) for el in input().split()]
if command == "Even":
    result = find_even(nums)
elif command == "Odd":
    result = find_odd(nums)

print(sum(result) * len(nums))