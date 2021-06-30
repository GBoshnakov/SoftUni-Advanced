try:
    with open("File Handling Exercise/text.txt") as file:
        print(file.read())
    print("File found")
except FileNotFoundError:
    print("File not found")