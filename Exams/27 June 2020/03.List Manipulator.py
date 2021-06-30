from collections import deque


def list_manipulator(numbers, *args):
    numbers = deque(numbers)
    first_command, second_command,*rest = args
    if first_command == "add" and second_command == "beginning":
        for el in rest[::-1]:
            numbers.appendleft(el)
    elif first_command == "add" and second_command == "end":
        numbers.extend(rest)
    elif first_command == "remove" and second_command == "beginning":
        if rest:
            for _ in range(rest[0]):
                numbers.popleft()
        else:
            numbers.popleft()
    elif first_command == "remove" and second_command == "end":
        if rest:
            for _ in range(rest[0]):
                numbers.pop()
        else:
            numbers.pop()
    return list(numbers)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
