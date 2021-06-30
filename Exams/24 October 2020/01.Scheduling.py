from collections import deque


jobs = deque([int(el) for el in input().split(", ")])
index = int(input())


jobs.rotate(-index)
needed_job = jobs.popleft()
total_cycles = 0

for el in jobs:
    if el <= needed_job:
        total_cycles += el
total_cycles += needed_job

print(total_cycles)