# bolean True or false
employee = True
if employee:
    print("CUrrently employeed")
else:
    print("Deasesed")
#Type Casting process converting type from one to another
student_name = "Mubashir"
ID_no = 1280
GPA = 3.79
Inrolled = True
print(type(student_name))   # → <class 'str'>
print(type(GPA))            # → <class 'float'>
print(type(ID_no))          # → <class 'int'>
print(type(Inrolled))       # → <class 'bool'>
#input take data from user
name = input(f"What is your name :")
Age = input(f"What is Your Age : ")
ID_no = input(f"Your ID is : ")
GPA = input(f"What GPA You Got : ")
Inrolled = input(f"IS You Are Inrolled")
print(f"My name is {name} I am {Age} Years Old I Got {GPA} In 1st semester {Inrolled} i am inrolled")