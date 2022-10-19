# Break and continue in for cycle

Without any condition it runs 10 times:
```py
n = 10
counter=0
for  i  in  range(1,n+1):
	counter+=1
	print(i)
print(f"Without any condition it ran for {counter} times")
```
If you add a step, it will run 5 times
```py
n = 10
counter = 0
for  i  in  range(1,n+1,2):
	counter += 1
	print(i)
print(f"With step set it ran for {counter} times")
```
If you add **continue** it will skip the rest of the cycle and goes to the next cycle, the whole loop runs for 10 times, but only 5 times the value of `i` is written to the terminal
```py
n = 10
counter = 0
for  i  in  range(1,n+1):
	counter += 1
	if  i % 2 == 0:
		continue
	print(i)
print(f"With continue it ran for {counter} times")
```
With the **break** command it runs for 3 times and then it jumps out of the the whole for loop
```py
counter = 0
for  i  in  range(1,n+1):
	counter += 1
	if  i % 3 == 0:
		break
	print(i)
print(f"With break it ran for {counter} times")
```

# The same applies to while cycle
```py
while [condition]:
	blockOfCode
else:
	anotherBlockOfCode
```
In while cycle there is a condition given, so it will be repeated till the condition is true.
```py
i = 10
while i>0:
	print(i)
	i-=1
```
As you can see, the condition has to be true at the beginning of the **while** cycle and adjust it while it runs
```py
i = 25
while i>10:	
	print(i)
	i+=1
	if(i == 30):
		break
```
Here it is tricky, the condition in `while` is `i>0`, but we increment the `i` so it would run forever, hence when we reach 30 it will break out from the cycle

# The else branche

```py
i = 0
while i<5:
    i+=1
    print("apple")
else:
    print("123")
```
This will print 5 times _apple_ and then at the end _123_, but if we `break` out of the cycle:
```py
i = 0
while i<5:
    i+=1
    print("apple")
    if(i==2):
        break
else:
    print("123")
```
It will print _apple_ 2 times, but _123_ won't be written
