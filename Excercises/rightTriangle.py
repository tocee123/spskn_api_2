#Nacitajte 2 odvesny a vypocitajte preponu

#Olvassatok be a 2 befogot es szamoljatok ki az atfogot

a=3#float(input("Side 1 lenght: "))
b=4#float(input("Side 2 lenght: "))

print("The length of the hypotenuse: ",(a**2+b*b)**(1/2))

from cmath import sqrt
from numpy import square
print(f"The length of the hypotenuse:  {sqrt(square(a)+square(b))}")