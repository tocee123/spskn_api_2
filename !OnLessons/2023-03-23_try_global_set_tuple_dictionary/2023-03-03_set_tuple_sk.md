# Set
Používajú sa  na ukladanie viacerých položiek do jednej premennej. `set` su kolekcie: 
- netriedene
- nemenne
- bez duplikatov
## Zapis
```py
mySet = {"apple", "cherry", "banana", "cherry"}
#{'apple', 'banana', 'cherry'}
```
## Pristup
`set` nie je ako zoznam, takze k prvkom sa nedostaneme cez index, jedine:
- v podmienke sa vieme dopytovat, ci dany prvok existuje v `set`e pomocou `in` 
- cez `for` cyklus

## Priklad
```py
thisSet = {"apple", "banana", "cherry"}

for x in thisSet:
    print(x)
    # cherry
    # apple
    # banana

print("banana" in thisSet)
#True
```
## Pridat novy prvok
Existujuce prvky nevieme menit, ale pridat sa da pomocou `add()` methody:

```py
thisSet = {"apple", "banana", "cherry"}
thisSet.add("orange")
print(thisSet)
# {'apple', 'orange', 'cherry', 'banana'}
```

## Vymazanie zo set-u
```py
thisSet = {"apple", "banana", "cherry"}
thisSet.remove("banana")
print(thisSet)
# {'apple', 'cherry'}
thisSet.discard("apple")
print(thisSet)
# {'apple'}
```
## Viac metod na set-y
[Viac metod na sety najdete tu](https://www.w3schools.com/python/python_sets_methods.asp)

# Tuple 
Sa pouziva na uchovavanie viac prvkov v jednej premennej. `tuple` su nemenne kolekcie pouziva sa `'()'`
```py
mytuple = ("apple","banana", "cherry")
print(mytuple)
# ('apple', 'banana', 'cherry')
```
## Pristup k prvkom
K prvkom v `tuple` vieme pristupovat cez `'[]'` ako pri zoznamoch

```py
#Zoznam
myList = ["apple", "banana", "cherry"]
print(myList[0])
myList[0]="kiwi"
print(myList)
#['kiwi', 'banana', 'cherry']

mytuple = ("apple","banana", "cherry")
print(mytuple)
# ('apple', 'banana', 'cherry')
print(mytuple[0])
# apple
apple, banana, cherry = mytuple
print(apple, banana, cherry)
# apple banana cherry
```
