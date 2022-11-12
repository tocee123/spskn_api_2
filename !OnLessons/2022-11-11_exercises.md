# Priklady
## Premen int na string
```py
def  PremenIntNaString(i:int)->str:
	return  str(i)
cislo = 10
retazec = PremenIntNaString(cislo)

print(cislo, type(cislo))
print(retazec, type(retazec))
```
## Vypis na obrazovku
```py
def  VypisNaObrazovku(i:int)->None:
	print(i)
VypisNaObrazovku(132213)
```

## Zavolaj na cislo
```py
def  ZavolajCislo(i) -> None:
	print("Zavolali sme cislo:", i)
ZavolajCislo(132213)
```
## Posli sms na cislo
```py
def  posliSms(cislo, text) -> None:
	print(f"Poslali sme sms \"{text}\" na cislo {cislo}")
posliSms("0903123456", "Ahoj Adam")
```
