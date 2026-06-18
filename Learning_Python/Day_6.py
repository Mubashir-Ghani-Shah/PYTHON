# 2D List --> it is a list of list
fruits=["Apple","orange","banana"]
vegetable=["Tomato","Potato","Onion"]
meats=["Bakra","Ghaye","bhens","chicken"]
groceries=[fruits,vegetable,meats]
print(groceries[0][0])
for collection in groceries:
    for food in collection:
        print(food,end=" ")