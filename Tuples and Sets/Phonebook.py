phone_book = {}

data = input()

while not data.isdigit():
    name, number = data.split("-")

    if name not in phone_book:
        phone_book[name] = ""
    phone_book[name] = number

    data = input()


for _ in range(int(data)):
    searched_name = input()

    if searched_name not in phone_book:
        print(f"Contact {searched_name} does not exist.")
    else:
        print(f"{searched_name} -> {phone_book[searched_name]}")