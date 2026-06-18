foods=[]
prices=[]
total=0
while True:
    food=input("Which Food You Want To Like To Buy or(q for quit) : ")
    if food=="q":
        break
    else:
        price=float(input(f"Ente The Price Of {food} : "))
        foods.append(food)
        prices.append(price)

print("----- Your Cart -----")
for food in foods:
    print(food, end=" ")

print()
for price in prices:
    total+=price

print(f"Your Total Is: {total}pkr")    