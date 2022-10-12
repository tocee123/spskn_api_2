#EASY nxn

# I****
# I****
# I****
# I****
# I****

n=5
for i in range(n):
    for j in range(n):
        if j==0 :
            print("I", end="") 
        else:     
            print ("*", end="")
    print()

# Version 2    
# print(n*(f"I{(n-1)*'*'}\n"))

# Version 3
# n=5
# result = ""
# for i in range(n):
#     for j in range(n):
#         if j==0 :
#             result+="I"
#         else:     
#             result+="*"
#     result+="\n"
# print(result)


# Version 4
# n=5
# result = ""
# for i in range(n):
#     for j in range(n):
#         result+= "I" if j == 0 else "*"
#     result+="\n"
# print(result)

#HARDER:
# **I**
# **I**
# **I**
# **I**
# **I**       
    
    
# def vytvorPrvyRiadok(pocetHviezdiciek):
#     #return f'{pocetHviezdiciek*"*"}I{pocetHviezdiciek*"*"}'
#     return pocetHviezdiciek*'*'+'I'+pocetHviezdiciek*'*'

# pocetRiadkov = 5
# for riadok in range(pocetRiadkov):
#     print(vytvorPrvyRiadok(pocetRiadkov//2))