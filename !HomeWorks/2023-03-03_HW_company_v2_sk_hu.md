# Domaca uloha Firma v2.0
Vašou úlohou bude vybudovať firmu dôrazom na triedy, triedne atribúty, funkcie. 
## Trieda `Zamestnanec` 

- bude mať nasledovné atribúty:
    - `Id:int`
    - `Plat:int`
    - `Pohlavie:str`
    - `Pozicia:str`
- a nasledovné funkcie:
    - `def __init__(self)->None:` bez parametra, init funkcia sa bude starat o to, ked zavolate konštruktor triedy `Zamestnanec()` tak sa naplnia atribúty automaticky:
        - `Id` - náhodné číslo <1_000_000, 10_000_000>
        - `Pohlavie` - muž/žena
        - `Plat` - náhodné číslo <1_000, 10_000>
        - `Pozicia` sa určí podľa výplaty: *Riaditel* (8000, 10000>, *Manager* (6000, 8000>, *Zastupca managera* (4000, 6000> a *Pracovník* <1000, 4000>
    - `def __str__(self) -> str:` alebo `def ToString(self) -> str:` vráti reťazec *Ahoj, moje ID je {Id}, som {Pohlavie}, pracujem na pozicii {Pozicia} a zarabam {Plat} Eur*

## Trieda `Firma`
- bude mať nasledovné atribúty:
    - `Nazov:str`
    - `Zamestnanci:list[Zamestnanec]`
    - `PriemernyPlatMuzov:float`
    - `PriemernyPlatZien:float`
    - `PriemernyPlatZamestnancov:float`
    - `PocetMuzov:int`
    - `PocetZien:int`
    - `PocetZamestnancov:int`
- a nasledovné funkcie:
    - `def __init__(self, nazov:str)->None:` s parametrom nazov.
    - `def VyvorZamestnancov(self, pocetZamestnancov:int):` ktorá vytvorí presný počet zamestnancov a pridá ich  do zoznamu `Zamestnanci`
    - `def VypočítajHodnotyFirmy(self):` vypočíta priemery platov a pocty zamestnancov a uloží do patričných atribútov
    - `def __str__(self) -> str:` alebo `def ToString(self) -> str:` alebo `def VratDetailyFirmy(self)->str:` vráti reťazec *Vo firme {Nazov} pracuje {PocetZamestnancov} z toho {PocetZien} zien a {PocetMuzov} muzov.\nPriemerny plat zamestnancov je {PriemernyPlatZamestnancov} eur, primerny plat zien je {PriemernyPlatZien} eur a priemerny plat muzov je {PriemernyPlatMuzov}\nVo firme pracuju nasledovny zmestnanci:\n{zoznam zamestnancov v textovom zobrazeni}*
## `Main`
- Vytvorte instanciu firmy
- Náhodným generátorom určite počet zamestnancov (50-100)
- Vypočítajte, nastavte atribúty firmy
- Vypíšte na obrazovku detaily firmy

## Známkovanie
1. Odovzdáte do termínu a program robí to, čo má
1. Neodovzdáte do termínu, alebo program bude obsahovať menšie chyby
1. Urobíte len časť programu
1. individuálne
1. Vôbec neodovzdáte, opisujete, nefunguje, ako má

# Házi feladat Cég v2.0
A feladatotok egy cég létrehozása, most viszont a hangsúlyt az osztályokra, attribútumokra és függvényekre tesszük.
## `Alkalmazott` osztály 

- következő attribútumokkal:
    - `Id:int`
    - `Fizetes:int`
    - `Nem:str`
    - `Pozicio:str`
- és függvényekkel rendelkezik:
    - `def __init__(self)->None:` bemenő paraméter nélkül, s ha meghívjátok az `Alkalmazott()` konstruktort, az init függvény megtölti az attribútumokat a következőképpen:
        - `Id` - véletlen szám <1_000_000, 10_000_000>
        - `Nem` - férfi/nő
        - `Fizetes` - véletlen szám<1_000, 10_000>
        - `Pozicio` határozzátok meg a fizetésből: *Igazgato* (8000, 10000>, *Manager* (6000, 8000>, *Helyettes manager* (4000, 6000> a *Munkas* <1000, 4000>
    - `def __str__(self) -> str:` vagy `def ToString(self) -> str:` a következő szövegkonstanst adja vissza: *Szia, az IDm {Id}, {Nem} vagyok, {Pozicio} pozicioban dolgozom, es {Fizetes} Eurt keresek*

## `Ceg` osztaly
- következő attribútumokkal:
    - `Nev:str`
    - `Alkalmazottak:list[Alkalmazott]`
    - `FerfiakAtlagfizetese:float`
    - `NokAtlagfizetese:float`
    - `AlkalmazottakAtlagfizetese:float`
    - `FerfiakSzama:int`
    - `NokSzama:int`
    - `AlkalmazottakSzama:int`
-  és függvényekkel rendelkezik:
    - `def __init__(self, nev:str)->None:` beállítjátok a cég nevét.
    - `def GeneraljAlkalmazottakat(self, alkalmazottakSzama:int):` `alkalmazottakSzama`nyi alkalmazottat hoz létre, és meni el a `Alkalmazottak` listába
    - `def HatarozdMegAzAttributumokat(self):` kiszámítja az átlagfizetéseket nem alapján, az alkalmazottak számát szintén nem alapján, és elmenti a meghatározott attribútumokba
    - `def __str__(self) -> str:` vagy `def ToString(self) -> str:` vagy `def AddViszaACegReszleteit(self)->str:` a következő szöveget adja vissza *A {Nev} cegben {AlkalmazottakSzama} dolgozik, ebbol {NokSzama} no es  {FerfiakSzama} ferfi.\nAz alkalmazottak atlagfizetese {AlkalmazottakAtlagfizetese} Eur, ebbol a noke {NokAtlagfizetese} Eur, es {FerfiakAtlagfizetese} Eur a ferfiake\nA cegben a kovetkezo alkalmazottak dolgoznak:\n{az egyes alkalmazottak szoveges reprezentacioja}*

## `Main`
- Inicializáljátok a céget
- Véletlenszám-generátorral határozzátok meg a dolgozók számát (50-100)
- Határozzátok meg a cég attribútumait
- Írjátok ki a képernyőre a cég részleteit


## Jegyek
1. Leadjátok határidőn belül, és a program azt csinálja, ami a feladatban van
1. Határidő után adjátok le, vagy kisebb hibákat tartalmaz a program
1. Csak egy részét csináljátok meg a programnak
1. Individuálisan
1. Egyáltalán nem adjátok le, másoltok, vagy nem működik

# Help skeleton

```py
from random import randint, choice

class Sex:
    Male = "male"
    Female = "female"

class Worker:
    Id:int
    
    def __init__(self)->None:
        pass
    
    def __str__(self) -> str:
        pass

class Company:
    Name:str
    Workers:list[Worker] = []
    
    def __init__(self, name:str) -> None:
        pass
    
    def __str__(self)->str:
        pass

def Main()->None:
    pass
Main()
```

# Example
```py
In company Just in case ltd. there are 85 workers. 48 men and 37 women.
The average salary of a worker is 5304.42 EUR, men earn 5357.96 and women earn 5234.97.
Each member of the company:
Hi, my id is 5437452, I'm a male Worker and I earn 2487
Hi, my id is 8055202, I'm a male Worker and I earn 3731
Hi, my id is 5217407, I'm a female Worker and I earn 1207
Hi, my id is 8187881, I'm a male Associate Manager and I earn 5509
Hi, my id is 8913786, I'm a female Associate Manager and I earn 5463
Hi, my id is 4601111, I'm a male Manager and I earn 7207
Hi, my id is 6104414, I'm a female Manager and I earn 6145
Hi, my id is 6601874, I'm a male Associate Manager and I earn 4551
Hi, my id is 6521231, I'm a male Worker and I earn 1661
Hi, my id is 2021602, I'm a female Associate Manager and I earn 5813
Hi, my id is 2765510, I'm a male Manager and I earn 7602
Hi, my id is 1623794, I'm a male Worker and I earn 3999
Hi, my id is 8241115, I'm a male Worker and I earn 2968
Hi, my id is 9112125, I'm a male Manager and I earn 7687
Hi, my id is 3212414, I'm a male Worker and I earn 1860
Hi, my id is 1841816, I'm a male Worker and I earn 2578
Hi, my id is 8381056, I'm a male Director and I earn 9484
Hi, my id is 3940956, I'm a female Worker and I earn 3518
Hi, my id is 8077605, I'm a female Worker and I earn 3857
Hi, my id is 6551905, I'm a male Associate Manager and I earn 4996
Hi, my id is 5734775, I'm a female Manager and I earn 7326
Hi, my id is 4115595, I'm a male Manager and I earn 7349
Hi, my id is 2295455, I'm a male Director and I earn 8356
Hi, my id is 3090092, I'm a female Manager and I earn 7930
Hi, my id is 3307271, I'm a male Worker and I earn 1646
Hi, my id is 7486222, I'm a male Associate Manager and I earn 5266
Hi, my id is 8182122, I'm a male Worker and I earn 3775
Hi, my id is 1027866, I'm a male Director and I earn 9456
Hi, my id is 4833397, I'm a female Worker and I earn 2112
Hi, my id is 9704647, I'm a female Worker and I earn 2263
Hi, my id is 6967449, I'm a male Worker and I earn 3455
Hi, my id is 9762232, I'm a male Associate Manager and I earn 5776
Hi, my id is 8702416, I'm a female Director and I earn 9966
Hi, my id is 5843859, I'm a female Manager and I earn 7877
Hi, my id is 2799798, I'm a male Manager and I earn 7800
Hi, my id is 5277523, I'm a male Manager and I earn 6225
Hi, my id is 8242997, I'm a male Associate Manager and I earn 4955
Hi, my id is 6442832, I'm a male Director and I earn 8136
Hi, my id is 5598156, I'm a male Associate Manager and I earn 5253
Hi, my id is 7690168, I'm a male Manager and I earn 6905
Hi, my id is 7537455, I'm a female Worker and I earn 1618
Hi, my id is 9877845, I'm a male Worker and I earn 2432
Hi, my id is 1122273, I'm a female Worker and I earn 2603
Hi, my id is 7055165, I'm a female Associate Manager and I earn 5368
Hi, my id is 7946965, I'm a male Manager and I earn 7811
Hi, my id is 1427837, I'm a female Director and I earn 9264
Hi, my id is 8871882, I'm a female Worker and I earn 3943
Hi, my id is 8051012, I'm a female Manager and I earn 7072
Hi, my id is 1587288, I'm a female Worker and I earn 1974
Hi, my id is 5214977, I'm a female Director and I earn 9846
Hi, my id is 2164661, I'm a male Worker and I earn 3976
Hi, my id is 8825497, I'm a male Worker and I earn 3194
Hi, my id is 9888808, I'm a female Director and I earn 9041
Hi, my id is 2509984, I'm a male Director and I earn 8651
Hi, my id is 6027665, I'm a female Associate Manager and I earn 4352
Hi, my id is 2959461, I'm a male Director and I earn 9881
Hi, my id is 7196469, I'm a female Worker and I earn 2817
Hi, my id is 2808782, I'm a female Worker and I earn 1500
Hi, my id is 6640697, I'm a male Worker and I earn 2602
Hi, my id is 7866279, I'm a male Worker and I earn 3889
Hi, my id is 7667962, I'm a male Worker and I earn 2399
Hi, my id is 8732772, I'm a male Associate Manager and I earn 5521
Hi, my id is 6203289, I'm a female Associate Manager and I earn 5392
Hi, my id is 8723804, I'm a female Associate Manager and I earn 5511
Hi, my id is 2613680, I'm a male Associate Manager and I earn 4741
Hi, my id is 5635636, I'm a female Associate Manager and I earn 5531
Hi, my id is 4654848, I'm a female Associate Manager and I earn 4055
Hi, my id is 8461156, I'm a female Worker and I earn 1230
Hi, my id is 4017909, I'm a male Director and I earn 9948
Hi, my id is 6385863, I'm a male Director and I earn 8757
Hi, my id is 8656132, I'm a male Worker and I earn 2562
Hi, my id is 2394900, I'm a female Associate Manager and I earn 5528
Hi, my id is 7548156, I'm a female Worker and I earn 3947
Hi, my id is 6309146, I'm a female Director and I earn 9480
Hi, my id is 6379627, I'm a male Associate Manager and I earn 4179
Hi, my id is 6740066, I'm a female Director and I earn 8440
Hi, my id is 4087695, I'm a male Manager and I earn 7147
Hi, my id is 9290582, I'm a female Manager and I earn 7421
Hi, my id is 6483444, I'm a female Manager and I earn 7413
Hi, my id is 8680233, I'm a male Associate Manager and I earn 5842
Hi, my id is 3048045, I'm a male Worker and I earn 3961
Hi, my id is 6268203, I'm a female Associate Manager and I earn 5706
Hi, my id is 2315339, I'm a female Worker and I earn 1165
Hi, my id is 9093895, I'm a male Associate Manager and I earn 5001
Hi, my id is 9306594, I'm a male Associate Manager and I earn 4015
```
