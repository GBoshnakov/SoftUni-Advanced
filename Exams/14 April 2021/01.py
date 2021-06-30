from collections import deque

orders = deque(int(el) for el in input().split(", "))
employees = [int(el) for el in input().split(", ")]

total_pizzas_made = 0

while orders:
    if not employees:
        break
    current_order = orders[0]
    if current_order <= 0 or current_order > 10:
        orders.popleft()
    else:
        while employees:
            if current_order < employees[-1]:
                total_pizzas_made += current_order
                employees.pop()
                orders.popleft()
                break
            elif current_order > employees[-1]:
                total_pizzas_made += employees[-1]
                current_order -= employees[-1]
                orders[0] -= employees[-1]
                employees.pop()
            elif current_order == employees[-1]:
                total_pizzas_made += current_order
                orders.popleft()
                employees.pop()
                break

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_made}")
    print(f"Employees: {', '.join(list(map(str, employees)))}")

elif orders and not employees:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(list(map(str, orders)))}")