#Import tkinter library
from tkinter import *
from tkinter import ttk
#Create an instance of tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
win.title("Main Window")
#Define a function to Open a new window
def open_win():
   child_win= Toplevel(win)
   child_win.title("Child Window")
   child_win.geometry("750x250")
   content= entry.get()
   Label(child_win, text=content, font=('Bell MT', 20, 'bold')).pack()
   win.withdraw()
#Create an Entry Widget
entry=ttk.Entry(win, width= 40)
entry.pack(ipady=4,pady=20)
#Let us create a button in the Main window
button= ttk.Button(win, text="OK",command=open_win)
button.pack(pady=20)
win.mainloop()