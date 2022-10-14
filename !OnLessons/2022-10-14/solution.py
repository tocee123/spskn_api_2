print("This program will write out numbers between a closed interval that can be divided by the divisor")
min = int(input("Give one border for the interval: "))
max = int(input("Give another border for the interval: "))
divisor = int(input("Give divisor: "))


min, max = min if min <max else max, max if max>min else min
result = ""
for i in range(min, max+1):
    result += f"{i} " if i % divisor == 0 else ""

print(result)

