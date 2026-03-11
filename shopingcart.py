#SHOPING CART
#___________________________________________________________________________

fooditem = [] #LISTS
prices =[]
sum=0

print("-----------------------------WELCOME------------------------------")
while True:
    food = input("Enter the Item You would Like to Buy (Enter q to exit) ")
    if food.lower()=="q":
        break
    else:
        price = int(input("Enter the price of the Item (in$) "))
        print(f"~~~~~~{food} Entered to Cart Successfully for {price}$~~~~~~")
        fooditem.append(food)
        prices.append(price)
print("-----YOUR CART------")
for x in fooditem:
    print(f"{x.upper()}" , end=" , ")
print()
print(f"No. of items bought : {len(fooditem)}")
for price in prices:
    sum+=price
print()
print(f"Your total price Amount is {sum}$ ")
print("THANKS FOR SHOPPING WITH US!")