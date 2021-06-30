n = int(input())

users = set()

for _ in range(n):
    user = input()

    users.add(user)

print(*users, sep= "\n")