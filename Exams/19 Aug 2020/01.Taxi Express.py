from collections import deque


customers = deque([int(el) for el in input().split(", ")])
taxis = [int(el) for el in input().split(", ")]

total_time_driven = 0

while taxis and customers:
    if customers[0] > taxis[-1]:
        taxis.pop()
        continue
    else:
        total_time_driven += customers.popleft()
        taxis.pop()

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time_driven} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(el) for el in customers])}")