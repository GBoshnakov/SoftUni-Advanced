import re

with open("text.txt") as file:

    for index, line in enumerate(file.readlines()):
        if index % 2 == 0:
            line = re.sub(r"[-,.!?]", "@", line)
            print(*line.split()[::-1])



