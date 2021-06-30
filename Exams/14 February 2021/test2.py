from collections import deque

firework_effects = deque([int(el) for el in input().split(", ") if int(el) > 0])
explosive_power = deque([int(el) for el in input().split(", ")if int(el) > 0])

fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}

while firework_effects and explosive_power:

    sum_of_both = firework_effects[0] + explosive_power[-1]

    if sum_of_both % 3 == 0 and sum_of_both % 5 != 0:
        fireworks["Palm Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_of_both % 5 == 0 and sum_of_both % 3 != 0:
        fireworks["Willow Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_of_both % 3 == 0 and sum_of_both % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    else:
        firework_effects[0] -= 1
        if firework_effects[0] > 0:
            firework_effects.rotate(-1)
        else:
            firework_effects.popleft()

    if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
        break
is_perfect = True

for el in fireworks:
    if fireworks[el] < 3:
        is_perfect = False

if is_perfect:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join([str(el) for el in firework_effects])}")

if explosive_power:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")

for key, val in fireworks.items():
    print(f"{key}: {val}")