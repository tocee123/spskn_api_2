# SK
## Zobrazenie
Na zobrazenie datumu a casu pouzijeme  a importneme `datetime` kniznicu
```py
import time, datetime
#display current time
print(time.ctime())
#display date
print(datetime.date.today())
#display date
print(datetime.datetime.now())
```
## Konvertovanie `datetime` na `string`
Pouzijeme metodu `strftime` na objekte `datetime`. Blizsie informacie a leaglne kody formatovania najdete [tu](https://www.w3schools.com/python/python_datetime.asp)
```py
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print(f"year: {year}")

month = now.strftime("%m")
print(f"month: {month}")

day = now.strftime("%d")
print(f"day: {day}")

time = now.strftime("%H:%M:%S")
print(f"time: {time}")

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"date and time: {date_time}")
```

## Unix timestamp
Unixovy casovy zapis znamena, kolko sekund preslo od 1.1.1970
```py
from datetime import datetime

timestamp = 1989797322
date_time = datetime.fromtimestamp(timestamp)

print("Date time object:", date_time)

formattings = ["%Y-%m-%d %H:%M:%S", "%d %b, %Y", "%d %B, %Y", "%I%p"]
for f in formattings:
    print(f"date using format {f: >18}: {date_time.strftime(f)}")
```

## Format podla lokalneho nastavenia pocitaca
```py
from datetime import datetime

date_time = datetime.now()

print("Date time object:", date_time)

formattings = ["%c", "%x", "%X"]
for f in formattings:
    print(f"date using format {f}: {date_time.strftime(f)}")
```

## Vytvorenie datetime objektu
Dbajte na to, ze prvy `datetime` z datetime.datetime je kniznica a druhy datetime je datovy typ. Datum s casom:
```py
import datetime
date = datetime.datetime(2020,1,14) #prida aj hodiny
print(date)
```
ked chcete len datum:
```py
import datetime
date = datetime.datetime(2020,1,14) #prida aj hodiny
print(date.date())
```
len datum:
```py
import datetime
date = datetime.date(2020,1,14)
print(date)
```
alebo:
```py
from datetime import date
d = date(2020,1,14)
print(d)
```
## Vytvorenie datetime objektu zo string-u
Tak isto, ako sme povedali, v akom **formate** chceme zobrazit `datetime`, mozeme pouzit format na generovanie `datetime`. Pouzijeme na to `strptime` funkciu nasledovne
```p
#https://www.programiz.com/python-programming/datetime/strptime
from datetime import datetime

def PrintValueAndType(value)->None:
    print(f"date_string = {value}")
    print(f"type of date_string = {type(value)}")

date_string = "21 June, 2018"
PrintValueAndType(date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
PrintValueAndType(date_object)
#just the date
PrintValueAndType(date_object.date())
```
```py
#https://www.programiz.com/python-programming/datetime/strptime
from datetime import datetime

dt_string = "14.4.2000"

# Considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(dt_string, "%d.%m.%Y")
print("dt_object1 =", dt_object1)
```
## Chyby pri konvertovani
Ak chcete konvertovat na datum budete mat chybu vo formate, alebo v texte, dostanete `ValueError`. Osetrite nasledovny kod
```py
#https://www.programiz.com/python-programming/datetime/strptime
from datetime import datetime

date_string = "12 11 2018"
date_object = datetime.strptime(date_string, "%d.%m.%Y")

print(f"date_object ={date_object}")
```
# Schedule, casovac taskov
```py
#https://docs.python.org/3/library/sched.html
import sched, time
s = sched.scheduler(time.monotonic, time.sleep)

def print_time(a='default'):
    print("From print_time", time.ctime(), a)
    
def print_some_times():
    print(time.ctime())
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('second',))
    # despite having higher priority, 'keyword' runs after 'positional' as enter() is relative
    s.enter(5, 1, print_time, kwargs={'a': 'first'})
    s.run()
    print(time.ctime())
    
print_some_times()
```
## Slow typing
```py
import time,random

typing_speed = 40 #wpm
def slow_type(text):
    for char in text:
        # sys.stdout.write(l)
        # sys.stdout.flush()
        print(char, end="")
        time.sleep(random.random()*10.0/typing_speed)
    
slow_type("In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available")
```
