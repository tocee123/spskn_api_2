# Uloha
> Nazov suboru: `2F_priezvisko_meno.py`

- Pomocou funkcie `GenerateRandomWord` vygenerujte 10 az 25 slov (`random`)
- ulozte ich do lubovolneho suboru (`text.txt`, `randomFile.txt`, atd...), definujte si vlastny oddelovac (medzera, `,`, `;`, novy riadok `\n`)
- Nacitajte slova zo suboru a nasledne:
    - vypiste len tie, ktore su dlhsie ako 8 znakov
    - vypiste vsetky slove v abecednom poradi (`sort`)
    - zistite priemernu dlzku slova (spocitajte dlzky slov a vydelte poctom slov)

# Feladat
> A fajl neve: `2G_vezeteknev_nev.py`

- A `GenerateRandomWord` fuggveny segitsegevel generaljatok 10-25 veletlen szot (`random`)
- mentsetek el egy tetszoleges fajlba (`text.txt`, `randomFile.txt`, stb...), valasszatok sajat elvalasztot (szokoz, `,`, `;`, uj sor `\n`)
- Ujra olvassatok be a fajlbol a szavakat, majd 
    - irjatok ki azokat, amelyek hosszabbak 8 betunel
    - irjatok ki az osszes szot abc sorrendben (`sort`)
    - hatarozzatok meg az atlagos szohosszt (adjatok ossze az egyes szavak hosszat, majd osszatok el a szavak szamaval)

# Help
[link](https://github.com/tocee123/spskn_api_2/blob/main/!OnLessons/2023-03-10_file_sk.md)

```py
def GenerateRandomWord()->str:
    from random import choice, randint
    import string
    return ''.join([choice(string.ascii_lowercase) for _ in range(randint(4,15))])
```
## Read
MODIFIER:
- for writing `a` or `w`
- for reading `r`

```py
import os
full_path = os.path.dirname(__file__)
f = open(f"{full_path}\\test.txt", MODIFIER)
f.write("hello World")
f.close()
```
# Example
```
Words that are longer than 8 characters are: dvmgrgyaykwusoa, offygqwtbfb, pljhyruiu, sbxtezagmgxzga, vxjommzzvcw, xdcevxcbuoxg
Alphabetically sorted words: ['dvmgrgyaykwusoa', 'ijjculv', 'offygqwtbfb', 'oqspqd', 'pbyagg', 'pljhyruiu', 'ropoo', 'sbxtezagmgxzga', 'vxjommzzvcw', 'xdcevxcbuoxg']
Average length of the word is: 9.60
```
