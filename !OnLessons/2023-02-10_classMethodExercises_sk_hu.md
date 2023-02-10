# Uloha 1
Vytvorte triedu `Vozidlo` s `Znacka`, `Spotreba`, ktora ma nasledujuce funkcie:
- `init(self, znacka, spotreba)->None:`
- `VypocitajSpotrebovanePalivo(self, trasa:float)->float`

Vas program ma:
- zadefinovat zoznam aspon s 2 vozidlami s nahodnymi hodnotami
- nahodne vygenerovat `float` trasu
- na obrazovku vypiste porovnanie, ktore vozidlo spotrebovalo menej paliva 

> nahodny `float` -> vygenerujte cele cislo s `randint` a vydelte 100-mi

> `names = ["SunValley", "Magellan", "Arsenal", "TeePee"]`

# Feladat 1
Keszitsetek `Jarmu` osztalyt `Gyarto`, `Fogyasztas`, amelyik a kovetkezo fuggvenyekkel rendelkezik:
- `init(self, gyarto, fogyasztas)->None:`
- `SzamitsdKiAzElfogyasztottUzemanyagot(self, ut:float)->float`

A programotok a kovetkezoket csinalja:
- definialjon listat legalabb 2 jarmuvel veletlenszeru ertekekkel
- veletlenszeruen kigeneralni egy `float` utat
- a kepernyore kiirni, hogy melyik auto fogyasztott kevesebb uzemanyagot

> veletlen `float` -> `randint` segitsegevel generaljatok veletlen szamot, es osszatok el 100zal

> `names = ["SunValley", "Magellan", "Arsenal", "TeePee"]`

# Uloha 2
Zadefinujte datovu strukturu `Student` s atributmi `Meno`, `Vyska`, `Vaha`. Zadefinujte `init` metodu pre tieto atributy. Dalsi atribut bude `Bmi`. Student bude mat aj funkciu:
- `VypocitajBmi(self)->None:`

Vas program ma:
- Vytvorit zoznam aspon 8 studentov s menami a nahodnymi hodnotanmi pre vysku a vahu
- Pre kazdeho studenta vypocitat BMI
- Vypisat na obrazovku 3 studentov s najmensim BMI (vypisat: meno, vahu, vysku, bmi)

Mate zoznam mien studentov

> nahodny `float` -> vygenerujte cele cislo s `randint` a vydelte 100-mi

> BMI sa pocita nasledovne: vaha/vyska^2. Vaha v kg a vyska v m

> `names = ["Alfonz", "Bob", "Cecil", "David", "Eric", "Fririch", "George", "Hugo", "Ivan"]`

# Feladat 2
Kesztisetek egy `Diak` osztalyt a kovetkezo attributumokkal `Nev`, `Magassag`, `Suly`. Definialjatok az `init` fuggvenyt ezekre a tulajdonsagokra. Kovetkezo attributum legyen a `Bmi`, es a diak tartalmazza a kovetkezo fuggvenyt:
- `SzamoldKiABmit(self)->None:`

A programotok a kovetkezot csinalja:
- Keszitsen listat legalabb 8 diakkal, nevukkel es a veletlen generalt magassagukkal es sulyukkal
- Mindegyik diaknal kiszamolni a BMIt
- Kiirni a kepernyore a 3 diakot a legmagasabb BMIvel (kepernyore: nev, suly, magassag, bmi)

Mate zoznam mien studentov

> veletlen `float` -> `randint` segitsegevel generaljatok veletlen szamot, es osszatok el 100zal

> BMI-t igy szamoljatok ki: suly/magassag^2. Suly kg-ban, magassag meterben

> `names = ["Alfonz", "Bob", "Cecil", "David", "Eric", "Fririch", "George", "Hugo", "Ivan"]`
