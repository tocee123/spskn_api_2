#https://blog.teclado.com/python-match-case/

# match variable:
#     case value1:
#         block of code
#     case value2:
#         block of code
#     case value3 | value4:
#         block of code when variable is value3 or value4
#     case _:
#         block of code for anything else


lang = "JavaScript"#input("What's the programming language you want to learn? ")
match lang:
    case "JavaScript":
        print("You can become a web developer.")
    case "Python":
        print("You can become a Data Scientist")
    case "PHP":
        print("You can become a backend developer")    
    case "Solidity":
        print("You can become a Blockchain developer")
    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")