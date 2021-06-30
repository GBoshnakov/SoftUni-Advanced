nums = input().split()

def rounding(nums):
    return [round(float(el)) for el in nums]

print(rounding(nums))