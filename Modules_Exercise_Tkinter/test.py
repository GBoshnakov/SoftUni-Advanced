import json

test_dict = {"a": 10, "b": 20, "c": 50}

with open("test.txt", "a") as file:
    file.write(json.dumps(test_dict))
    file.write("\n")


with open("test.txt") as file:
    text = file.readlines()
    for line in text:
        user = json.loads(line[:])
        print(user)



# with open("DB/user_credentials_db.txt") as file:
#     for line in file.readlines():
#         line = line.strip()
#         line = line.strip("\n")
#         print(line)
#         #print(line.split(", ")[0])