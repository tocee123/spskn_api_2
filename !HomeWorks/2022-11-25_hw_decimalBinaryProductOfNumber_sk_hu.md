# Domáca úloha
Napíšte program, ktorý si od uživateľa vypýta spôsob a číslo, ako ho máte zobraziť:
1. binárne rozložené
1. desatinne rozložené
1. binárne aj desatinne rozložené

V príkladoch máte znázornené, ako by to malo vyzerať
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
Írjatok egy programot, amelyik a felhasználótól bekéri a módszert és egy számot, amelyet a következőképpen jeleníttek meg:
1. binárisan
1. tizedes bontásban
1. binárisan és tizedes bontásban

A példák bekezdésben láthatjátok, hogyan is nézzen ki a kimenet.
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
Enter your number: 123


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
Enter your number: 123


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
