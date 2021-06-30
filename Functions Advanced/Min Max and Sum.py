def min_max_sum(nums):
    result = {"min_el": min(nums),  "max_el": max(nums), "sum_el": sum(nums) }

    return result

nums = [int(el) for el in input().split()]

print(f"The minimum number is {min_max_sum(nums)['min_el']}")
print(f"The maximum number is {min_max_sum(nums)['max_el']}")
print(f"The sum number is: {min_max_sum(nums)['sum_el']}")