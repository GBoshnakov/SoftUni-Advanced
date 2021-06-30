def filtered(nums):
    result = filter(lambda x: x % 2 == 0, nums)
    return list(result)


nums = [int(el) for el in input().split()]
print(filtered(nums))