from collections import deque

water = int(input())

name = input()
queue = deque([])

while name != "Start":
    queue.append(name)

    name = input()

command = input()

while command != "End":
    if command.startswith("refill"):
        water += int(command.split()[-1])
    else:
        person = queue.popleft()
        if water >= int(command):
            water -= int(command)
            print(f"{person} got water")
        else:
            print(f"{person} must wait")


    command = input()

print(f"{water} liters left")
