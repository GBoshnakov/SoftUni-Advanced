string = "GeorgGi"
for i in range(len(string)):
    if string[i] in "GOR":
        string = string.replace(string[i], "@")
        print("YES")

print(string)





with open("./files/text.txt") as file:
    text = []
    i = 0
    for line in file.readlines():
        if i % 2 == 0:
            text.append(line.strip("\n").split())
        i += 1

for el in text:
    sublist = el[::-1]
    for i in range(len(sublist)):
        word = sublist[i]
        for index in range(len(word)):
            if word[index] in "-,.!?":
                word = word.replace(word[index], "@")

        print(word, end=" ")
    print()

















