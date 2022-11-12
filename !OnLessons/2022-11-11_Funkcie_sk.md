# Funkcie
Funkcia, alebo podprogram je blok kodu, ktory sa vykona po zavolani. Funkciu najprv treba zadefinovat pomocou `def` dat jej nazov, vstupne parametre, zadefinovat vystupny typ a dvojbodka, po nej v novom riadku uz mozeme pisat blok kodu patriaci funkcii
S tymito podprogramami vieme rozdelit zodpovednosti celkoveho programu.

## Parametre funkcie

Parametrom funkcie je  **dočasná premenná**, ktorá vzniká pri volaní funkcie a prostredníctvom ktorej, môžeme do funkcie  _poslať_  nejakú hodnotu. Parametre funkcií definujeme počas definovania funkcie v  **hlavičke funkcie**  a ak ich je viac, oddeľujeme ich čiarkami:
```py
def meno_funkcie(parameter):
    prikaz
    prikaz
    ...
```

## Deklaracia funkcie bez vystupneho parametra
Nasledujuca funkcia nieco vykona, ale nevrati nam ziadnu hodnotu naspat, navratova hodnota je `None`
```py
def NazovFunkcie(vstupnyParameter1, vstupnyParameter2)-> None:
	prikaz
	prikaz
NazovFunkcie(1, "text")
```
### Priklad
```py
def PozdravUzivatela(meno:str, priezvisko: str)-> None:
	print(f"Ahoj {meno} {priezvisko}! Aky mas dnes den?")
PozdravUzivatela("John", "Doe")
```
> Ahoj John Doe! Aky mas dnes den?

## Deklaracia funkcie s vystupnym parametrom
Nasledujuca funkcia nieco vykona a na konci vrati nejaky vysledok, zadefinujeme typ
```py
def NazovFunkcie(vstupnyParameter1, vstupnyParameter2)-> str/int/float/bool...:
	blok kodu
	blok kodu
	return hodnota
navratovaHodnota = NazovFunkcie(1, "text")
print(navratovaHodnota)
```
### Priklad
```py
def SpocitajDveCisla(prveCislo:int, druheCislo: int)-> int:
	return prveCislo + druheCislo
sucet = SpocitajDveCisla(1, 10)
print(sucet)
```
> 11

### Priklad, chceme zistit ci oba retazce maju dlzku aspon 10
```py
retazec1 = input("Zadaj prvy retazec: ")
retazec2 = input("Zadaj prvy retazec: ")
minimalnaDlzka = 10
majuObaRetazceViacAko10Znakov = retazec1.__len__()> minimalnaDlzka  and  retazec1.__len__() > minimalnaDlzka
if(majuObaRetazceViacAko10Znakov):
	print(f"Ano, oba retazce maju viac ako {minimalnaDlzka} znakov")
else:
	print(f"Jeden alebo oba retazce su kratsie, ako {minimalnaDlzka} znakov")
```
> Zadaj prvy retazec: 12344334324 
Zadaj prvy retazec: 23e42309asflij
Ano, oba retazce maju viac ako 10 znakov

```py
def  SuRetazceDhlsieAkoMinimalnaDlzka(r1:str, r2:str, min:int)->bool:
	majuObaRetazceViacAko10Znakov = r1.__len__()> min  and  r2.__len__() > min
	return  majuObaRetazceViacAko10Znakov
	#alebo return r1.__len__()> minimalnaDlzka and r2.__len__() > minimalnaDlzka

retazec1 = input("Zadaj prvy retazec: ")
retazec2 = input("Zadaj prvy retazec: ")
minimalnaDlzka = 10
if(SuRetazceDhlsieAkoMinimalnaDlzka(retazec1, retazec2, minimalnaDlzka)):
	print(f"Ano, oba retazce maju viac ako {minimalnaDlzka} znakov")
else:
	print(f"Jeden alebo oba retazce su kratsie, ako {minimalnaDlzka} znakov")
```
> Zadaj prvy retazec: 12344334324 
Zadaj prvy retazec: 23e42309asflij
Ano, oba retazce maju viac ako 10 znakov
### Priklad, rozhodnime sa, aku poziciu ma zamestnanec na zaklade mzdy
```py
from random import randint

platZamestnanca = randint(1000,10000)
pozicia = ""
if(platZamestnanca>8000):
    pozicia = "Director"
elif(platZamestnanca>6000): 
    pozicia = "Manager"
elif(platZamestnanca>4000):
    pozicia = "Associate Manager"
else:
    pozicia = "Worker"
    
print(f"Zamestnanec, ktory zaraba {platZamestnanca} EUR ma poziciu \"{pozicia}\"")
```
>Zamestnanec, ktory zaraba 7698 EUR ma poziciu "Manager"

Takto to vyzera pouzitim funkcie:
```py
from random import randint

def VratPoziciuNaZakladePlatu(plat:int)->str:
    pozicia = ""
    if(plat>8000):
        pozicia = "Director"
    elif(plat>6000): 
        pozicia = "Manager"
    elif(plat>4000):
        pozicia = "Associate Manager"
    else:
        pozicia = "Worker"
    return  f"\"{pozicia}\""

platZamestnanca = randint(1000,10000)

print(f"Zamestnanec, ktory zaraba {platZamestnanca} EUR ma poziciu {VratPoziciuNaZakladePlatu(platZamestnanca)}")
```
Rozmýšľaš, prečo občas voláme funkcie pomocou `.` na konci reťazca (napr. `"Ola".upper()`) a inokedy najprv zavoláme funkciu a reťazec dáme do zátvoriek? Ide o to, že v niektorých prípadoch funkcie patria k **objektom**, ako napríklad `upper()`, čo je funkcia, ktorá môže byť vykonaná len na **reťazcoch**.  Inokedy funkcie nepatria k žiadnemu konkrétnemu objektu a môžu byť použité na rôzne typy objektov, ako je to v prípade `print()`. Preto posielame reťazec `"Ola"` ako parameter funkcii `print`.
Viac si o tom mozete precitat [tu](https://input.sk/python2017/05.html)
