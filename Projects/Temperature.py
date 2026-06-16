import math
temp = float(input("What is the temperature : "))
unit = input("Enter your unit (C or F) : ")
if unit=="C":
    temp = round((9*temp)/5+32,3)
    print(f"Temperature in Farenheit is : {temp} F")
elif unit=="F":
    temp = round((temp-32)*5/9,3)
    print(f"Temperature in Centigrade is : {temp} C")