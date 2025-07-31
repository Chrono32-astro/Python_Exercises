import random

die = { 1 : (
        "+-----+",
        "|     |",
        "|  o  |",
        "|     |",
        "+-----+"),
        2 : (
        "+-----+",
        "| o   |",
        "|     |",
        "|   o |",
        "+-----+"),
        3 : (
        "+-----+",
        "| o   |",
        "|  o  |",
        "|   o |",
        "+-----+"),
        4 : (
        "+-----+",
        "| o o |",
        "|     |",
        "| o o |",
        "+-----+"),
        5 : (
        "+-----+",
        "| o o |",
        "|  o  |",
        "| o o |",
        "+-----+"),
        6 : (
        "+-----+",
        "| o o |",
        "| o o |",
        "| o o |",
        "+-----+")}

dice = [ ]
total = 0

num = int(input ("How many dice would you like? :  "))

for val in range ( num )  :
	roll = random.randint ( 1, 6)
	print (roll)
	dice.append (roll)

for val in range (num) :
	for line in die.get (dice[val]) :
		print (line)
	
print ( )
for x in dice :
	total += int(x)
print (f"TOTAL = {total}")
print ( )
print ( )

#Leap year calculator
year = int(input("Enter a year to check if it is a leap year\n"))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))