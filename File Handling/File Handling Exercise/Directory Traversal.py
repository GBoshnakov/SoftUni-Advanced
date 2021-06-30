import os

all_files = dict()
_, _, files = next(os.walk(input()))

for file in files:
    extension = file.split(".")[-1]

    if extension not in all_files:
        all_files[extension] = []
    all_files[extension].append(file)

text = ""

for key, val in sorted(all_files.items()):
    text += f".{key}\n"
    for v in sorted(val):
        text += f"- - - {v}\n"

with open(os.path.expanduser("~\\Desktop\\report.txt"), "w") as file:
    file.write(text)

