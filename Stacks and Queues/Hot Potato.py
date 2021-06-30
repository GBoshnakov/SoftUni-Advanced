from collections import deque

kids = deque(input().split())

turns = int(input())

# while len(kids) > 1:
#     kids.rotate(-turns)
#     print(f"Removed {kids.pop()}")
#
# print(f"Last is {kids.pop()}")

while len(kids) > 1:
    count = turns
    while count > 0:
        count -= 1
        kid = kids.popleft()
        kids.append(kid)
    print(f"Removed {kids.pop()}")

print(f"Last is {kids.pop()}")