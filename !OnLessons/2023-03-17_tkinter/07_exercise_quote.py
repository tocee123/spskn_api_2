#pip install tkinter

import tkinter as tk
from tkinter import END, Text
from tkinter.ttk import Button
import requests


def get_quote():
    r = requests.get('https://api.quotable.io/random')
    data = r.json()
    quote = data['content']
    text_box.delete('1.0', END)
    text_box.insert(END, quote)   

root = tk.Tk()
root.title('Quoter')
text_box = Text(root, height=10, width=50)
get_button = Button(root, text="Get Quote", command=get_quote)
  
text_box.pack()
get_button.pack()
root.mainloop()