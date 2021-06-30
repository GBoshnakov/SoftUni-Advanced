n = int(input())

guests = set()

for _ in range(n):
    code = input()
    if len(code) == 8:
        guests.add(code)

command = input()

while command != "END":
    guests.discard(command)

    command = input()

sorted_guests = sorted(guests)

print(len(sorted_guests))
print(*sorted_guests, sep="\n")