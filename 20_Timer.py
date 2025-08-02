

#Time counter

import time

res = int(input ("Start : "))
out = int(input ("End : "))

def counter (end, start = res) :
	for x in range (start , end+1 ) :
		print (x)
		time.sleep (1)
	print ("DONE")

counter (out)