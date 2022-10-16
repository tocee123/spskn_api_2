# Task
While the user doesn't enter `0`, collect the numbers he enters on the keyboard (even negative ones), when he enters `0`, the program returns the **sum** and the **count** of the entered numbers
```
Enter a number, 0 exits the program: 51
Enter a number, 0 exits the program: 215
Enter a number, 0 exits the program: -652
Enter a number, 0 exits the program: 123
Enter a number, 0 exits the program: 54
Enter a number, 0 exits the program: 12
Enter a number, 0 exits the program: 214 
Enter a number, 0 exits the program: -15
Enter a number, 0 exits the program: -153
Enter a number, 0 exits the program: 12
Enter a number, 0 exits the program: 154
Enter a number, 0 exits the program: 351 
Enter a number, 0 exits the program: -54651
Enter a number, 0 exits the program: 4561
Enter a number, 0 exits the program: 5113
Enter a number, 0 exits the program: 653
Enter a number, 0 exits the program: 645
Enter a number, 0 exits the program: 0
The sum of the 18 entered numbers is -43313
```

# Solution

Either you can use read the first number before the while loop:

```py
sum = 0
count = 0
enteredNumber=int(input("Enter a number, 0 exits the program: "))
while enteredNumber != 0:
    enteredNumber=int(input("Enter a number, 0 exits the program: "))
    sum=sum+enteredNumber
    count+=1
print(f"The sum of the {count} entered number{'s' if count>1 else ''} is {sum}")
```
or you can do it inside the while loop, but then you have to pay attention to the fact, that you have to break from the neverending cycle:
```py
sum = 0
count = 0
while True:
    enteredNumber=int(input("Enter a number, 0 exits the program: "))
    sum=sum+enteredNumber
    count+=1
    if enteredNumber==0:
        break
print(f"The sum of the {count} entered number{'s' if count>1 else ''} is {sum}")
```
