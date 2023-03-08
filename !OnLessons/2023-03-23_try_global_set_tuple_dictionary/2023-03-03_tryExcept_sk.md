# Try except
Ked sa vyskytne chyba v aplikacii (konvertujeme slovo na int, pristupujeme k neexistujucemu klucu v slovniku), aplickacia hodi **exception** (chybu)

## Priklad
```py
x = int("apple")
print("hello world")
```
alebo
```py
x = int(input(("Zadaj cislo: ")) #a pouzivatel zada 'jablko'
print("hello world")
```
## Koncept
```py
try: #blok na spustenie prikazov s moznymi chybami
    pass #prikazy, pri ktorych mozu nastat chyby
except: #ked nastane chyba, co sa ma udiat
    pass #prikazy na osetrenie chyby
finally: #hocico sa stane naslaedujuci blok sa ma spustit
    pass
```

> `pass` je prikaz, ktory nic nerobi, ale pre prazdne funkcie, bloky je nevyhnutny, aby python vedel spracovat skript

v takychto pripadoch my mozeme chybu odchytit a spracovat bez toho, aby program prestal bezat
```py
try:
    x = int("apple")
except:
    print("there was an error")
print("hello world")
```
alebo
```py
try:
    x = int("apple")
except:
    print("there was an error")
finally:
    print("hello world")
```
## Hierarchia chyb

Kazda chyba dedi od `Exception`
```py
try:
    x = int("apple")
except ValueError:
    print("there was a value")
except Exception:
    print("there was a general exception")
print("hello world")
```
