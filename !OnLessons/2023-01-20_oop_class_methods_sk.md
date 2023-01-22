# OOP

Podrobnejsie si mozete precitat o OOP na stranke [tu](https://input.sk/python2017/14.html)

Pracovali sme doteraz s datovymi typmi ako `int`, `float`, `str`, `bool`, `list`, `tuple`, dalej su tu datove typy ako `time`, `date`. Ako si, nad ktorymi mozeme mat:
- **operácie**: `7 * 8 + 9`, `'a' * 8 + 'b'`, `7 * [8] + [9]`
- **funkcie** : `len('abc')`, `sum(zoznam)`, `min(ntica)`, `'11 7 234'.split()`,`zoznam.append('novy')`, `g.create_line(1,2,3,4)`, `t.fd(100)`

##  Vlastný typ
V Pythone sú všetky typy objektové, t.j. popisujú objekty, a takýmto typom hovoríme **trieda** (po anglicky `class`). Všetky hodnoty (teda aj premenné) sú nejakého objektového typu, teda typu trieda, hovoríme im **inštancia triedy** (namiesto hodnota alebo premenná typu trieda).

```py
class Student:
    pass
```

> `pass` je prikaz, ktory nerobi nic, ale potrebujeme ho v tomto pripade, aby syntax jazyka bola zachovana

### Definovanie vlastneho typy a atributu
```py
#own type
class Student:
   pass

#object variable => class instance or data containers
fero = Student()
print(type(fero))
print(fero)

#attribute
fero.name = "test"
print(fero.name)
fero.name = "Frantisek"
print(fero.name)
```

>`fero = Student()` v pamati sa vytvorilo miesto velkostou potrebne pre typ `Student` a premenna `fero` ukazuje na to miesto v pamati, napriklad `<__main__.Student object at 0x000001825B3F7C40>`

### Vypis atributov
```py
class Student:
    pass

def WriteOutName(student)->None:
    print(f"My name is {student.name} {student.surname}")
    
bob = Student()
WriteOutName(bob)
```
> Vypise nasledovnu chybu: `AttributeError: 'Student' object has no attribute 'name'` V metode `WriteOutName` ocakavame, ze typ Student bude mat atributy\vlastnosti `name` a `surname`

```py
class Student:
    pass

def WriteOutName(student)->None:
    print(f"My name is {student.name} {student.surname}")
    
bob = Student()
bob.name = "Bob"
bob.surname = "Best"
WriteOutName(bob)
```
>Vypise: `My name is Bob Best`

### Hodnota vlastnosti je menitelna (mutable)
```py
class Student:
    pass

def WriteOutName(student)->None:
    print(f"My name is {student.name} {student.surname}")
    
bob = Student()
bob.name = "Bob"
bob.surname = "Best"
WriteOutName(bob)
bob.surname = "Clever"
WriteOutName(bob)
```
>Vypise: `My name is Bob Best My name is Bob Clever`

### Ukazovatel na tu istu adresu v pamati
```py
class Student:
    pass

def WriteOutName(student)->None:
    print(f"My name is {student.name} {student.surname}")
    
bob = Student()
bob.name = "Bob"
bob.surname = "Best"
WriteOutName(bob)

#new variable will point to the same address in memory
clint = bob
WriteOutName(clint)
clint.name = "Clint"
clint.surname = "Eastwood"
WriteOutName(clint)
WriteOutName(bob)

#same address in memory
print(f"{bob}\n{clint}")
```
Vypise
```
My name is Bob Best
My name is Bob Best
My name is Clint Eastwood
My name is Clint Eastwood
<__main__.Student object at 0x000001940D597C40>
<__main__.Student object at 0x000001940D597C40>
```
### Create method
```py
class Student:
    pass

def WriteOutName(student)->None:
    print(f"My name is {student.name} {student.surname}")

def CreateStudent(name:str, surname:str)->Student:
    #creating a new area in the memory with the size of Student and variable student will have the pointer to the address in the memory
    student = Student()
    #defining 2 attributes for the Student instance
    student.name = name
    student.surname = surname 
    return student

alice = CreateStudent("Alice","Awesome")
bob = CreateStudent("Bob", "Best")
#alice and bob are in different memory address
print(f"alice:\t{alice}\nbob:\t{bob}")
WriteOutName(alice)
WriteOutName(bob)

#variable dave points to the same address in the memory as alice
dave = alice
dave.name = "Dave"
WriteOutName(dave)
WriteOutName(alice)
print(f"alice:\t{alice}\ndave:\t{dave}")
```
Vypise
```py
alice:  <__main__.Student object at 0x0000020118AB6470>
bob:    <__main__.Student object at 0x0000020118AB6350>
My name is Alice Awesome
My name is Bob Best
My name is Dave Awesome
My name is Dave Awesome
alice:  <__main__.Student object at 0x0000020118AB6470>
dave:   <__main__.Student object at 0x0000020118AB6470>
```
### Atributy/vlastnosti zadefinovane v triede
Doteraz sme definovali atributy len na jednotlivych instanciach a mohli sa odlisovat, alebo vonkoncom aj chybat. Ak cheme zadefinovat vlastny typ s vlastnostami, ktore budu pritomne pre vsetky instancie, mozeme definovat nasledovne:
```py
class ClassName:
    StringAttribute:str
    IntAttribute:int
    FloatAttribute:float
    BoolAttribute:bool
```
>Vsimnite si zapis: nazov triedy velkym zaciatocnym pismenom, tak isto aj pre atributy/vlastnosti. (Takto sa jednoducho vizualne odlisia od ostatneho kodu)

```py
class Student:
    Name :str
    Surname:str

def WriteOutName(student)->None:
    print(f"My name is {student.Name} {student.Surname}")

def CreateStudent(name:str, surname:str)->Student:
    student = Student()
    student.Name = name
    student.Surname = surname 
    return student

alice = CreateStudent("Alice","Awesome")
bob = CreateStudent("Bob", "Best")

print(f"{alice}\n{bob}")
WriteOutName(alice)
WriteOutName(bob)
```
>Rozdiel medzi predoslim kodom a tymto je v tom, ze vo VSCode po napisani bodky sa nam zobrazi ponuka atributov/vlastnosti a metod, ktore vieme zavolat na danej instancii

### Funkcie na instanciach
Ak chceme zadefinovat funkciu vramci triedy, tak musime dat blok kodu pod "do" triedy (pouzi tab). Ak funkcia ma byt volana na instancii triedy, tak prvy parameter funkcie ma byt prikaz `self`:

```py
class LocalClass:
    StringAttribute:str
    def PrintOutStringAttribute(self):
        print(self.StringAttribute)

newInstance = LocalClass()
newInstance.StringAttribute = "Str"
newInstance.PrintOutStringAttribute()
```
>Vsimnite si posledny riadok, ked volame `PrintOutStringAttribute` na instancii, nema vstupny parameter. Ten `self` je vlastne ta instancia

Priklad:
```py
class Student:
    Name :str
    Surname:str
    #Pay attention to self!
    def WriteOutName(self)->None:
        print(f"My name is {self.Name} {self.Surname}")

def CreateStudent(name:str, surname:str)->Student:
    student = Student()
    student.Name = name
    student.Surname = surname 
    return student

alice = CreateStudent("Alice","Awesome")
bob = CreateStudent("Bob", "Best")

print(f"{alice}\n{bob}")
alice.WriteOutName()
bob.WriteOutName()
```
### Init- Konstruktor
Doteraz sme pouzivali na vytvaranie instancie `Student` triedy metodu `CreateStudent`, ktorej vstupnymi parametrami boli `name` a `surname`. Ak chceme, aby instanciu `Student` triedy sme robili cez funkciu definovanu v triede samej, pouzimeje funkciu na inicializovanie `__init__(self...)`
```py
class Student:
    Name :str
    Surname:str
    
    def __init__(self, name:str, surname:str) -> None:
        self.Name = name
        self.Surname = surname
    
    def WriteOutName(self)->None:
        print(f"My name is {self.Name} {self.Surname}")
        
    def GetFullName(self)->str:
        return f"{self.Surname}, {self.Name}"
        
alice = Student("Alice", "Awesome")
bob = Student("Bob", "Brave")

alice.WriteOutName()
bob.WriteOutName()

print(f"Person's full name is: {alice.GetFullName()}")
```
>Vsimnite si, ako sme vyrobili instanciu `alice = Student("Alice", "Awesome")`, ako sme zavolali funkciu `alice.WriteOutName()` a `print(f"Person's full name is: {alice.GetFullName()}")`

### Funkcie nad instanciou vs. nad triedou
```py
class Student:
    Name :str
    Surname:str
    
    def __init__(self, name:str, surname:str) -> None:
        self.Name = name
        self.Surname = surname
    
    #instance function
    def WriteOutName(self)->None:
        print(f"My name is {self.Name} {self.Surname}")
        
    #class function
    def WriteOutName(student:"Student")->None:
        print(f"My name is {student.Name} {student.Surname}")
    
alice = Student("Alice", "Awesome")
bob = Student("Bob", "Brave")

alice.WriteOutName()
bob.WriteOutName()

Student.WriteOutName(alice)
Student.WriteOutName(bob)
```
Funkciu nad instanciou spoznate rychlo tym, ze ma ako prvy vstupny parameter `self` a zavolate ju nad instanciou triedy napriklad `alice.WriteOutName()`. Pomocou `self`u ma pristup k atributom/vlastnostiam danej instancie `print(f"My name is {self.Name} {self.Surname}")`. Na druhej strane funkcia nad triedou nema self, ale student, ako parameter. Volame ju trieda.nazovMetody(vstupneParametre) `Student.WriteOutName(alice)`
