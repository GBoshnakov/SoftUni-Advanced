from Modules_Exercise_Tkinter.helper_tools import clear_screen
from Modules_Exercise_Tkinter.app_view import window
from tkinter import *
from PIL import Image, ImageTk
import json
import os


base_folder = os.path.dirname(__file__)


def render_products_page():
    clear_screen()
    with open("DB/products.txt") as file:
        products = file.readlines()
        col = 0
        for line in products:
            product = json.loads(line[:-1]if "\n" in line else line)
            if product["count"] > 0:

                Label(window, text=product["name"]).grid(row=0, column=col)

                image = Image.open(os.path.join(os.path.join(base_folder, "DB/images"), product["img_path"]))
                image = image.resize((100, 100))
                photo = ImageTk.PhotoImage(image)
                img_label = Label(image=photo)
                img_label.image = photo
                img_label.grid(row=1, column=col)

                Label(window, text=f"In stock: {product['count']}").grid(row=2, column=col)
                button = Button(window, text=f"Buy {product['id']}")
                button.configure(command=lambda b=button: buy_product(b))
                button.grid(row=3, column=col)
                col += 1


def buy_product(button):
    _, product_id = button.cget("text").split()
    product_id = int(product_id)
    username = None
    with open("DB/current_user.txt") as file:
        username = file.read()
    with open("DB/users.txt", "r+") as file:
        data = file.readlines()
        file.seek(0)
        for line in data:
            current_user = json.loads(line)
            if current_user["username"] == username:
                current_user["products"].append(product_id)
            file.write(json.dumps(current_user) + "\n")

    with open("DB/products.txt", "r+") as file:
        data = file.readlines()
        file.seek(0)
        for line in data:
            product = json.loads(line)
            if product["id"] == product_id:
                product["count"] -= 1
            file.write(json.dumps(product) + "\n")
    render_products_page()

