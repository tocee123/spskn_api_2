# for cycle
## syntax
```py
for [cycle variable] in [iteratable object]:
	#block_of_code
else:
	#block_of_code(after the cycle is done)
```
## range() function
The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
### Example when the stop is set
```py
for i in range(6):
	print(i)
```
writes to the console:
```py
0
1
2
3
4
5
```
### Example when the start and the stop are set
```py
for i in range(1,6):
	print(i)
```
writes to the console:
```py
1
2
3
4
5
```
### Example when the start, the stop and the step are set
```py
for i in range(1,6,2):
	print(i)
```
writes to the console:
```py
1
3
5
```

## for cycle example with numbers
```py
start = 1
stop = 10
step = 2
for i in range(start,stop,step):
	print(i)
else:
	print("done")
```
writes to the terminal:
```
1
3
5
7
9
done
```

##  for cycle example with text
```py
text = "quick brown fox jumps over the lazy dog"
for c in text:
	print(c, end="..")
```
writes to the terminal:
```
q..u..i..c..k.. ..b..r..o..w..n.. ..f..o..x.. ..j..u..m..p..s.. ..o..v..e..r.. ..t..h..e.. ..l..a..z..y.. ..d..o..g..
```
##  for cycle example with arrays
```py
fruits = ["apple", "banana", "cherry"]  
for fruit in fruits:  
	print(fruit)
```
writes to the terminal:
```
apple
banana
cherry
```
## The break Statement
With the `break` statement we can stop the loop before it has looped through all the items
### Example with range
```py
start = 1
stop = 10
step = 1
for i in range(start,stop,step):
	if  i % 4 == 0:
		break
	print(i)
```
writes to the terminal:
```
1
2
3
```
### Example with array breaking after writing out
```py
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
	print(fruit)
	if(fruit == "banana"):
		break
```
writes to the terminal:
```
apple
banana
```
After writing `banana` it leaves the cycle
### Example with array breaking before writing out
```py
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
	if(fruit == "banana"):
		break
	print(fruit)
```
writes to the terminal:
```
apple
```
Before writing `banana` it leaves the cycle
## The continue Statement
With the `continue` statement we can stop the current iteration of the loop, and continue with the next:
### Example with range
```py
start = 1
stop = 10
step = 1
for i in range(start,stop,step):
	if  i % 4 == 0:
		continue
	print(i)
```
writes to the terminal (**4** and **8** are missing)
```
1
2
3
5
6
7
9
```
## Else in For Loop
The `else` keyword in a `for` loop specifies a block of code to be executed when the loop is finished:
```py
for x in  range(6):  
	print(x)  
else:  
	print("Finally finished!")
```

writes to the terminal:
```
0
1
2
Finally finished!
```
**Hint** when the loop breaks, the `else` block is not executed

```py
for x in range(6):
	if x == 3: 
		break
	print(x)
else:
	print("Finally finished!")

```

writes to the terminal:
```
0
1
2
```
