names = {name: {} for name in input().split(", ")}

command = input()

while command != "End":
    name, item, cost = command.split("-")
    if name in names:
        if item not in names[name]:
            names[name][item] = int(cost)
    command = input()

for key, val in names.items():
    print(f"{key} -> Items: {len(val)}, Cost: {sum([val[el] for el in val])}")