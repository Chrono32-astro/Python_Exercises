#Countdown timer
import time
x = int(input("How long in seconds should the timer run for? : "))
for x in reversed(range (0 , x, )) :
	sec = x % 60
	min = int(x / 60) %60
	hrs = int(x /3600) %24
	time.sleep(1)
	print(f"{hrs:02}:{min:02}:{sec:02}")
print("horray")