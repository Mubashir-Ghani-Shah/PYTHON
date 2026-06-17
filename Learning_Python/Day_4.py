# Logical Operator --> or , And , Not
age=25
is_Student=True
if age<40 or is_Student==True:
    print("A Valid Student")
else :
    print("Student is Overage")
#--------STRING METHODS---------
# Conditional Expression --> one line shortcut for if else statement(ternary operator) 
# FORMULA : x if condition else y
age = 19
status="ADult" if age>=18 else "Child"
print(status)
# String Functions
name = input("What is your name : ")
result = len(name) #--> to find the length of name
print(result)
result1 = name.find("a") #--> to find a character index
print(result1)
result2=name.rfind("a")
print(result2)
result3 = name.capitalize()#--> to capitalized first letter
print(result3)
result4=name.upper()#--> to upper case all letter
print(result4)
result5=name.lower()#--> to lower case all letter
print(result5)
result6=name.isdigit()#--> true when name contain only digits
print(result6)
result7=name.isalpha()#--> true when name contain only Alphabets
print(result7)
phone_number=input ("What is your contact number : ")
result=phone_number.count("3")#--> to find how many digit in input values
print(result)
result1=phone_number.replace("3","1")
print(result1)
#print(help(str)) --> help to gives syntax
#--------EXERCISE---------
if name >= str(12):
    print("you can't take more than 12 digits ")
elif not name.find(" ")==-1:
    print("Your username can't contain spaces ")
elif not name.isalpha():
    print("You cannot Add Digits ")
else:
    print(f"Welcome {name}")
#--------INDEXING------->accesing elements of a sequence using [](indexing operator)
# FORMULA : [start:end:step]
credit_no="123,456,789,987,654,321"
print(credit_no[3])
print(credit_no[0:9])
print(credit_no[3:])
print(credit_no[-2])#--> - means it will from last to fast
print(credit_no[::2])
#Format Specifier --> {value:flags}--> format a value based on what flags are inserted
number=float(input("What is your number for Format Specifier :"))
print(f"Round Decimal {number:.5f}")#--> round off decimal
print(f"{number:3}")#--> allocatte Spaces
print(f"{number:<}")#--> allocate 0 at the End
print(f"{number:>}")#--> allocate 0 at the start
print(f"{number:,}")#--> add comma b/t digits
# WHILE LOOP --> executes some code while some condition remain true
name = input("What is your name : ")
while name == "":
    print("Invalid name ")
    name = input("What is your name : ")

    
    print(f"Hello {name}")
