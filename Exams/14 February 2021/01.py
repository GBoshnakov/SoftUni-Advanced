from collections import deque


firework_effects = deque([int(el) for el in input().split(", ") if int(el) > 0])
explosive_power = [int(el) for el in input().split(", ") if int(el) > 0]


palm_counter = 0
willow_counter = 0
crossette_counter = 0
is_enough = False

while firework_effects and explosive_power:

    sum_of_both = firework_effects[0] + explosive_power[-1]

    if sum_of_both % 3 == 0 and sum_of_both % 5 != 0:
        palm_counter += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_of_both % 5 == 0 and sum_of_both % 3 != 0:
        willow_counter += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_of_both % 3 == 0 and sum_of_both % 5 == 0:
        crossette_counter += 1
        firework_effects.popleft()
        explosive_power.pop()

    else:
        firework_effects[0] -= 1
        if firework_effects[0] > 0:
            firework_effects.rotate(-1)
        else:
            firework_effects.popleft()

    if palm_counter >= 3 and willow_counter >= 3 and crossette_counter >= 3:
        is_enough = True
        break


if is_enough:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(el) for el in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")


print(f"Palm Fireworks: {palm_counter}")
print(f"Willow Fireworks: {willow_counter}")
print(f"Crossette Fireworks: {crossette_counter}")


