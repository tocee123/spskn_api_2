numberOfSpaces = int(input("Enter the number of spaces before the word START, maximum is 20: "))
maxNumberOfSpaces = 20
if(0 <= numberOfSpaces <= maxNumberOfSpaces):
    print(f"{numberOfSpaces*' '}START")
else:
    print(f"The number of spaces is not in the range 0-{maxNumberOfSpaces}")