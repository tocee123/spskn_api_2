# Valtozok
nevvel ellatott memoriaterulet, lehet: 
- egesz szam `10`
- tizedes szam `98.23`
- szoveg `"Hello"`

a valtozo neve:
- betuvel vagy `_` kell kezdodjon
- csak alfanumerikus karakterekt tartalmazhat (A-z, 0-9, es _ )
- kis/nagy betu kulonbseg (age, Age es AGE 3 kulonbozo valtozo)
- vigyazz a szokozre
  ## Pelda a jo valtozonevre
 ```py
myvar = "John"  
my_var = "John"  
_my_var = "John"  
myVar = "John"  
MYVAR = "John"  
myvar2 = "John"
```

a kovetkezok nem jok:
```py
2myvar = "John"  
my-var = "John"  
my var = "John"
```
## A jo valtozonev:
```py
#Camel case, az elso betu kicsi
myVariableName = "John"
#Pascal case, az elso betu nagy
MyVariableName = "John"
#Snake case 
my_variable_name = "John"
```
## Ertekadas
Egyenloseggel adunk erteket a valtozoknak:
```py
alma = "alma"
kisSzam = 10,
nagySzam = 9781239.13
pi = 3.14
print(alma)
print(kisSzam)
print(nagySzam)
print(pi)
```
egyszerre tobb valtozonak is adhatsz erteket
```py
x, y, z = "Orange", "Banana", "Cherry"  
print(x)  
print(y)  
print(z)
```
vagy egyszerre tobb valtozonak is adhatod ugyanazt az erteket
```py
x = y = z = "Orange"  
print(x)  
print(y)  
print(z)
```

## Kiiras a kepernyore
a `print()` paranccsal tortenik, 
```py
x = "Python is awesome"  
print(x)
```
```py
x = "Python"  
y = "is"  
z = "awesome"  
print(x, y, z)
```

### end
a `print()` fuggveny alapmeretezetten egy ujsort tesz a kiirt karakterlanc vegere
```py
print("x")
print("y")
```
kiirja a kovetkezot:
```
x
y
```
Ha meg akarjuk valtoztazni a sor veget, akkor meg kell hatarozni az `end` parametert (a `""` ures karaktert jelol)
```py
print("x", end ="")
print("y")
```
kiirja a kovetkezot:
```
xy
```
### sep
A `print()` fuggvenybe annyi kiirando objektumot teszunk, amennyit szeretnenk, ezeket viszont a `sep` szeparatorral valassza el egymastol, alapjaraton szokoz `" "`
```py
alma = "alma"
szam = 10
print(alma, szam, "vege")
```
kiirja a kovetkezot:
```
alma 10 vege
```
ha a szeparatort megvaltoztatjuk, legyen `"."`:
```py
alma = "alma"
szam = 10
print(alma, szam, "vege", sep=".")
```
kiirja a kovetkezot:
```
alma.10.vege
```
## Formatozas
```py
a = int(5)
b = int(2)
print("Ahoj %f" % (a-b))
print(a/b)

x = "%i.%i" % (a, b)
print(x) 

c = 519.2123
print(f'{c:.2f}')
```
kiirja:
```
519.21
Ahoj 3.000000
2.5
5.2
```
A formatozas a kovetkezokeppen tortenik: `""` koze kerul a szoveg, amit ki akarunk irni, a `%` jellel hatarozzuk meg, hogy oda szeretnenk tenni valamilyen erteket:
Az `print("Ahoj %f"  %  (a-b))` a `%f` azt jeloli, hogy azon a helyen lesz egy `float` (tizedes szam) tipusu ertek. A macskakormok utan jon ujra a `%` es felsoroljuk az erteketket (ebben az esetben `a-b`, ugyeljetek a zarojelre)
- `%f` float
- `%.2f` 2 tizedes jegyet ir ki
- `%i` integer
- `%s` string

### Pelda
```py
alma = "alma"
szam = 10
tizedesSzam = 981.23
kiirni = "Ma reggel vettem egy taska %st, amelyik %fgot nyomott, de ezert fizettem %i eurot, dragasag van" % (alma, tizedesSzam, szam)

print(kiirni)
```
kiirja:
```
Ma reggel vettem egy taska almat, amelyik 981.230000got nyomott, de ezert fizettem 10 eurot, dragasag van
```
(Ahogy latjatok, nem kell mindig a `print()`-ben osszerakni a szoveget, lehet kulon valtozoba is)
A tizedes szamoknal igy adjuk meg, mennyit tizedes jegyet irjon ki: `%.2f` persze, a 2-es helyett lehet mas szam is
```py
masikTizedesSzam = 142.81239
print("%.3f"%masikTizedesSzam)
```
kiirja:
```
142.812
```
### Format hasznalata
https://tutorial.eyehunts.com/python/python-print-format-float-example-code/
egy karakterlancba megirod a szoveget, a formazast, aztan teszel pontot es meghivod a format fuggvenyt, ahova behelyezed az ertekeket
`"Itt van egy {s}".format("szoveg")`
Ennel mar nincs `%i`:

- `%f` float
- `%.2f` 2 tizedes jegyet ir ki
- `%.0f` egesz szam
- `%s` string


```py
alma = "alma"
szam = 10
tizedesSzam = 981.23
kiirni = "Ma reggel vettem egy taska {:s}t, amelyik {:.2f}got nyomott, de ezert fizettem {:.0f} eurot, dragasag van".format(alma, tizedesSzam,szam)

print(kiirni)
```
kiirja:
```
Ma reggel vettem egy taska almat, amelyik 981.23got nyomott, de ezert fizettem 10 eurot, dragasag van
```
### Interpolacio
Szamomra a leheto legegyszerubb, amikor a formazott szovegbe egyenesen beirod azt, amit szeretnel megjeleniteni: `f"szoveg {ertek/valtozo}"` nincs se szazalekjel, se format a vegen:
```py
alma = "alma"
szam = 10
tizedesSzam = 981.23
kiirni = f"Ma reggel vettem egy taska {alma}t, amelyik {tizedesSzam:.3f}got nyomott, de ezert fizettem {szam} eurot, dragasag van"

print(kiirni)
```
kiirja:
```
Ma reggel vettem egy taska almat, amelyik 981.230got nyomott, de ezert fizettem 10 eurot, dragasag van
```
