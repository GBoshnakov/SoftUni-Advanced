import os

command = input()

while command != "End":
    operation, file_name,  *rest = command.split("-")

    if operation == "Create":
        with open(file_name, "w") as file:
            pass

    elif operation == "Add":
        content = rest[0]
        with open(file_name, "a") as file:
            file.write(content + "\n")

    elif operation == "Replace":
        old_string, new_string = rest
        try:
            with open(file_name, "r") as file:
                text = file.read()
            text = text.replace(old_string, new_string)
            with open(file_name, "w") as file:
                file.write(text)

        except FileNotFoundError:
            print("An error occurred")

    elif operation == "Delete":
        try:
            os.remove(file_name)

        except FileNotFoundError:
            print("An error occurred")

    command = input()