# 2D List --> it is a list of list
fruits=["Apple","orange","banana"]
vegetable=["Tomato","Potato","Onion"]
meats=["Bakra","Ghaye","bhens","chicken"]
groceries=[fruits,vegetable,meats]
print(groceries[0][0])
for collection in groceries:
    for food in collection:
        print(food,end=" ")

# Phone Numpad 
numpad=(( 1, 2, 3),
         (4, 5, 6),
         (7, 8, 9),
         ("*", 0, "#"))

for row in numpad:
    for num in row:
        print(num, end=" ")
    print()

# Dictionary --> a collection of {key:value} pairs ordered and changeable . No Duplicates
capitals= {"Pakistan":"Islamabad","Turkey":"Istanbul","USA":"DC","China":"Beijing"}
print(capitals.get("Turkey"))#--> to get the value of the following key
capitals.update({"Afghanistan":"Kabul"})
print(capitals)
capitals.pop("USA")# --> To remove 
print(capitals)
keys = capitals.values()
for key in capitals.keys():
    print(key)
values=capitals.values()
for value in capitals.values():
    print(values)

items=capitals.items()# --> it resemble a 2D list of tuple
print(items)
for key,value in capitals.items():
    print(f"{key}:{value}")

    
