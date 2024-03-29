# Uloha
> Nazov suboru: `2F_priezvisko_meno.py`

## ZMENA
**Pri nacitani pouzite subor `randomWords.txt`, ktory je pripojeny k ulohe!**

## Chod programu
1. Vygenerovane slova zapiste do vami urceneho suboru
2. Nacitajte slova a vypiste statistiky z prilozeneho `randomWords.txt` suboru

### Kroky
- Pomocou funkcie `GenerateRandomWord` vygenerujte 10 az 25 slov (`random`)
- ulozte ich do lubovolneho suboru (`text.txt`, `randomFile.txt`, atd...), definujte si vlastny oddelovac (medzera, `,`, `;`, novy riadok `\n`)
- Vypiste cely subor, ktory ste vytvorili
- Nacitajte slova zo suboru `randomWords.txt` a nasledne:
    - vypiste len tie, ktore su dlhsie ako 8 znakov
    - vypiste vsetky slova v abecednom poradi (`sort`)
    - zistite priemernu dlzku slova (spocitajte dlzky slov a vydelte poctom slov)

# Feladat
> A fajl neve: `2G_vezeteknev_nev.py`

## VALTOZAS
**A beolvasasnal hasznaljatok a `randomWords.txt` fajlt, amelyik a feladathoz van illesztve!**
## A program menete
1. A kigeneralt veletlen szavakat mentsetek el egy altalatok meghatarozott fajlba
2. A mellekelt `randomWords.txt` fajlbol olvassatok be a szavakat, es irjatok ki a statisztikat

### Lepesek
- A `GenerateRandomWord` fuggveny segitsegevel generaljatok 10-25 veletlen szot (`random`)
- mentsetek el egy tetszoleges fajlba (`text.txt`, `randomFile.txt`, stb...), valasszatok sajat elvalasztot (szokoz, `,`, `;`, uj sor `\n`)
- A mellekelt `randomWords.txt` fajlbol olvassatok be a szavakat, es irjatok ki a statisztikat:
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
def WriteRandomWordsToFile(filePath:str)->None:
    pass
def WriteOutStatisticsFromFile(filePath:str)->None:
    pass
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
# Expected output

## randomWords.txt content
```
sffejzjwptc,dumipesy,ilhvqntufv,jjfdlzfzcpon,vacpmwqnynnlufyojep,cdzfsiirg,ypvh,noyobnisskqvb,obqbrebemeab,siwclbvgpiwk,etpgryravlntrpj,wbzxypvfzjnimnnkpwco,liihce,sdwhinnahwkw,hyntyosvlbzm,rwiaiwrmgpwoqqughky,tuvpitym,qjhfgftwjrnjc,mnoxdwuesedfwdwblcf,ikqzpnrbd,iixgcsubove
```
Python program's output: 
```
Words that are longer than 8 characters are: sffejzjwptc, ilhvqntufv, jjfdlzfzcpon, vacpmwqnynnlufyojep, cdzfsiirg, noyobnisskqvb, obqbrebemeab, siwclbvgpiwk, etpgryravlntrpj, wbzxypvfzjnimnnkpwco, sdwhinnahwkw, hyntyosvlbzm, rwiaiwrmgpwoqqughky, qjhfgftwjrnjc, mnoxdwuesedfwdwblcf, ikqzpnrbd, iixgcsubove
Alphabetically sorted words: ['cdzfsiirg', 'dumipesy', 'etpgryravlntrpj', 'hyntyosvlbzm', 'iixgcsubove', 'ikqzpnrbd', 'ilhvqntufv', 'jjfdlzfzcpon', 'liihce', 'mnoxdwuesedfwdwblcf', 'noyobnisskqvb', 'obqbrebemeab', 'qjhfgftwjrnjc', 'rwiaiwrmgpwoqqughky', 'sdwhinnahwkw', 'sffejzjwptc', 'siwclbvgpiwk', 'tuvpitym', 'vacpmwqnynnlufyojep', 'wbzxypvfzjnimnnkpwco', 'ypvh']
Average length of the word is: 12.10
```
