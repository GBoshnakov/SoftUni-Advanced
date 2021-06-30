clothes = [int(n) for n in input().split()]

max_capacity = int(input())

current_rack = 0

rack_counter = 1

while clothes:
    cloth = clothes.pop()
    if current_rack + cloth > max_capacity:
        rack_counter += 1
        current_rack = cloth
    else:
        current_rack += cloth

print(rack_counter)