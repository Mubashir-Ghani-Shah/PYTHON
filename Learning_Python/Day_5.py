# For Loop
#for x in range(1,20):--> for 1 to 20
#for x in reversed(range(1,20)): --> for 20 to 1
#for x in range(2,34,4):--> 2=start,34=End,4=steps
#for x in range(1,22):
 #   if x==13:
  #      continue
   # else:
#Time Counter
import time
My_time=int(input("What is Time In Seconds : "))
for x in range(My_time,0,-1):
     seconds=x%60
     minutes=int(x/60)%60
     hours=int(x/3600)
     print(f"{hours:02}:{minutes:02}:{seconds:02}")
     time.sleep(1)

print("Times Over!")
#Nested Loop --> a loop with another loop (outerloop,inner loop)
#for x in range(2):
 #    for y in range(2):
  #        print(x,y)
#Output in one line --> we want to give output in one line
#print(x, end="")-->b/t qoutetion you can add any thing e.g " ","-","+"etc
#Output in rows and columns:
rows=int(input("Enter The Number Of Rows: "))
coloumn=int(input("Enter The Number Of Coloumns: "))
symbol=input("Enter The symbol style: ")
for x in range(rows):
     for y in range(coloumn):
          print(symbol,end=" ")
     print()

# Collection --> single variable used to store multiple variables
# List[]--> ordered and changeable .can be Duplicates
# Set{}--> inordered and immutable,but Add/Remove Ok.No Duplicates
# Tuple()--> Ordered and Unchangable .Duplicates ok Faster

#List
Alphabets=["a","b","c","d"]
print(Alphabets)
#Set
Alphabets={"a","b","c","d"}
print(Alphabets)
#Tuple
Alphabets=("a","b","c","d")
print(Alphabets)
