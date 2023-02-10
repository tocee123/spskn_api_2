# Uloha 1
Vytvorte triedu `Vozidlo` s atributmi `Znacka`, `Spotreba`, ktora ma nasledujuce funkcie:
- `init(self, znacka, spotreba)->None:`
- `VypocitajSpotrebovanePalivo(self, trasa:float)->float`

Vas program ma:
- zadefinovat zoznam aspon s 2 vozidlami, atributy generujte nahodne
- nahodne vygenerovat `float` trasu, spolocna pre vsetky vozidla
- na obrazovku vypiste, kolko paliva spotrebovali jednotlive vozidla
- na obrazovku vypiste naujspornejsie vozidlo (Znacku aj Spotrebu)

> nahodny `float` -> vygenerujte cele cislo s `randint` a vydelte 100-mi

> mozete pouzit `names = ["SunValley", "Magellan", "Arsenal", "TeePee"]`

# Feladat 1
Keszitsetek `Jarmu` osztalyt `Gyarto`, `Fogyasztas` atributumokkal, amelyik a kovetkezo fuggvenyekkel rendelkezik:
- `init(self, gyarto, fogyasztas)->None:`
- `SzamitsdKiAzElfogyasztottUzemanyagot(self, ut:float)->float`

A programotok a kovetkezoket csinalja:
- definialjon listat legalabb 2 jarmuvel, ahol az atributumokat veletlenszeruen generalja
- veletlenszeruen kigeneralni egy `float` utat, amelyik egyforma az osszes jarmu szamara
- a kepernyore kiirni, hogy az adott uton az egyes jarmuvek mennyi uzemanyagot fogyasztottak
- a kepernyore kiirni, hogy melyik autonak van a legkisebb fogyasztasa (Gyarto, Fogyasztas)

> veletlen `float` -> `randint` segitsegevel generaljatok veletlen szamot, es osszatok el 100zal

> hasznalhatjatok `names = ["SunValley", "Magellan", "Arsenal", "TeePee"]`

# Uloha 2
Zadefinujte datovu strukturu `Student` s atributmi `Meno`, `Vyska`, `Vaha` a `Bmi`. Zadefinujte nasledujuce metody:
- `init` pre `Meno`, `Vyska`, `Vaha`
- `VypocitajBmi(self)->None:` ktora po zavolani vypocita BMI daneho studenta

Vas program ma:
- Vytvorit zoznam aspon 8 studentov s menami a nahodnymi hodnotanmi pre vysku a vahu
- Pre kazdeho studenta vypocitat BMI
- Vypisat na obrazovku 3 studentov s najmensim BMI (vypisat: meno, vahu, vysku, bmi)

> nestracajte cas na vymyslani mien

> nahodny `float` -> vygenerujte cele cislo s `randint` a vydelte 100-mi

> BMI sa pocita nasledovne: vaha/vyska^2. Vaha v kg a vyska v m

> `names = ["Alfonz", "Bob", "Cecil", "David", "Eric", "Fririch", "George", "Hugo", "Ivan"]`

# Feladat 2
Kesztisetek egy `Diak` osztalyt a kovetkezo attributumokkal `Nev`, `Magassag`, `Suly`, `Bmi`. Definialjatok a kovetkezo fuggvenyeket:
- `init` a `Nev`, `Magassag`, `Suly` tulajdonsagokra. 
- `SzamoldKiABmit(self)->None:` Ez kiszamitja, es elmenti az adott diak BMIjet

A programotok a kovetkezot csinalja:
- Keszitsen listat legalabb 8 diakkal, nevukkel es a veletlen generalt magassagukkal es sulyukkal
- Mindegyik diaknal kiszamolni a BMIt
- Kiirni a kepernyore a 3 diakot a legmagasabb BMIvel (kepernyore: nev, suly, magassag, bmi)

> neidozzetek a diakok nevei felett

> veletlen `float` -> `randint` segitsegevel generaljatok veletlen szamot, es osszatok el 100zal

> BMI-t igy szamoljatok ki: suly/magassag^2. Suly kg-ban, magassag meterben

> `names = ["Alfonz", "Bob", "Cecil", "David", "Eric", "Fririch", "George", "Hugo", "Ivan"]`
