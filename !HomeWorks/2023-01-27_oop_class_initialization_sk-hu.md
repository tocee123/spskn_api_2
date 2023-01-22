# Uloha 1
Zadefinujte triedu `Person`, ktora bude mat nasledovne 
- atributy/vlastnosti:
    - Meno (`string`)
    - Vek (`int`)
- metody:
    - inicializaciu `def __init__(self, meno:str, vek:int) -> None:`
    - pozdrav `def Pozdrav(self)->None:`, ktory vypise na obrazovku nasledujucu hlasku (ked meno je _Anton_ a vek _19_): `Ahoj, volam sa Anton a mam 19 rokov`

Urobte 2 instancie triedy a zavolajte na nich metodu `Pozdrav`

> anton = Person("Anton", 19)

# Feladat 1
Definialjatok egy `Person` osztalyt, amelyik a kovetkezo 
- attributumokat/tulajdonsagokat tartalmazza:
    - Nev (`string`)
    - Kor (`int`)
- fuggvenyek:
    - inicializacio `def __init__(self, nev:str,kor:int) -> None:`
    - udvozles `def Udvozolj(self)->None:`, amelyik a kovetkezo szoveget irja ki a kepernyore (ha a nev _Antal_ es a kor _19_): `Szia, Anton a nevem, es 19 eves vagyok`

Keszitsetek 2 `Person` instanciot/valtozot, es hivjatok meg rajtuk az `Udvozolj` fuggvenyt

> anton = Person("Antal", 19)
