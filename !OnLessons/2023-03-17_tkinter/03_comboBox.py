import tkinter as tk
from tkinter import ttk

def on_field_change(index, value, op):
    print ("combobox updated to ", my_combobox.get())
    
root = tk.Tk()
my_str_var = tk.StringVar()
my_str_var.trace("w", on_field_change)

my_combobox = ttk.Combobox(
    root, 
    textvariable = my_str_var,
    values=["PHP", "Java", "Python"],
    )

my_combobox.pack()
root.mainloop()