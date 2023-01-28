# Uloha na dedenie
Teraz vyskusate dedenie tried. Nasledujuca uloha vyzera byt velmi dlha, ale je to na techniku. Budete vela kopirovat, kedze triedy az tak velmi sa neodlisuju od seba. Chodte bod po bode.

Zadefinujete 4 triedy nasledovne:
- triedu `Zviera`, super class, bude mat atribut `Meno:int` a `__init__` metodu, cez ktoru naplnite `Meno`
- triedu `Macka`, bude dedit od `Zviera` a rozsirite ju o atribut `PocetChytenychMysi:int` a `__init__` metodu, cez ktoru naplnite `Meno` a `PocetChytenychMysi`. Bude mat hlasku: **"Volam sa {Meno} a som macka. Chytila som {PocetChytenychMysi} mysi"**
- triedu `Pes`, bude dedit od `Zviera` a rozsirite ju o atribut `PocetUhryznutychPostarov:int` a `__init__` metodu, cez ktoru naplnite `Meno` a `PocetUhryznutychPostarov`. Bude mat hlasku: **"Volam sa {Meno} a som pes. Uhryzol som {PocetUhryznutychPostarov} postarov"**
- triedu `Mys`, bude dedit od `Zviera` a rozsirite ju o atribut `VahaZjedenehoSyra:float` a `__init__` metodu, cez ktoru naplnite `Meno` a `VahaZjedenehoSyra`. Bude mat hlasku: **"Volam sa {Meno} a som mys. Za moj zivot som zjedol {VahaZjedenehoSyra}kg syra"**

Zadefinujete aj `Main()` metodu:
- kde vytvorite lubovolny pocet instancii kazdej podtriedy (aspon 1x macku, 1x psa a 1x mys)
- vlozite ich do zoznamu [link](https://github.com/tocee123/spskn_api_2/blob/main/!OnLessons/2023-01-27_oop_inheritance_sk.md#priklad-so-studentami)
- pomocou `for` cykla vypisete ich hlasku

## Pomocka na vypis hlasky
Bud zadefinujete funkciu `def __str__(self)->str:` alebo `def PozdravSa()->str`
### Priklad na `__self__`
```py
class Person:
    Name:str
    Age:int
    
    def __init__(self, name:str, age:int) -> None:
        self.Age = age
        self.Name = name

    def __str__(self):
        return f"Hi, i'm {self.Name} and i am {self.Age} years old"

person = Person("Aladar", 18)
print(person)
```
### Priklad na PozdravSa
```py
class Person:
    Name:str
    Age:int
    
    def __init__(self, name:str, age:int) -> None:
        self.Age = age
        self.Name = name

    def PozdravSa(self):
        return f"Hi, i'm {self.Name} and i am {self.Age} years old"

person = Person("Aladar", 18)
print(person.PozdravSa())
```

## Pomocky
- priklad na funkciu `def__str__(self)->str:` najdete tu [link](https://github.com/tocee123/spskn_api_2/blob/main/!OnLessons/2023-01-27_oop_inheritance_sk.md#priklad-so-studentami)
- na `__init__` v podtriedach (`Macka`, `Pes`, `Mys`) pouzijete nasledovny postup, kde `PridanyAtribut` je `PocetChytenychMysi`, `PocetUhryznutychPostarov` a pre mysi `VahaZjedenehoSyra`
```py
def __init__(self, name: str, pridanyAtribut:int) -> None:
    super().__init__(name)  
    self.PridanyAtribut = pridanyAtribut
```
## Znamkovanie
1. Odovzdate do terminu a mate vsetky 4 triedy spravne nastavene, vytvorili ste zoznam zvierat, inicializovali ste aspon 3, dali ste ich do zoznamu a vypisali ich hlasku
1. Odovzdate po terminte a mate vsetky 4 triedy spravne nastavene, vytvorili ste zoznam zvierat, inicializovali ste aspon 3, dali ste ich do zoznamu a vypisali ich hlasku
1. Zadefinujete aspon jednu dedicnost, vytvorite aspon jednu instanciu dedenej/podtriedy, vypisete hlasku
1. individualne
1. Ked vobec nic neodovzdate

# Feladat az oroklesre
Most kiprobaljatok az osztalyokban az oroklest. A kovetkezo feladat nagyon igenyesnek, es hosszunak tunhet, de most a technikat sajatitjuk el. Sok mindent masolni fogtok, hiszen eppen csak egy-ket dologban ternek el az osztalyok. Lepesrol lepesre haladjatok

Definialjatok 4 osztalyt:
- `Allat` felnott osztalyt, super class, amelyiktol orokol majd a tobbi, `Nev:int` attributummal rendelkezik es `__init__` fuggvennyel, melyen kereszul erteket adtok a `Nev` attributumnak
- `Macska` osztalyt, amelyik az `Allat` osztalytol fog orokolni, es terjesszetek ki (adjatok hozza) egy attributumot `MegfogottEgerekSzama:int`, es `__init__` fuggvenyt, amelyen keresztul erteket adtok a `Nev` es a  `MegfogottEgerekSzama` attributumoknak. Bemutatkozasa a kovetkezo: **"A nevem {Nev} es egy macska vagyok. {MegfogottEgerekSzama} egeret fogtam mar"**
- `Kutya` osztalyt, amelyik az `Allat` osztalytol fog orokolni, es terjesszetek ki (adjatok hozza) egy attributumot `MegharapottPostasokoSzama:int`, es `__init__` fuggvenyt, amelyen keresztul erteket adtok a `Nev` es a  `MegharapottPostasokoSzama` attributumoknak. Bemutatkozasa a kovetkezo: **"A nevem {Nev} es egy kutya vagyok. {MegharapottPostasokoSzama} postast haraptam mar meg"**
- `Eger` osztalyt, amelyik az `Allat` osztalytol fog orokolni, es terjesszetek ki (adjatok hozza) egy attributumot `MegvettSajtSulya:float`, es `__init__` fuggvenyt, amelyen keresztul erteket adtok a `Nev` es a  `MegvettSajtSulya` attributumoknak. Bemutatkozasa a kovetkezo: **"A nevem {Nev} es egy eger vagyok. Eletemben mar megettem {MegvettSajtSulya}kg sajtot"**

Definialjatok egy `Main()` fuggvenyt:
- Ahol tetszoleges szamu allatot hoztok letre (legalabb 1 macskat, 1 kutyat es 1 egeret)
- Tegyetek oket egy listaba [link](https://github.com/tocee123/spskn_api_2/blob/main/!OnLessons/2023-01-27_oop_inheritance_sk.md#priklad-so-studentami)
-  `for` ciklissal irjatok ki a kepernyore a bemutatkozasukat.

## Segitseg a bemutatkozashoz
Vagy definialjatok a `def __str__(self)->str:` vagy csinaltok egy `def MutatkozzBe()->str` fuggvenyt az osszes osztalyban
### Pelda `__self__` re
```py
class Person:
    Name:str
    Age:int
    
    def __init__(self, name:str, age:int) -> None:
        self.Age = age
        self.Name = name

    def __str__(self):
        return f"Hi, i'm {self.Name} and i am {self.Age} years old"

person = Person("Aladar", 18)
print(person)
```
### Pelda a `MutatkozzBe`re
```py
class Person:
    Name:str
    Age:int
    
    def __init__(self, name:str, age:int) -> None:
        self.Age = age
        self.Name = name

    def MutatkozzBe(self):
        return f"Hi, i'm {self.Name} and i am {self.Age} years old"

person = Person("Aladar", 18)
print(person.MutatkozzBe())
```

## Segitseg
- A `def__str__(self)->str:` itt talaltok peldat [link](https://github.com/tocee123/spskn_api_2/blob/main/!OnLessons/2023-01-27_oop_inheritance_sk.md#priklad-so-studentami)
- Az alosztalyok  (`Macska`, `Kutya`, `Eger`) `__init__` fuggvenyeben  hasznaljatok a kovetkezo lepeseket `HozzaadottAttributum` a kovetkezo az egyes osztalyokban: `MegfogottEgerekSzama`, `MegharapottPostasokSzama`, es `MegevettSajtSulya`
```py
def __init__(self, name: str, hozzaadottAttributum:int) -> None:
    super().__init__(name)  
    self.HozzaadottAttributum = hozzaadottAttributum
```

## Jegyek
1. Idoben leadjatok, es mind a 4 osztaly helyes definicioval rendelkezik, keszitettetek allatok listat, amibe inicialtatok legalabb 3 allatot, es kiirtatok a bemutatkozasukat
1. Terminus utan adjatok le, es mind a 4 osztaly helyes definicioval rendelkezik, keszitettetek allatok listat, amibe inicialtatok legalabb 3 allatot, es kiirtatok a bemutatkozasukat
1. Legalabb egy oroklest definialtok, legalabb egy instaciot letrehoztok az alosztalybol, es kiirjatok a bemutatkozasat
1. Individualisan
1. Ha semmit sem adtok le

# Example 
```
Hi, i'm Tom and i am a cat. I caught 0 mice
Hi, i'm Jaws and i am a dog. I bit 12 postmen
Hi, i'm Jerry and i am a mouse. I ate 487.21kg of cheese in my life
```
