import math
principle=0
rate=0
time=0
while principle<=0:
    principle=float(input("Enter The Principle Amount : "))
    if principle<=0:
        print("pricinple cannot be equal or zero ")

while rate<=0:
    rate =float(input("What is the rate of interest : "))        
    if rate<=0:
        print("Rate cannot be equal or zero ")
while time<=0:
    time=int(input("Enter The Time in Years : "))
    if time<=0:
        print("Time cant be less than or equal to zero ")

Total=principle*pow((1+rate/100),time)
print(f"Balance after {time} years : ${Total:.2f}")