# if
## syntax
```py
if [condition]:
	block_of_code
elif [condition]:
	block_of_code
else:
	block_of_code
```

## Conditions
-   Equals:  `a == b`
-   Not Equals:  `a != b`
-   Less than:  `a < b`
-   Less than or equal to:  `a <= b`
-   Greater than:  `a > b`
-   Greater than or equal to:  `a >= b`
## Short hand if... else
also called **Ternary Operators**, or **Conditional Expressions**
```py
a = 2  
b = 330  
print("A") if a > b else  print("B")
```
prints "B"

## And
|a| b | a and b |
|--|--| --|
| False | False | False
| False | True| False
| True| False | False
| True | True| **True**

```py
a = 200  
b = 33  
c = 500  
if a > b and c > a:  
	print("Both conditions are True")
```
or you can use:
```py
a = 200  
b = 33  
c = 500  
if c > a > b:  
	print("Both conditions are True")
```
## Or
|a| b | a or b |
|--|--| --|
| False | False | False
| False | True| **True**
| True| False | **True**
| True | True| **True**

```py
a = 200  
b = 33  
c = 500  
if a > b or a > c:  
	print("At least one of the conditions is True")
```
## Nested If
You can have `if` statements inside `if` statements, this is called _nested_  `if` statements.
```py
x = 41  
  
if x > 10:  
	print("Above ten,")  
	if x > 20:  
		print("and also above 20!")  
	else:  
		print("but not above 20.")
```

## The pass Statement
`if` statements cannot be empty, but if you for some reason have an `if` statement with no content, put in the `pass` statement to avoid getting an error.
```py
a = 33  
b = 200  
  
if b > a:  
	pass
```

## Not
The  `not`  keyword is a logical operator.
The return value will be  `True`  if the statement(s) are not  `True`, otherwise it will return  `False`
```py
a = 9
if  a == 9:
	print('a is 9')
	
a = 10
if  a != 9:
	print('a does not equal 9')

a = 10
if  not(a == 9):
	print('a does not equal 9 second time')
```
