#Shopping cart program
foods = [ ]
prices = [ ]
total = 0

while True :
	food = input("Enter a food on your shopping list( Use q to quit) : ")
	if food == "q" :
		break
	else :
		price = float(input(f"What is the price of {food}? : "))
		foods.append(food)
		prices.append(price)
print("______Your Cart______")

for food in foods :
	print(food , end = " ")

for price in prices :
	total = total + price

print()
print(f"Your total expenditure is {total}" )
