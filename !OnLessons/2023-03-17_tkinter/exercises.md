# Pouzivanie `tkinter` kniznice
Na tychto linkoch mozete najst blizsie informacie: 
- [w3resource](https://www.w3resource.com/python-exercises/tkinter/index.php)
- [w3schools](https://www.w3schools.in/python/gui-programming)
- [Python Examples](https://pythonexamples.org/python-tkinter/)

> ak by vam chybal modul, zavolajte `pip install tkinter` v terminali

# Kroky pri vytvarani grafickeho rozhrania
- importnite si `Tkinter` modul
- postavte si GUI aplikaciu (okno)
- pridajte **widget**y (vizualne elemnty)
- pridajte cyklus primarneho objektu `parent.mainloop()`

> **Dolezite** niektore widget-y maju vstupny parameter `command`, prikaz, tento prikaz je **objekt funkcii**, cize nedavajte za nou `()`. Ako keby ste povedali, ze ked pouzivatel klikne na gombik, vtedy sa ma vykonat prikaz. Ked zavolate funkciu so `()` na konci, ona vam vrati hodnotu, my potrebujeme v takomto pripade objekt funkcie

### Priklad s jednym gombikom
Jednoduche graficke rozhranie s jednym tlacidkom `Quit`, ktory zatvory aplikaciu
```py
import tkinter as tk 
parent = tk.Tk() 
parent.title('Title - button') 
my_button = tk.Button(parent, text='Quit', height=1, width=35, command=parent.destroy) 
my_button.pack() 
parent.mainloop()
```

### Priklad s dvoma gombikmi
```py
import tkinter as tk   

def write_text():
    print("Tkinter is easy to create GUI!")

parent = tk.Tk()
frame = tk.Frame(parent)
frame.pack()

text_disp= tk.Button(frame, text="Hello", command=write_text)

text_disp.pack(side=tk.LEFT)

exit_button = tk.Button(frame, text="Exit", fg="green",command=quit)
exit_button.pack(side=tk.RIGHT)

parent.mainloop()
```

> Vsimnite si, ako `text_disp` objet ma `command` nastaveny na `write_text` a nie ~~`write_text()`~~

## Typy `widget`ov
- button
- canvas
- combo-box
- frame
- level
- check-button
- entry
- level-frame
- menu
- list - box
- menu button
- message
- tk_optoinMenu
- progress-bar
- radio button
- scroll bar
- separator
- tree-view

# Umiestnenie widgetov
## Pack
Tato metoda usporiada widgety pre parent:
```py
import tkinter as tk 
parent = tk.Tk() 
parent.title('Title - button') 
for i in range(1, 6):
    tk.Button(parent, text=f'Quit #{i}', height=1, width=35, command=parent.destroy).pack()
parent.mainloop()
```
Inicializujeme novy gombik pre pre okno `parent` a funkcia `pack()` sa postara o umiestnenie
## Grid
```py
import tkinter as tk 
parent = tk.Tk() 
parent.title('Title - button') 
i = 1
for row in range(3):
    for column  in range(2):
        tk.Button(parent, text=f'Quit #{i}', height=1, width=35, command=parent.destroy).grid(row=row, column=column)
        i+=1
parent.mainloop()
```
Inicializuje sa gombik pre `parent` okno, ale teraz pouzijeme `grid(row=, column=)` funkciu, kde presnie vieme povedat, kde sa ma dany widget zobrazit
## Place
```py
import tkinter as tk 
parent = tk.Tk() 
parent.title('Title - button') 
parent.geometry("500x200")
i = 1
height, width = 1, 15
for row in range(3):
    for column  in range(2):
        tk.Button(parent, text=f'Quit #{i}', height=height, width=width, command=parent.destroy).place(x=row*(width+100), y=column*(height+20))
        i+=1
parent.mainloop()
```
Tu musite presne vediet, kde sa maju jednotlive widgety nachadzat
