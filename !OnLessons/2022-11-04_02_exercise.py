texts = ""
while True:
    text = input("Write something: ")
    if(text == "0"):
        break
    print(f"You entered \"{text}\" it has {text.__len__()} characters")
    texts += f"{text}\n"

padding = "Any key ".__len__() + 1

option = int(input(f"Would you like to write out your texts in:\n{'1: '.rjust(padding,' ')}lower case\n{'2: '.rjust(padding,' ')}UPPER\n{'3: '.rjust(padding, ' ')}UPPER and lower as well\n{'Any key: '.rjust(padding,' ')}Nothing\n\nYour answer is: "))
if(option == 1):
    print(texts.lower())
elif(option == 2):
    print(texts.upper())
elif(option == 3):
    print(texts.upper())
    print(texts.lower())
else:
    print("you chose nothing to display"
