from collections import deque

def time(time_in_seconds):
    hours = time_in_seconds // 3600
    time_in_seconds %= 3600
    minutes = time_in_seconds // 60
    time_in_seconds %= 60
    seconds = time_in_seconds
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

robots = input().split(";")
starting_time = [int(n) for n in input().split(":")]
time_in_seconds = starting_time[0] * 3600 + starting_time[1] * 60 + starting_time[2]
products = deque()
available_robots = deque(robots)
command = input()


while command != "End":
    products.append(command)

    command = input()

while products:
    time_in_seconds += 1
    if available_robots:
        pass
    if time_in_seconds == 36002:
        break

print(time(time_in_seconds))



print(robots)
print(starting_time)
print(time_in_seconds)
print(products)
print(available_robots)