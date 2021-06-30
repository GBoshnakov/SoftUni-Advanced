from collections import deque

number_of_pumps = int(input())

circle = deque()





for _ in range(number_of_pumps):
    data = [int(n) for n in input().split()]
    circle.append(data)

current_smallest = int()
index = 0

#print(circle)


for i in range(len(circle)):
    fuel_in_tank = 0
    is_enough_fuel = True
    j = i
    for _ in range(number_of_pumps):

        if j == len(circle) - 1:
            if fuel_in_tank + circle[j][0] >= circle[j][1]:
                fuel_in_tank += circle[j][0]
                fuel_in_tank -= circle[j][1]
                j = 0
            else:
                is_enough_fuel = False
                break
        else:
            if fuel_in_tank + circle[j][0] >= circle[j][1]:
                fuel_in_tank += circle[j][0]
                fuel_in_tank -= circle[j][1]
                j += 1

            else:
                is_enough_fuel = False
                break
    if is_enough_fuel:
        current_smallest = i
        break

print(current_smallest)