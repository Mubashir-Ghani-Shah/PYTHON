import math
weight = float(input("What is your weight : "))
unit= input("Type your Unit (K or L) : ")
if unit=="K":
    weight = weight * 2.205
    unit="Lbs"
    print(f"Your Weight in Pounds is {round(weight,3)} {unit}")
elif unit == "L":
    weight = weight/2.205
    unit ="KG"
    print(f"Your Weight in KG is {round(weight,3)} {unit}")
else :
    print(f"Invalid Unit {unit}")