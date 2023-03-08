# Dictionary

[Viac o slovnikoch najdete tu](https://input.sk/python2017/19.html)

Typ `dict` **slovník** (informatici to volajú **asociatívne pole**) je taká dátová štruktúra, v ktorej k prvkom neprichádzame cez poradové číslo (index) tak ako pri zoznamoch, n-ticiach a reťazcoch, ale k prvkom prichádzame pomocou **kľúča**. Hovoríme, že k danému kľúču je **asociovaná** nejaká hodnota (niekedy hovoríme, že hodnotu **mapujeme** na daný kľúč).

Samotný slovník zapisujeme ako takéto dvojice `(kľúč : hodnota)` a celé je to uzavreté v `'{'` a `'}'` zátvorkách. Slovník si môžeme predstaviť ako zoznam dvojíc (kľúč, hodnota), pričom v takomto zozname nemôžu byť dve dvojice s rovnakým kľúčom. Napr.

Key value pair: `kľúč : hodnota`
## Priklad
``` py
vek = {'Jan':17, 'Maria':15, 'Ema':18}
print(vek['Jan'])
```
```py
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(dict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(len(dict))
#3
```

```py
dict = dict(brand="Ford", model = "mustang", year=1964)
print(dict)
#{'brand': 'Ford', 'model': 'mustang', 'year': 1964}
```

Je tam podobnost s triedou. Trieda ma atributy/vlastnosti, to su u slovnika kluce.
```py
class Car:
    def __init__(self, brand:str, model:str, year:int) -> None:
        self.brand, self.model, self.year = brand, model, year
    
    def __str__(self) -> str:
        return f"{self.brand} {self.model}, {self.year}"
        
car = Car("Ford", "Mustang", 1964)
print(car)

dict = dict(brand="Ford", model = "mustang", year=1964)
print(dict)
#{'brand': 'Ford', 'model': 'mustang', 'year': 1964}
```

K hodnotam pristupujeme, ako pri zozname cez index `'[]'`
```py
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"],
  "electric": False,
}

print(dict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'colors': ['red', 'white', 'blue'], 'electric': False}
print(len(dict))
#5
print(dict["brand"])
#Ford
```
## Neexistujuca hodnota
Ak sa pokúsime zistiť hodnotu pre neexistujúci kľúč
``` py
vek = {'Jan':17, 'Maria':15, 'Ema':18}
print(vek['Juraj'])
```
> `KeyError: 'Juraj'`

Python nám tu oznámi `KeyError`, čo znamená, že tento slovník nemá definovaný kľúč `'Juraj'`. K prvkom mozeme pristupovat aj v takzvanom "bezpecnom rezime" cez methodu `get`. Ak nenajde pozadovany kluc, vrati hodnotu `None`
```py
dict = dict(brand="Ford", model = "mustang", year=1964)
print(dict.get("model"))
#mustang
print(dict["model"])
#mustang

print(dict.get("numberOfDoors"))
#None
print(dict["numberOfDoors"])
#KeyError: 'numberOfDoors'
```

> `slovnik.get(kluc, nahrada)` ak v slovniku sa nenachadza hodnota pod danym klucom, vrati nam hodnotu `nahrada`

```py
dict = dict(brand="Ford", model = "mustang", year=1964)
print(dict.get("numberOfWheels", "0"))
#0
```

## Pridanie noveho prvku
Rovnako, ako priraďujeme hodnotu do zoznamu, môžeme vytvoriť novú hodnotu pre nový kľúč:
``` py
vek = {'Jan':17, 'Maria':15, 'Ema':18}
vek['Hana'] = 16
print(vek['Hana'])
```

## Operacia in
Pri zoznamoch je to nasledovne:
```py
zoznam = [17, 15, 16, 18]
print(15 in zoznam)
```
> `True`
Operácia `in` v slovniku neprehľadáva hodnoty ale kľúče:
``` py
vek = {'Jan':17, 'Maria':15, 'Ema':18, 'Hana':16}
print(16 in vek)
print('Hana' in vek')
```

```
False
True
```

## Zoznam klucov
Keďže operácia `in` so slovníkom prehľadáva **kľúče**, tak aj for-cyklus bude fungovať na rovnakom princípe. Z tohto istého dôvodu funkcia `list()` s parametrom slovník vytvorí zoznam **kľúčov** a nie zoznam hodnôt:
```py
vek = {'Jan':17, 'Maria':15, 'Ema':18, 'Hana':16}
zoznam = list(vek)
print(zoznam)
```
```
['Jan', 'Maria', 'Ema', 'Hana']
```

## 3 dolezite metody na pracu s hodnotami slovnika
Slovníky majú definovaných viac zaujímavých metód, my si najprv ukážeme len 3 z nich. Táto skupina troch metód vráti nejaké špeciálne „postupnosti“:

- `keys()` - postupnosť kľúčov
- `values()` - postupnosť hodnôt
- `items()` - postupnosť dvojíc kľúč a hodnota

### Kluce, hodnoty, prvky
```py
vek = {'Jan':17, 'Maria':15, 'Ema':18, 'Hana':16}
print(vek.keys())
#dict_keys(['Jan', 'Maria', 'Ema', 'Hana'])
print(vek.values())
#dict_values([17, 15, 18, 16])
print(vek.items())
#dict_items([('Jan', 17), ('Maria', 15), ('Ema', 18), ('Hana', 16)])
```
### Kluce
```py
dict = dict(brand="Ford", model = "mustang", year=1964)
keys = dict.keys()
print(keys)
# dict_keys(['brand', 'model', 'year'])

dict["color"]="white"
print(keys)
#dict_keys(['brand', 'model', 'year', 'color'])
```
### Hodnoty
```py 
dict = dict(brand="Ford", model = "mustang", year=1964)
values = dict.values()
print(values)
#dict_values(['Ford', 'mustang', 1964])
dict["model"] = "Skoda"
print(dict)
# {'brand': 'Ford', 'model': 'Skoda', 'year': 1964}
print(values)
# dict_values(['Ford', 'Skoda', 1964])
```
## Update 
```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
thisdict.update({"color": "blue"})
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'blue'}
```
## Vymazanie prvku
- `del slovnik[kluc]` 
- `pop(kluc)`
- `popitem()` vyhodi posledny prvok 
```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
del car["brand"]
print(car)
#{'model': 'Mustang', 'year': 1964}

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
car.pop("year")
print(car)
#{'model': 'Mustang', 'year': 1964}

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
car.popitem()
print(car)
#{'model': 'Mustang', 'year': 1964}
```

## Prechadzanie cez prvky pomocou for cyklu

- `for key in car:` prechadzame cez kluce
- `for key, value in car.items` vrati nam 2 premenne **kluc** a **hodnotu**

```py
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for key in car:
	print(key)
	# brand
	# model
	# year
    
for key in car:
    print(car[key])
    # Ford
	# Mustang
	# 1964
    
for key in car:
    print(f'key:{key:<5}, value: {car[key]}')
    # key:brand, value: Ford
	# key:model, value: Mustang
	# key:year , value: 1964
 
for key, value in car.items():
    print(f'key:{key:<5}, value: {value}')
    # key:brand, value: Ford
	# key:model, value: Mustang
	# key:year , value: 1964
```

## Vonerene (nested) slovniky
```py
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
#{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
print(myfamily["child1"])
#{'name': 'Emil', 'year': 2004}
print(myfamily["child1"]["name"])
#Emil
```

Zhrňme všetko, čo sme sa doteraz naučili pre dátovú štruktúru slovnik:

- `slovnik = {}` prázdny slovník
- `slovnik = {kluc:hodnota, ...}` priame priradenie celého asociatívneho poľa
- `kluc in slovnik` zistí, či v slovníku existuje daný kľúč (vráti True alebo False)
- `len(slovnik)` zistí počet prvkov (dvojíc kľúč:hodnota) v slovníku
- `slovnik[kluc]` vráti príslušnú hodnotu alebo príkaz spadne na chybe KeyError, ak neexistuje
- `slovnik[kluc] = hodnota` vytvorí novú asociáciu kľúč:hodnota alebo zmení existujúcu
- `del slovnik[kluc]` zruší dvojicu kľúč:hodnota alebo príkaz spadne na chybe KeyError, ak neexistuje
- `for kluc in slovnik: ...` prechádzanie všetkých kľúčov
- `for kluc in sorted(slovnik): ...` prechádzanie všetkých kľúčov slovníka v utriedenom poradí
- `for kluc in slovnik.values(): ...` prechádzanie všetkých hodnôt
- `for kluc, hodnota in slovnik.items(): ...` prechádzanie všetkých dvojíc kľúč:hodnota
- `slovnik.get(kluc)` vráti príslušnú hodnotu alebo None, ak kľúč neexistuje
- `slovnik.get(kluc, náhradná)` vráti príslušnú hodnotu alebo vráti hodnotu parametra náhradná, ak kľúč neexistuje
