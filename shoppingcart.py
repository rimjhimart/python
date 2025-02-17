foods = []
prices = []
total = 0
while True:
    food= input("enter the food you want(q to quit): ")
    if food.lower()=="q":
        break
    else:
        price = float(input(f"enter the price of the {food} in $: "))
        foods.append(food)
        prices.append(price)

print("------YOUR CART------")

for food in foods:
        print(food, end= " ")
        for price in prices:
            total+= price
        
print()
print(f"your total is: ${total}")
