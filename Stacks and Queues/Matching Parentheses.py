text = input()

indexes = []

for i in range(len(text)):
    if text[i] == "(":
        indexes.append(i)
    elif text[i] == ")":
        print(text[indexes.pop():i + 1])