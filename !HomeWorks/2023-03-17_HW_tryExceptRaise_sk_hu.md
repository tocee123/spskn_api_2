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
- ak 2. cislo je > 3krat prve, program sa ukonci

## Hodnotenie

1. poslete vypracovane zadanie do terminnu a zadefinujete 2 vlastne chyby, pouzijete `raise`, `except`, funkcie 
1. poslete vypracovane zadanie  po termine a zadefinujete 2 vlastne chyby, pouzijete `raise`, `except` , funkcie
1. Individualne
1. Indivualne
1. neodovzdate, alebo kod bude velmi nezrozumitelny, robi nieco uplne ine

## Pomocka
[link na exception](https://github.com/tocee123/spskn_api_2/blob/main/!OnLessons/2023-03-23_try_global_set_tuple_dictionary/2023-03-03_tryExcept_sk.md)

# Feladat
Irjatok egy programot, amelyik a billentyuzetrol beolvas 2 egesz szamot kovetkezokeppen: 
- Mindket szam > 0
- A masodik beolvasott szam 3szor nagyobb, mint az elsonek beolvasott szam

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
- ak 2. cislo je > 3krat prve, program sa ukonci

## Hodnotenie

1. poslete vypracovane zadanie do terminnu a zadefinujete 2 vlastne chyby, pouzijete `raise`, `except`, funkcie 
1. poslete vypracovane zadanie  po termine a zadefinujete 2 vlastne chyby, pouzijete `raise`, `except` , funkcie
1. Individualne
1. Indivualne
1. neodovzdate, alebo kod bude velmi nezrozumitelny, robi nieco uplne ine

## Pomocka
[link na exception](https://github.com/tocee123/spskn_api_2/blob/main/!OnLessons/2023-03-23_try_global_set_tuple_dictionary/2023-03-03_tryExcept_sk.md)


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
