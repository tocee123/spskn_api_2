import tkinter as tk
from tkinter import ttk

def whenChecked()->None:
    print(f"checked, value: {my_boolean_var.get()}")

root = tk.Tk()
my_boolean_var = tk.BooleanVar()

my_checkbutton = ttk.Checkbutton(
    text="Check when the option True",
    variable=my_boolean_var,
    command=whenChecked
)
my_checkbutton.pack()
root.mainloop()