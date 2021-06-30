nums = input().split()

def abs_val(nums):
    return [abs(float(el)) for el in nums]

print(abs_val(nums))