# Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a
# felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi
# a megadott szám értéke!

# Napíš Python program, ktorý si vypýta celé pozitívne číslo nie väčšie ako 20 a na obrazovku vypíše slovo START tak, že pred ním bude toľko medzier, koľko uzívateľ zadal!
# Pomôcka: 
# - použite for cyklus (dá sa aj bez neho, ak máte, pripojte aj to)
# - buď poskladáte výsledok do premennej (start += reťazec), alebo hneď vypíšete na obrazovku (sep/end)
# - dbajte na "nie väčšie ako 20"

numberOfSpaces = int(input("Enter the number of spaces before 'START', it has to be < 20: "))

min = 0
max = 20

if min <= numberOfSpaces <= max:
    for n in range(numberOfSpaces):
        print(' ',end="")
    print("START")
else:
    print(f"The number is not between {min} <= {numberOfSpaces} <= {max}")
  
#Version 2  
# if min <= numberOfSpaces <= max:
#     result = ""
#     for n in range(numberOfSpaces):
#         result += " "    
#     print(result+"START")
# else:
#     print(f"The number is not between {min} <= {numberOfSpaces} <= {max}")

#Version 3
# if min <= numberOfSpaces <= max:
#     result = ""
#     for n in range(numberOfSpaces):
#         result += " "    
#     print(f"{result}START")
# else:
#     print(f"The number is not between {min} <= {numberOfSpaces} <= {max}")
    
#Version 4 without for cycle
# if min <= numberOfSpaces <= max:
#     print(f"{numberOfSpaces*' '}START")
# else:
#     print(f"The number is not between {min} <= {numberOfSpaces} <= {max}")