import os
import json
from tkinter import *
from Modules_Exercise_Tkinter.app_view import window
from Modules_Exercise_Tkinter.helper_tools import clear_screen
from Modules_Exercise_Tkinter.products import render_products_page


def render_main_screen():
    clear_screen()
    Button(window, text="Login", bg="green", fg="white", width=10, command=lambda :render_login()).grid(row=0, column=0)
    Button(window, text="Register", bg="yellow",activeforeground="red", fg="black", width=10, command=lambda: render_register()).grid(row=1, column=0)
    Label(window, text="Click here to log into your account.").grid(row=0, column=1)
    Label(window, text="Click here to register new account.").grid(row=1, column=1)


def render_register(error=None):
    clear_screen()
    Label(window, text="Enter username:").grid(row=1, column=5)
    username = Entry(window)
    username.grid(row=2, column=5)
    Label(window, text="Enter password:").grid(row=3, column=5)
    password = Entry(window, show="*")
    password.grid(row=4, column=5)
    Label(window, text="Enter first name:").grid(row=5, column=5)
    first_name = Entry(window)
    first_name.grid(row=6, column=5)
    Label(window, text="Enter last name:").grid(row=7, column=5)
    last_name = Entry(window)
    last_name.grid(row=8, column=5)
    Label(window, text="").grid(row=9, column=5)
    Button(window, text="Submit", width=15, bg="green", command=lambda: register(username=username.get(),
                password=password.get(),first_name=first_name.get(), last_name=last_name.get())).grid(row=10, column=5)

    Button(window, text="<- Go back", width=15, bg="red", command=lambda: render_main_screen()).grid(row=11, column=5)

    if error is not None:
        Label(window, text=error).grid(row=12, column=5)


def render_login(error=None):
    clear_screen()
    Label(window, text="Enter username:").grid(row=1, column=2)
    username = Entry(window)
    username.grid(row=2, column=2)
    Label(window, text="Enter password:").grid(row=3, column=2)
    password = Entry(window, show="*")
    password.grid(row=4, column=2)
    Label(window, text="").grid(row=5, column=2)
    Button(window, text="Login", width=15, bg="green", command=lambda :login(username.get(), password.get())).grid(row=6, column=2)
    Button(window, text="<- Go back", width=15, bg="red", command=lambda: render_main_screen()).grid(row=7, column=2)

    if error is not None:
        Label(window, text=error).grid(row=8, column=2)


def register(**user, ):
    is_wrong = False
    user.update(({"products": []}))
    with open("DB/user_credentials_db.txt", "r") as file:
        for text in file.readlines():
            if user["username"] == text.split(", ")[0]:

                render_register(error="Username already registered")
                is_wrong = True
                break
    if not is_wrong:
        with open("DB/users.txt", "a") as file:
            file.write(json.dumps(user))
            file.write("\n")
        with open("DB/user_credentials_db.txt", "a") as file:
            file.write(f"{user['username']}, {user['password']}\n")
        render_registration_complete()


def login(usr, pasw):
    with open("DB/user_credentials_db.txt") as file:
        for line in file.readlines():
            line = line.strip("\n")
            username, password = line.split(", ")
            if username == usr and password == pasw:
                with open("DB/users.txt") as file:
                    users = file.readlines()
                    for user in users:
                        user = json.loads(user[:-1])
                        if user["username"] == usr:
                            first_name, last_name = user["first_name"], user["last_name"]

                            with open("DB/current_user.txt", "w") as current_user:
                                current_user.write(usr)
                            render_welcome_page(first_name, last_name)
                            return
        render_login(error="Invalid username or password")


def render_registration_complete():
    clear_screen()
    Label(window, text="Registration successful!", font=20).grid(row=0, column=0)
    Button(window, text="Go to Login", bg="green", fg="white", width=10, command=lambda :render_login()).grid(row=1, column=0)
    Button(window, text="Home", width=10,bg="red", command= lambda :render_main_screen()).grid(row=1, column=1)


def render_welcome_page(first_name, last_name):
    clear_screen()
    Label(text=f"Hello, {first_name.capitalize()} {last_name.capitalize()}!", font=32).grid(row=0, column=2)
    Button(window, text="Log out", bg="red", font="bold", width=15, command=lambda: render_main_screen()).\
        grid(row=2,column=2)

    Button(window, text="Start shopping", bg="green", font="bold", width=15, command=lambda :render_products_page()).\
        grid(row=2, column=1)
