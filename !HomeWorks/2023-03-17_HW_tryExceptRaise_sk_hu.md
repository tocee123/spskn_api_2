# Uloha
Napiste program, ktory nacita z klavesnice 2 kladne cele cisla nasledovne: 
- Obe cisla musia byt > 0
- Druhe nacitane cislo musi byt aspon 3krat vacsie ako prve

Program musi vediet zvladnut:
- ked uzivatel zada nie cele cislo ('apple', '123asd', '12.312'), program sa neukonci, znovu si vypyta hodnotu od pouzivatela
- ked uzivatel zada cele cislo <= 0 -> kod 'hodi' (`raise`) vlastnu chybu, ktora indikuje, ze hodnota bola mensia alebo rovna nule
- ked uzivatel zada 2. cislo <= 3krat prve cislo -> kod 'hodi' (`raise`) vlastnu chybu, ktora indikuje, ze hodnota bola mensia, ako 3krat prve cislo

## Chod programu:
- zadefinujte aspon 2 typy chyb (`class`, ktora dedi od `Exception`)
    1. chybu hodite, ak cislo je zaporne alebo nula (<=0)
    2. chybu hodite, ak 2. cislo < 3krat 1. cislo
- od pouzivatela si pytajte cisla kym nesplnia podmienku (cele cislo > 0)
- ak 2. cislo je < 3krat prve, zopakujte cely proces
- ak 2. cislo je >= 3krat prve, program sa ukonci

## Hodnotenie

1. poslete vypracovane zadanie do terminnu a zadefinujete 2 vlastne chyby, pouzijete `raise`, `except` prikazy 
1. poslete vypracovane zadanie  po termine a zadefinujete 2 vlastne chyby, pouzijete `raise`, `except` prikazy
1. Individualne
1. Individualne
1. neodovzdate, alebo kod bude velmi nezrozumitelny, robi nieco uplne ine

## Pomocka
[link na exception](https://github.com/tocee123/spskn_api_2/blob/main/!OnLessons/2023-03-23_try_global_set_tuple_dictionary/2023-03-03_tryExcept_sk.md)
```py
try:
    pass 
except: 
    pass
finally:
    pass
```
> `pass` je prikaz, ktory nic nerobi, ale pre prazdne funkcie, bloky je nevyhnutny, aby python vedel spracovat skript

# Feladat
Irjatok egy programot, amelyik a billentyuzetrol beolvas 2 egesz szamot kovetkezokeppen: 
- Mindket szam > 0
- A masodik beolvasott szam 3szor nagyobb, mint az elso

A program a kovetkezokeppen kezeli a hibakat:
- ha a felhasznalo nem egesz szamot ad be ('apple', '123asd', '12.312'), a program nem fejezodik be, ujra bekeri a szamot a felhasznalotol
- ha a felhasznalo negativ egesz szamot vagy nullat ad be (<= 0) -> a program 'dob' (`raise`) egy sajat magatok altal irt hibat, amelyik azt jelzi, hogy a beadott szam negativ vagy 0
- ha a felhasznalo beadja a 2. szamot, es az 3szor kisebb, mint az elso szam -> a p program 'dob' (`raise`) egy sajat magatok altal irt hibat, ktora indikuje, amelyik azt jelzi, hogy a beadott szam kisebb, mint 3szor az elso

## Program menete:
- definialjatok legalabb 2 hibat (`class`, amelyik az `Exception` osztalytol orokol)
    1. hibat dobjatok, ha a beolvasott szam negativ vagy nulla (<=0)
    2. hibat dobjatok, ha a 2. szam < 3szor az 1. szam
- A felhasznaltol addig kerjetek be a szamot, amig az nem teljesiti a felteleket (egesz szam > 0)
- ha a 2. szam < 3szor az elso, az egesz program ujra lefut
- ha a 2. szam >= 3szor az elso, a program befejezodik

## Ertekeles

1. a megoldast hataridon belul kulditek be, definialtok 2 sajat hibat, hasznaljatok a `raise`, `except` parancsokat 
1. a megoldast hatarido utan kulditek, definialtok 2 sajat hibat, hasznaljatok a `raise`, `except` parancsokat 
1. Individualisan
1. Individualisan
1. ha nem adjatok le, vagy a kod nagyon kusza, esetleg teljesen mast csinal

## Segitseg
[link az exceptionokre](https://github.com/tocee123/spskn_api_2/blob/main/!OnLessons/2023-03-23_try_global_set_tuple_dictionary/2023-03-03_tryExcept_sk.md)

```py
try:
    pass 
except: 
    pass
finally:
    pass
```
> `pass` egy olyan parancs, ami nem csinal semmit, de a szintaxis miatt szukseges


# Example
```
Give me #1 positive integer: -9
The value -9 is negative or 0
Give me #1 positive integer: 0
The value 0 is negative or 0
Give me #1 positive integer: 9
Give me #2 positive integer: apple
Incorrect value
Give me #2 positive integer: 123asd
Incorrect value
Give me #2 positive integer: 12.312
Incorrect value
Give me #2 positive integer: 18
The value 18 is not at least 3x bigger than 9
Give me #1 positive integer: 30
Give me #2 positive integer: 91
91 is at least 3x bigger than 30, because 30 * 3 = 90 and 91 > 90
```
