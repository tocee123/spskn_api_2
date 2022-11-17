# Domáca úloha
Napíšte program, ktorý si od uživateľa vypýta, ako má zobraziť zadanú hodnotu:
1. binárne rozloženú
1. desatinne rozloženú
1. binárne aj desatinne rozloženú

Potom si vypýta číslo, ak hodnota možnosti výpisu bola korektná a zobrazí hodnotu. V príkladoch máte znázornené, ako by to malo vyzerať
## Pomôcky
- `%` modulo
- `//` celočíselné delenie
- `while`

### Postup pri zisťovaní rozloženia podľa deliteľa
1. kým je číslo vačšie ako `0` opakuj
1. text: [zvyšok po delení delitelom] x [deliteľ na exponent]
1. celočíselné delenie čísla a zvýšenie exponentu

## Použite
- 2 funkcie, ktoré vám vrátia textovú hodnotu výpisu
- 1 funkciu, ktorá vám len pomôže pri spúšťaní

# Házi feladat
Írjatok egy programot, amelyik a felhasználótól bekér egy értéket, ami alapján eldönti, milyen szorzatokra bontsa a bekért számot:
1. bináris
1. tizedes
1. bináris és tizedes

Ezek után bekéri a számot, amelyiket szorzatokra bont, ha a megfelelő opciót választotta. Az példák bekezdésben láthatjátok, hogyan is nézzen ki a kimenet.
## Segítség
- `%` modulo
- `//` egész számos osztás
- `while`

### Lépések a szorzatok felbontására
1. amíg a szám nagyobb, mint `0` ismételd
1. szoveg: [az osztóval való osztás utáni maradék] x [osztó a kitevőre]
1. a bekért szám egész számú osztása és a kitevő növelése

## Használjatok
- 2 függvényt, amelyek értéket adnak vissza
- 1 fő függvényt, amelyik nem ad vissza értéket, csak lefuttatja a programot

# Function example
```py
def ToDecimalProduct(number:int)->str:
    return ""
def ToBinaryProduct(number:int)->str:
    return ""
def Main()->None:
    pass
```
`pass` when the function does not do anything (yet)

_product(EN)_ súčin(SK), sorzat(HU)

# Example
Bad request
```
This program will write your chosen integer as:
1 binary product
2 decimal product
3 binary and decimal product
What do you choose? 121
You requested incorrect option, bye!
```
Choosing binary
```
This program will write your chosen integer as:
1 binary product
2 decimal product
3 binary and decimal product
What do you choose? 1
Enter your number: 121


Binary product of 123:
1 x 1
1 x 2
0 x 4
1 x 8
1 x 16
1 x 32
1 x 64
```
Choosing decimal
```
This program will write your chosen integer as:
1 binary product
2 decimal product
3 binary and decimal product
What do you choose? 2
Enter your number: 121


Decimal product of 123:
3 x 1
2 x 10
1 x 100
```
Choosing both
```
This program will write your chosen integer as:
1 binary product
2 decimal product
3 binary and decimal product
What do you choose? 3
Enter your number: 123


Binary product of 123:
1 x 1
1 x 2
0 x 4
1 x 8
1 x 16
1 x 32
1 x 64


Decimal product of 123:
3 x 1
2 x 10
1 x 100
```
