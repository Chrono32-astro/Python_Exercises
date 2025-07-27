#Shopping list
item = input("what item woud you like to buy? : ")
price = float(input("Cost of item: "))
quantity = int(input("Number of items bought: "))

total_cost=price*quantity

print(f"total expenditure is ${total_cost}")
print(f"You've bought {quantity} {item} for ${total_cost}")