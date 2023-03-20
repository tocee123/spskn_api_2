import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk

barValue = 0
def increment()->None:
    print("called")
    global barValue
    barValue += 10
    barValue = barValue % 100
    bar['value'] = barValue

def doIncrement()->None:
    parent.after(1000, func=increment)

parent = tk.Tk()

parent.title("Progressbar")
parent.geometry('350x200')
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green')
bar = Progressbar(parent, length=220, style='black.Horizontal.TProgressbar')
# bar['value'] = 80
bar.grid(column=0, row=0)
button= ttk.Button(parent, text="OK",command=doIncrement)
button.grid(column=0, row=1)
parent.mainloop()
