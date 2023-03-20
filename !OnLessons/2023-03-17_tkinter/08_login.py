from tkinter import *
from tkinter import ttk

def open_popup():
   top= Toplevel(parent)
   top.geometry("750x250")
   top.title("Child Window")
   Label(top, text= f"Name: {entry1.get()}, Id: {entry2.get()}, password: {entry3.get()}",).place(x=150,y=80)

parent = Tk()
parent.geometry("400x250")
name = Label(parent, text = "Name").place(x = 30, y = 50)
email = Label(parent, text = "User ID").place(x = 30, y = 90)
password =  ttk.Label(parent, text = "Password", ).place(x = 30, y = 130)
sbmitbtn = Button(parent, text = "Submit", activebackground = "green", activeforeground = "blue", command=open_popup).place(x = 120, y = 170)
entry1 = ttk.Entry(parent)
entry2 = ttk.Entry(parent)
entry3 = ttk.Entry(parent,show="*",)

entry1.place(x = 85, y = 50)
entry2.place(x = 85, y = 90)
entry3.place(x = 90, y = 130)
parent.mainloop()
