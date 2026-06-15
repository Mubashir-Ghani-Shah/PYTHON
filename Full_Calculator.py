operator=input("What is the operator you want to use : ")
num1=float(input("What is the value of A : "))
num2=float(input("What is the value of B : "))
if operator =="+":
    result=float(num1+num2)
    print(f"By Addition Of A and B is {round(result,3)}")
elif  operator =="-":
    result=float(num1-num2)
    print(f"By Subtraction Of A and B is {round(result,3)}")
elif  operator =="*":
    result=float(num1*num2)
    print(f"By Multiplication Of A and B is {round(result,3)}")
elif  operator =="/":
    result=float(num1/num2)
    print(f"By Division Of A and B is {round(result,3)}")
else :
    print(f"{operator} is invalid")