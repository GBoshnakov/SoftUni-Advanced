def find_neg_pos(nums):
    negative = []
    positive = []
    for el in nums:
        if el < 0:
            negative.append(el)
        elif el > 0:
            positive.append(el)
    return sum(positive), sum(negative)

nums = [int(el) for el in input().split()]

positive, negative = find_neg_pos(nums)
print(negative, positive, sep="\n")
if abs(positive) > abs(negative):
    print(f"The positives are stronger than the negatives")
elif abs(positive) < abs(negative):
    print(f"The negatives are stronger than the positives")



