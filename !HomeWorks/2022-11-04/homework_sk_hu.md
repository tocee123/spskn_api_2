


# Úloha
V tomto programe budete pracovať s prvočíslami, výpíšete všetky v danom intervale a to podľa nasledovných pravidiel:
 1. Od používateľa si vypýtate, čo sa má zobraziť:
	 1. **len** prvočísla
	 2. len **nie** prvočísla, vypíše aj ľubovoľný násobok 2 čísel, z ktorého sa skladá dané číslo
	 3. **všetky** čísla a napíše, či je **prvočíslo**, alebo ak **nie**, vypíše aj ľubovoľný násobok 2 čísel, z ktorého sa skladá dané číslo
1. Potom si vypýtate hornú hranicu intervalu výpisu. Interval je uzavretý z oboch strán: 1 až horná hranica.
## Dôležité
Odovzdaný súbor má mať formát: `2F_priezvisko_meno.py`
## Poznámky
_Prvočíslo: číslo, ktoré sa dá deliť len 1 a samým sebou_

_Uzavretý interval: patrí tam aj dolná aj horná hranica_

## 30-10-2022 Update
Ľahšia varianta za 3 bude:
1. vypýtate od používateľa kladné číslo `>1`
2. napíšete na obrazovku, či je to prvočíslo alebo nie

<!--
## 2-11-2022 Update
Na to, aby ste zistili, či číslo je prvočíslo, budete musieť prejsť celý interval čísel od `2` po `n-1`, kde `n` je hľadané číslo
Použiť môžete Pythonovu deklaráciu for cyklu
```py
for i in range(2, n):
	when modulo for any i is 0, n is not prime
else:
	it is prime```
```
alebo použijete takzvané flagy https://www.youtube.com/watch?v=lZ51aXq-VIg&ab_channel=CalebCurry čím si budete značiť, čo sa udialo
```py
isPrime = True
for i in range(2, n):
	when modulo for any i is 0, n is not prime 
		then isPrime = False
```
--->
# Feladat

Ebben a feladatban prímszámokkal fogtok dolgozni, kiírjátok őket egy adott intervallumban a következő szabályok szerint:
 1. A felhasználótól megkérdezitek, mit szeretne kiíratni:
	 1. **csak** a prímszámokat
	 2. csak **nem** a prímszámokat, és hozzá kiír egy tetszőleges szorzatot, amiből az adott szám áll
	 3. **minden** számot, amihez kiírja, hogy az adott szám **prímszám**, vagy ha **nem** prímszám, kiír egy tetszőleges szorzatot, amiből az adott szám áll
1. Utána felszólítja a felhasználót, hogy adja meg az intervallum felső határát, az intervallum zárt: 1től a felső határig
## Fontos
A leadott fájl formátuma: `2G_vezeteknev_nev.py`
## Megjegyzések
_Prímszám: olyan szám, ami csak 1-gyel és önmagával osztható_

_Zárt intervallum: az intervallumba beletartozik az alsó és felső határ is_
## 2022-10-30 Update
Könnyebb feladat 3asért:
1. bekértek egy pozitív egész számot `>1`
2. kiírjátok a képernyőre, hogy prímszám-e

<!--
## 2022-11-02 Update
Ahhoz, hogy egy számról megállapítsátok, hogy prímszám-e, végig kell haladni az összes lehetséges osztón `2`től `n-1`-ig, ahol `n` a szám, amelyikről ki akarjuk deríteni, hogy prímszám-e. 
kétféleképpen lehet Pythonban megkeresni, az első módszer Python specifikus:
```py
for i in range(2, n):
	when modulo for any i is 0, n is not prime
else:
	it is prime
```
Vagy úgynevezett flag, zászló változót használtok https://www.youtube.com/watch?v=lZ51aXq-VIg&ab_channel=CalebCurry amelyikkel azt jelzitek, történt-e változás:
```py
isPrime = True
for i in range(2, n):
	when modulo for any i is 0, n is not prime 
		then isPrime = False
```
--->

# Example
## 1- Just primes
```
This program will find the prime numbers for you. You can choose:
1- just the prime numbers
2- numbers that are not prime numbers
3- both
- 1
Give the upper border: 20
2, is a prime number
3, is a prime number
5, is a prime number
7, is a prime number
11, is a prime number
13, is a prime number
17, is a prime number
19, is a prime number
```

## 2- Just not primes
```
This program will find the prime numbers for you. You can choose:
1- just the prime numbers
2- numbers that are not prime numbers
3- both
- 2
Give the upper border: 20
4 equals 2*2
6 equals 2*3
8 equals 2*4
9 equals 3*3
10 equals 2*5
12 equals 2*6
14 equals 2*7
15 equals 3*5
16 equals 2*8
18 equals 2*9
20 equals 2*10
```
## 3- Both
This program will find the prime numbers for you. You can choose:
```
1- just the prime numbers
2- numbers that are not prime numbers
3- both
- 3
Give the upper border: 29
2, is a prime number
3, is a prime number
4 equals 2*2
5, is a prime number
6 equals 2*3
7, is a prime number
8 equals 2*4
9 equals 3*3
10 equals 2*5
11, is a prime number
12 equals 2*6
13, is a prime number
14 equals 2*7
15 equals 3*5
16 equals 2*8
17, is a prime number
18 equals 2*9
19, is a prime number
20 equals 2*10
21 equals 3*7
22 equals 2*11
23, is a prime number
24 equals 2*12
25 equals 5*5
26 equals 2*13
27 equals 3*9
28 equals 2*14
29, is a prime number
```
