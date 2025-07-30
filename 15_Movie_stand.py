#Concession Stand
#dictionary {key : value}

print ("These are the foods and beverages available ")
print ( )
print ("---------MENU---------")
menu = {
"pizza" : 3.00 ,
"nachos" : 4.50,
"popcorn" : 6.00,
"fries" : 2.50,
"chips" : 1.00,
"pretzels" : 3.50,
"soda" : 3.00,
"lemonade" : 4.25 }

cart = [ ]
sum = 0

for key, value in menu.items ( ) :
	print (f"{key :9} : ${value}")
print ( )

while True :
	order = input ("What item would you like to buy? (q to quit) :")
	if menu.get (order) != None :
		cart.append (order)
		sum += menu.get (order)
	elif order.lower ( ) == "q" :
		break
print ( )
print (" -----------Your order----------- ")

for food in cart :
	print ( food, end = " " )
print ( )
print (" -----------Total Cost----------- ")
print ( )
print (f"Your total cost is ${sum}")
print ( )
print ("------HAVE FUN WATCHING THE MOVIE 🧟------")