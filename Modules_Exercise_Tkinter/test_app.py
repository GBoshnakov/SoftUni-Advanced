from tkinter import *


def clear_screen():
    for el in window.grid_slaves():
        el.destroy()


def main_screen():
    clear_screen()
    Button(window, text="Hi", bg="yellow", fg="green", width=5, command=lambda: button_pressed()).grid(row=0, column=0)
    Label(window, text="<= Press this for more info").grid(row=0, column=1)


def button_pressed():
    clear_screen()
    Label(window, text="Surprise madafaka", fg="red").grid(row=0, column=0)
    Button(window, text="Go back", bg="yellow", width=10, command=lambda: main_screen()).grid(row=1, column=0)


window = Tk()
main_screen()

window.title("Bazu's app")
window.geometry("400x300")


window.mainloop()


