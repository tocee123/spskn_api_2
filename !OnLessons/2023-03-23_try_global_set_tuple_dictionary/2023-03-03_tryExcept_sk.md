# Try except

[link](https://www.w3schools.com/python/python_try_except.asp)

- `try` blok vam umozni spustit/otestovat kod, kde sa mozu vyskytnut chyby
- `except` blok vam umozni poradit sa s vyskytnutou chybou
- `else` blok nastane v tedy, ked ziadna chyba nenastala v `try` bloku
- `finally` blok spusti kod bez ohladu na to, ci bola nastala chyba alebo nie
- 
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
Jeden try-except blok moze mat viacero except blokov, ale vzdy zamerany na iny typ chyby. 
Kazda chyba dedi od `Exception`, alebo uz od nejakeho potomka:
```py
class SystemError(Exception): ...
class TypeError(Exception): ...
class ValueError(Exception): ...
class FloatingPointError(ArithmeticError): ...
class OverflowError(ArithmeticError): ...
class ZeroDivisionError(ArithmeticError): ...
class ModuleNotFoundError(ImportError): ...
class IndexError(LookupError): ...
class KeyError(LookupError): ...
class UnboundLocalError(NameError): ...
```

Ked odchytavame chyby, najprv musime dat vzdy najnizsi potomok (v hierarchy dedenia toho, od ktoreho uz ina chyba `Exception` nededi v `except` blokoch)

`class ValueError(Exception)` `ValueError` dedi od `Exception`, tym padom ho musime zachytit skor ako `Exception`: 
```py
try:
    x = int("apple")
except ValueError:
    print("there was a value error")
except Exception:
    print("there was a general exception")
print("hello world")
```
```
there was a value error
hello world
```
ked to ich obratime, hlaska z bloku `except ValueError` sa nikdy nezobrazi:
```py
try:
    x = int("apple")
except Exception:
    print("there was a general exception")
except ValueError:
    print("there was a value error")
print("hello world")
```
```
there was a general exception
hello world
```

## Pouzite hodnoty chyby

Zapis: `except Exception as ex:` v tomto pripade mozeme vypisat hodnotu chyby, ak ma atributy, tak aj tie mozeme pouzit

```py
try:
    x = int("apple")
except ValueError as ex:
    print("there was a value error", ex)
print("hello world")
```
## Definovanie a pouzitie vlastnej chyby
V nasledujucom priklade si vytvorime vlastnu chybu `LessThan20Exception`, ktora dedi od `Exception` a bude mat atribut/vlastnost `Message` a v `except` bloku ju odchytime a vypiseme na obrazovku spravu
```py
class LessThan20Exception(Exception):
    def __init__(self, value) -> None:
        super().__init__()
        self.Message = f"Value {value} is less than 20."

x = 10
try:
   if (x<20):
       raise LessThan20Exception(x)
except LessThan20Exception as ex:
    print(ex.Message)
    #Value 10 is less than 20.
```
