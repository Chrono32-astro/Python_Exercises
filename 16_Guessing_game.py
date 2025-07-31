#Guessing game
import random

low = 1
high = 10

out = [ ]
score = 0
wrong = [ ]

is_running = True

print ("°°°°°°°°°°°GUESS GAME°°°°°°°°°°°")

while True :
	guess = input ("Take a guess at any random number in the range 1 - 10 : (e to end the game)  ")
	if guess.isdigit ( ) is is_running :
		print ( )
		if int(guess) == random.randint (low, high):
			print ("°°°°°°°°°°°°°°°")
			print ("Yay 🥳 the answer is correct!!! ")
		else :
			wrong.append ("w")
			out.append ("Yay")
			score += 1
			print ( )
	elif guess.isdigit ( ) is False and guess.lower ( ) == "e" :
		break
	elif guess.isdigit ( ) is False :
		print ( )
		print ("Your guess can only be a numeric input")
		print ( )

print ( )	
print ("°°°°°°°°Result°°°°°°°°")
print ( )
print (f"You got the right answer {out.count ("Yay")} times out of {wrong.count ("w")} valid attempts. " )