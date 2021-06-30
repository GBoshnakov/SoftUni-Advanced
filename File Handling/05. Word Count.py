with open("./files/words.txt") as file:
    words = file.read().split()

with open("./files/input.txt") as file:
    text = [el.strip("-.,?!").lower() for el in file.read().split()]

result = dict()

for word in words:
    result[word] = text.count(word)
sorted_result = sorted(result.items(), key=lambda x: -x[1])

for key, val in sorted_result:
    print(f"{key} - {val}")