# Working with strings
## string declaration
```py
#In py " == '
s = "hello"
print(s)
s = 'hello'
print(s)
s = ""
print(s)
s+="Hello"
print(s)
s+="banana"
print(s)
i = 1
s = str(i)
print(i, type(i))
print(s, type(s))
```
## Add numbers
```py
i1 = 10
i2 = 20
i3 = 30
i = i1+i2+i3
print(i)
```
## Add strings
```py
s1 = "Hello"
s2 = " "
s3 = "World"
s = s1+s2+s3
print(s)
```
### Be careful
```py
s1 = "Hello"
s2 = " "
s3 = "World"
s = s1
s = s + s2
s = s3 + s
print(s)
```

## Multi line strings
```py
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print()
#or
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print()
#or
a = 'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit,\nsed do eiusmod tempor incididunt\nut labore et dolore magna aliqua.'
print(a)
```

## Looping through every character
```py
for  x  in  "banana":
print(x)
```

## Get the length of the string
On strings you can call methods, you do it the following:
`[string variable's name].[name_of_the_method]()`
for example:
```py
lengthOfTheString = "abc".__len__()
#or
text = "lorem ipsum"
lengthOfTheString = text .__len__()
```
```py
s = input("Give me a sentece and i will tell you how many characters are in there: ")
print(s.__len__())

if(s.__len__() > 20):
	print("Very long sentence")
elif  s.__len__() > 10:
	print("Long sentence")
else:	
	print("Few words")
```
## In method
When you want to figure out if a `string` contains another `string` you use `in`
```py
txt = "The best things in life are free!"
print("free"  in  txt)
if("a"  in  "Brown fox"):
	print("Brown fox has [a]")
else:
	print("Brown fox does not have [a]")
#or
print(f"Brown fox {'has'  if  'a'  in  'Brown fox'  else  'does not have'} [a]")
```
Or moving repeating parts to variables
```py
stringToSearch = "a"
textToSearchIn = "Brown fox"
if(stringToSearch  in  textToSearchIn):
	print(f"\"{textToSearchIn}\" has [{stringToSearch}]")
else:
	print(f"\"{textToSearchIn}\" does not contain [{stringToSearch}]")
#or
print(f"\"{textToSearchIn}\"  {'has'  if  stringToSearch  in  textToSearchIn  else  'does contain'} have [{stringToSearch}]")
```
## If you would search for a string that does not contain another one
```py
txt = "The best things in life are free!"
print("expensive"  not  in  txt)
txt = "The best things in life are free!"

if  "expensive"  not  in  txt:
	print("No, 'expensive' is NOT present.")
```
## Case
```py
a = "Hello, World!"
print(a.upper()) 

a = "Hello, World!"
print(a.lower()) 

a = " Hello, World! "
print(a.strip())

a = "hello friend"
print(a.capitalize())
```

## Replace
```py
a = "Hello, World!"
print(a.replace("H", "J"))
print("FightClub".replace("Fight", "*****"))
```

## Formatting
```py
# age = 36
# name = "John"
# txt = "My name is "+name+", I am " + age
# print(txt)  

age = 36
txt = "My name is John, and I am {}".format(age)
print(txt)
##################################
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

##################################
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars.".format(quantity, itemno, price)
print(myorder)
##################################
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}.".format(quantity, itemno, price)
print(myorder)
##################################
quantity = 3
itemno = 567
price = 49.95123989123
myorder = f"I want to pay {price} dollars for {quantity} pieces of item {itemno}."
print(myorder)
##################################
quantity = 3
itemno = 567
price = 49.95123989123
myorder = f"I want to pay {price:.02f} dollars for {quantity} pieces of item {itemno}."
print(myorder)
```
## Escape characters
[You can read more about it here](https://www.w3schools.com/python/python_strings_escape.asp )
When you want to write out "" in print: _We are the so-called "Vikings" from the north._ Then you have to use `\"` this indicates, that " is used as visible character, the following won't work:
```py
txt = "We are the so-called "Vikings" from the north."
print(txt)
```
you have to use 
```py
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
```
Some other spacing advices
```py
print("\nnew line\nanother new line\n\n2 new lines")
print("\tthere is a tab\tand another one")
print("Text".ljust(10," "),"another text")
print("Text".rjust(10," "),"another text")
```
## Other string methods
[You an read more about it here](https://www.w3schools.com/python/python_strings_methods.asp)
```py
print("123".isnumeric())
print("banana".islower())
print("BANANA".islower())
print("BANANA".isupper())

print("FightClub".startswith("F")) 
print("FightClub".startswith("f"))
print("FightClub".lower().startswith("f"))
print("FightClub".replace("Fight", "*****"))
```
