import math
#Arithmetic operator
a=2.8
a=a+5
a+=5
print(f"Addition {float(a)}")
a=a-6
a-=2
print(f"Subtraction {round(float(a),3)}")
a=a*4
a*=4
print(f"Multiplication {round(float(a),3)}")
a=a/2
a/=4
print(f"Division{round(float(a),3)}")

# Exponential / Power
a=a**1
a**=2
print(f"Exponential/Power {round(float(a),3)}")

#Modulus
a = a%2
a%=4
print(f"Modulus {round(float(a))}")

#BUILT IN ARITHMETIC OPERATIONS
#Round Operation
x=4.5869
result=round(x,2)
print(f"Round Operater {result}")
#absolute --> distance from Zero
x=7
result=abs(x)
print(f"Absolute {result}")
# Power Function --> Take a power of variable
x=5
result=pow(5,3)
print(f"Power Function {result}")
# Find Maximum and Minimum Value
x=4
y=5
z=8
result1=max(x,y,z)
print(f"Maximum {result1}")
result2=min(x,y,z)
print(f"Minimum {result2}")
# import Library --> constant and function 
# Pi
pi=print(f"Pi {round(math.pi,3)}")
#e
e=print(f"e {round(math.e,3)}")
# Square Root
print(f"Square Root {math.sqrt(4)}")
# Ceiling --> Round a floating number Up
print(f"Ceiling {math.ceil(5.4057)}")
