#Napiste program, ktory:
#- nacita meno pouzivatela z klavesnice
#- nacita vek pouzivatela z klavesnice
#- vypise: vek >= 18: 'Ahoj [meno], ty si uz dospely' alebo 'Ahoj [meno], ty este nie si dospely'

#Irj programot, amelyik:
#- Beolvassa a felhasznalo nevet a billentryzetrol
#- Beolvassa a felhasznalo eletkorat a billentyuzetrol
#- Kiirja a kepernyore: eletkor>=18 'Szia [nev], te mar felnott vagy' vagy 'Szia [nev], te meg nem vagy felnott

# useInterpolation = True
# name = input("What is your name?")
# age = int(input("How old are you?"))
# if(not useInterpolation):
#     if(age>=18):
#         print(f'Hi {name}, you are an adult')
#     else:
#         print(f'Hi {name}, you are not an adult')
# if useInterpolation: 
#     print(f'Hi {name}, you are {"not " if age<18 else "" }an adult')

useInterpolation = True
name = "Peter"# input("What is your name?")
age = 17 # int(input("How old are you?"))
if(age>=0):
    print(f"Hi {name}, you are {age} years old, you are {'not ' if age<18 else ''}an adult")
else:
    print("The age should be > 0")