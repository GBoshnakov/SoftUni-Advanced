from collections import deque

food = int(input())

queue = deque(int(n) for n in input().split())

print(max(queue))

while queue:
    if food < queue[0]:
        break
    food -= queue[0]
    queue.popleft()

if not queue:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(list(map(str, queue)))}")