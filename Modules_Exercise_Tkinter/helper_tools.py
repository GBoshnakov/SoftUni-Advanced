from Modules_Exercise_Tkinter.app_view import window



def clear_screen():
    for el in window.grid_slaves():
        el.destroy()


