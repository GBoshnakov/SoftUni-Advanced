n = int(input())

parking = set()

for _ in range(n):
    command, reg = input().split(", ")

    if command == "IN":
        parking.add(reg)

    elif command == "OUT":
        parking.discard(reg)

if parking:
    print(*parking, sep="\n")
else:
    print("Parking Lot is Empty")