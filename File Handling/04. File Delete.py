import os

try:
    os.remove("./files/my_first_file.txt")

except FileNotFoundError:
    print("File alreeady deleted!")