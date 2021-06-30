num = int(input())

set_one = set()
set_two = set()

intersection = set()
longest_intersection = []
longest_len = int()

for _ in range(num):
    first_range, second_range = input().split("-")

    first_start, first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")

    set_one = set(range(int(first_start), int(first_end) + 1))
    set_two = set(range(int(second_start), int(second_end) + 1))

    intersection = set_one & set_two
    if len(intersection) > longest_len:
        longest_len = len(intersection)
        longest_intersection = list(intersection)

print(f"Longest intersection is {longest_intersection} with length {longest_len}")