# Dedenie
[link](https://input.sk/python2017/16.html)

Čo už vieme o triedach a ich inštanciách:
- triedy sú kontajnery atribútov/vlastnosti a funkcii:
  - atribúty/vlastnosti su premenne v triede
  - funkcie/metody
  - niektoré metódy sú „magické“: začínajú aj končia dvomi znakmi `__` a každá z nich má pre Python svoje špeciálne využitie
- triedy sú vzormi na vytvárame inštancií (niečo ako formičky na vyrábanie nejakých výrobkov)
- aj inštancie sú kontajnery atribútov:
  - väčšinou sú to súkromné premenné inštancií
- ak nejaký atribút nie je v inštancii definovaný, tak Python zabezpečí, že sa použije atribút z triedy (inštancia automaticky "vidi" triedne atribúty) - samozrejme, len ak tam existuje, inak sa o tom vyhlási chyba

## Dedicnost 
Dedičnosť **inheritance** označuje, že
- novú triedu nevytvárame z nuly, ale využijeme už existujúcu triedu
- tejto vlastnosti sa budeme venovať v tejto prednáške

Najjednoduchsie ti to viete predstavit, ak povieme, ze dana trieda **je**:
- _auto_ je _vozidlo_
- _student_ je _clovek_
- _vtak_ je _zviera_

### Zapis
```py
class Person:
    pass

class Student(Person):
    pass
```
Takyto zapis znamena, ze `Student` dedi (je) `Person`
## Pojmy

Vďaka tomuto naša nová trieda už pri "narodení" pozná základnú množinu atribútov/vlastnosti a funkcii/metod a my našimi definíciami metód tieto atribúty buď prepisujeme alebo pridávame nové. Tomuto mechanizmu sa hovorí **dedičnosť** a znamená to, že z jednej triedy vytvárame nejakú inú:

- triede, z ktorej vytvárame nejakú novú, sa hovorí **základná trieda**, alebo **bázová trieda**, alebo **super trieda** (base class, super class)
- triede, ktorá vznikne dedením z inej triedy, hovoríme **odvodená trieda**, alebo **podtrieda **(derived class, subclass)

Niekedy sa vzťahu základná trieda a odvodená trieda hovorí aj terminológiou **rodič** a **potomok** (potomok zdedil nejaké vlastnosti od svojho rodiča).

### Priklad s bodmi
```py
class Bod(object):
    X:int
    Y:int

    def __init__(self, x, y):
        self.X, self.Y = x, y

    #ked trieda ma zadefinovanu 'magicku' funkciu __str__ vrati nam stringovu reprezentaciu triedy
    def __str__(self):
        return f'Bod({self.X},{self.Y})'

    #defaultne hodnoty funkcii sa zadavaju pomocou rovna sa. Nasledujucu funkciu viete zavolat:
    # bod1.Posun() -> bod sa zavola so zakladnymy hodnotami, 0mi, to iste ako bod1.Posun(0, 0)
    # bod1.Posun(10) -> bod1.Posun(10, 0), takze sa posunie v osi x
    #Bbod1.Posun(dy=10) -> bod1.Posun(0, 10), posunie sa v osi y
    #bod1.Posun(10,20)
    def Posun(self, dx=0, dy=0):
        self.X += dx
        self.Y += dy
        
class FarebnyBod(Bod):
    Farba:str

    def ZmenFarbu(self, novaFarba:str)->None:
        self.Farba = novaFarba
    
def PosuvajZadkladnyBod()->None:
    bod = Bod(10, 20)
    print(bod)
    #posunuli sme o (0,0)
    bod.Posun(20)
    print(bod)
     #posunuli sme o (20,0)
    bod.Posun(-20)
    print(bod)
     #posunuli sme naspat o (-20,0)
    bod.Posun(dy=20)
    print(bod)
    #posunuli sme o (0,20)
    bod.Posun(30,40)
    print(bod)
    #posunuli sme o (30,40)
    
def PosuvajFarebnyBod()->None:
    # volá __init__() z triedy Bod
    fbod = FarebnyBod(200, 50)         
    # volá ZmenFarbu() z triedy FarebnyBod
    fbod.ZmenFarbu('red')
    # volá Posun() z triedy Bod             
    fbod.Posun(dy=50)      
    # volá __str__() z triedy Bod               
    print('fbod =', fbod)             
    
    
PosuvajFarebnyBod()
```

### Priklad so studentami

```py
class Person:
    Name:str
    Age:int
    
    def __init__(self, name:str, age:int) -> None:
        self.Age = age
        self.Name = name

    def __str__(self):
        return f"Hi, i'm {self.Name} and i am {self.Age} years old"
    
    def SayHi(self)->None:
        print(self)
        
class Student(Person):
    YearOfGraduation:int
    
    def __init__(self, name: str, age: int, yearOfGraduation:int) -> None:
        super().__init__(name, age)  
        self.YearOfGraduation = yearOfGraduation
    
    def __str__(self):
        return f"Hi, i'm {self.Name} and i am {self.Age} years old and i graduated in {self.YearOfGraduation}"
        
p = Person("name", 123)
p.SayHi()

s1 = Student("Aladar", 20, 2015)
s2 = Student("Bela", 19, 2012)
s3 = Student("Bela", 19, 2012)
students = [s1, s2, s3]
#alebo
#students = [tudent("Aladar", 20, 2015), Student("Bela", 19, 2012), Student("Bela", 19, 2012)]

for student in students:
  #Zavola sa SayHi z Person, ale ToString metoda __str__(self) uz zo Studenta
  student.SayHi()
```
