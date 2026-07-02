#Function--> a block of reusable code place() after the function name to invoke it
def student(name,age):
    student("MK",20)
    print(student)

#return --> this statement is used to end a function and send a result back to the caller
# positional AARgument
def addition(x,y):
    z=x+y
    return z
print(addition(29,14))

def subtraction(x,y):
    z=x-y
    return z
print(subtraction(46,17))

def multiplication(x,y):
    z=x*y
    return z
print(multiplication(4,17))

def division(x,y):
    z=x/y
    return z
print(division(44,6))

def fullname(first,last):
    fullname=first+last
    print(fullname("Mubashir","Ghani Shah"))

#default arguments --> a default value for a ceratain parameters default is used when that argument is omitted make your fuinctions more flexible , reduces # OF ARGUment
# 1.positional 2.default 3.KEYWORD 4.atribution
#default Argument
def net_price(list_price,discount=0,tax=0.01):
    return list_price*(1-discount)*(1+tax)
print(net_price(400,0.1))

#Keyword arguments--> an atgument preceded by an identifer helps with readibility order of arguments doesn't matter
def hello(greeting,title,firstname,lastname):
    print(f"{greeting}{title}{firstname}{lastname}")

hello("Salam ","Mr. ","Mubashir ","Ghani Shah")

def get_phone(country,area,first,last):
    return f"{country}{area}{first}{last}"
phone_num=get_phone(country= "+92",area=331,first="000",last="0000")

print(phone_num)

#Arbitrary Arguments--> 
# * --> unpacking operator
#*args--> allows you to pass multiple non-key arguments
#**kwargs--> allows you to pass multiple keyword arguments
