# Domáca úloha
Domáca úloha bude zameraná na zoznamy (list) a prácou s nimi. Za úlohu budete mať napísať program, ktorý si od užívateľa vypýta možnosť úlohy:

1. Práca s prvočíslami
1. Práca s načítavaním čísel

> Užívateľ musí vybrať správnu hodnotu. Ak užívateľ zadal niečo mimo 1 a 2, tak si vypýtate od neho hodnotu úlohy (1 alebo 2) znovu! (`while`)

## Práca s prvočíslami
Vytvorte 2 zoznamy pre prvočísla a neprvočísla. Program si vypýta hornú hranicu intervalu a iteráciou od 2 po vypýtané číslo sa rozhodne o čísle, či je prvočíslo a do ktorého zoznamu ho pridá (`append`). Na konci vypíše hlášku: 
```
In the interval from 2 till 30 there are
prime numbers:      [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
not prime numbers:  [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
```
>[2, 3, 5, 7, 11] -> stačí do printu dať len zoznam, hranaté zátvorky a hodnoty v zozname Python pridá sám
## Práca s načítavaním čísel
Takýto príklad ste už mali, teraz využite zoznamy: kým užívateľ nezadá 0, budete načítavať prirodzené čísla (`float`) a pridávať do zoznamu. Keď užívateľ ukončí beh, vypíšete: počet, súčet a primer načítaných hodnôt

## Známkovanie
<ol>
<li> Odovzdáte pred ukenčením splatnosti, použijete zoznamy, funkcie, názvy premenných sú zrozumiteľné
</li>
<li> Nepoužívate funkcie (zoznamy musíte)
</li>
  <li> Individuálne
</li>
  <li> Individuálne
</li>  
  <li>ak neodovzdáte, alebo viacerí budete mať to isté</li>
</ol>

## Pomôcky
- `%` modulo
- `//` celočíselné delenie
- `while`
- `[]` inicializácia zoznamu, listu
- `append, sum, len` práca so zoznamami
# Házi feladat
Ez a házi feladat a listákkal (list), és a velük való műveletekkel foglalkozik. írjatok programot, amelyik a felhasználótól bekéri, milyen műveletet hajtson végre: 

1. Prímszámok kiírása
1. A beolvasott számokkal való összesített műveletek

> A felhasználónak pontosan kell megadnia a művelet számát, ha nem adott be 1est vagy 2est, akkor addig kérjétek tőle, míg azt meg nem teszi helyesen! (`while`)

## Prímszámok kiírása
Hozzatok létre 2 listát, egyet a prímszámkra másikat a nem prímszámokra. A program bekéri az intervallum felső határát, és lépésenként összegyűjti, helyes listába helyezi (`append`), osztályozza a számot attól függően, hogy prímszám-e vagy sem. A vegén megjeleníti: 
```
In the interval from 2 till 30 there are
prime numbers:      [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
not prime numbers:  [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
```
>[2, 3, 5, 7, 11] -> elég, ha a listát íratjátok ki, a szögletes zárójeleket és az értékekt a Python maga írja oda
## A beolvasott számokkal való összesített műveletek
Ilyen programot már egyszer csináltatok, most azzal a különbséggel, hogy listát alkalmaztok a számok tárolására: amíg a felhasználó nem ír be 0-t, addig beolvasod a természetes számot (`float`), és hozzáadod a listához. Ha a felhasználó befejezi a program futtatását, kiírod a beolvasott számok: számát, összegét és átlagát. 

## Osztályzás
<ol>
<li> Leadjátok a programot a határidő előtt, függvényeket, listákat használtok, a függvényeket és változókat értelmesen megneveztik annak függvényében, mit is tartalmaznak
</li>
<li> Ha nem használtok függvényeket (listákat kell)
</li>
  <li> Individuális
</li>
  <li> Individuális
</li>  
  <li> ha egyáltalán nem adjátok le, vagy éppen többen másoltok</li>
</ol>

## Segítség
- `%` modulo
- `//` egész számú osztás
- `while`
- `[]` a lista létrehozása, inicializálása
- `append, sum, len` műveletek listákkal

# Function example
```py
def IsPrime(number:int)->bool:
    pass
def PrintPrimesAndNotPrimes()->None:
    pass
def PrintAggregateFunctionsOnAList()->None:
    pass
def Main()->None:
    pass
```
`pass` when the function does not do anything (yet), just skipping

# Example
Bad request, it will loop till the correct number of operation is given
```
This program will display some mathematical games using lists in the background:
1] writes out prime and not prime numbers from 2 till the upper border of the interval you enter
2] it will collect floating point numbers till you hit 0, then writes out the sum, the count and the average of the numbers you entered    
What is your choice?: 3
The number has to be in: [1, 2]
What is your choice?: 6
The number has to be in: [1, 2]
What is your choice?: 9
The number has to be in: [1, 2]
What is your choice?: 7
The number has to be in: [1, 2]
What is your choice?: 1
Get upper border for the prime numers: 10
In the interval from 2 till 10 there are
prime numbers:      [2, 3, 5, 7]
not prime numbers:  [4, 6, 8, 9, 10]
```
Choosing to write out prime numbers
```
This program will display some mathematical games using lists in the background:
1] writes out prime and not prime numbers from 2 till the upper border of the interval you enter
2] it will collect floating point numbers till you hit 0, then writes out the sum, the count and the average of the numbers you entered    
What is your choice?: 1
Get upper border for the prime numers: 30
In the interval from 2 till 30 there are
prime numbers:      [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
not prime numbers:  [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
```
Choosing to write out collected numbers' aggregate functions
```
This program will display some mathematical games using lists in the background:
1] writes out prime and not prime numbers from 2 till the upper border of the interval you enter
2] it will collect floating point numbers till you hit 0, then writes out the sum, the count and the average of the numbers you entered    
What is your choice?: 2
Enter your number, 0 will end the loop: 9
Enter your number, 0 will end the loop: -9
Enter your number, 0 will end the loop: 1
Enter your number, 0 will end the loop: 234
Enter your number, 0 will end the loop: 32.124
Enter your number, 0 will end the loop: 68
Enter your number, 0 will end the loop: -94
Enter your number, 0 will end the loop: 15
Enter your number, 0 will end the loop: -6441
Enter your number, 0 will end the loop: -45
Enter your number, 0 will end the loop: 123
Enter your number, 0 will end the loop: 1.348411
Enter your number, 0 will end the loop: -9.5874
Enter your number, 0 will end the loop: 0
You entered 13 numbers, the sum is -6115.11, the average is -470.39
```
