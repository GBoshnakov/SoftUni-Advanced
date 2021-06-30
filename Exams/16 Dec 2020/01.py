from collections import deque


def check_value(number):
    if number <= 0:
        return True
    return False


def check_if_divisible(number):
    if number % 25 == 0:
        return True
    return False


males = [int(el) for el in input().split()]
females = deque([int(el) for el in input().split()])
matches = 0


while males and females:
    current_male = males[-1]
    current_female = females[0]

    if check_value(current_male):
        males.pop()
        continue
    if check_value(current_female):
        females.popleft()
        continue
    if check_if_divisible(current_male):
        males.pop()
        if males:
            males.pop()
        continue
    if check_if_divisible(current_female):
        females.popleft()
        if females:
            females.popleft()
        continue

    if current_male == current_female:
        males.pop()
        females.popleft()
        matches += 1

    else:
        females.popleft()
        males[-1] -= 2


print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(el) for el in males[::-1]])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(el) for el in females])}")
else:
    print("Females left: none")




