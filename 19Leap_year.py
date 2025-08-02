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
    
   
#Time counter

import time

res = int(input ("Start : "))
out = int(input ("End : "))

def counter (end, start = 0) :
	for x in range (start , end+1 ) :
		print (x)
		time.sleep (1)
	print ("DONE")

counter (out)