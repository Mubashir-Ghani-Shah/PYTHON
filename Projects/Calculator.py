num1 = int(input("Enter Your number 1 : "))
num2 = int(input("Enter Your number 2 : "))
operator = input("Enter Your Operator sign : ")
if operator == "+":
    result = num1+num2
    print(f"Sum : {result}")
elif operator =="-":
    result= num1 -num2
    print(f"Subtaction : {result}")
elif operator == "*":
    result=num1*num2
    print(f"Multiplication : {result}")
elif operator =="/":
    result=num1/num2
    print(f"Division : {result}")
else:
    print(f"Invalid Operator {operator}")