#Rock paper scissors game
import random

three = ("rock" , "paper" , "scissors")
 
for one in three :
 	print ( )
 	

boo = True

win = 0
draw = 0
loose = 0

print ("------Rock🪨---Paper📄---Scissors✂️------ ")
print ( )

while boo :
	comp = random.choice (three)
	
	opt = input (" what option would you like? \n (rock ) , (paper ) or (scissors ) \n (q to quit ) : ")
	if comp == opt :
		print (f"------DRAW------ \n Your competitor chose {comp}, and you also chose {opt}")
		draw += 1
		
		
	elif comp == "rock" and opt == "paper" :
		print (f"------YOU WIN------ \n Your competitor chose {comp}, you chose {opt}")
		win += 1
	elif comp == "paper" and opt == "rock" :
		print (f"------YOU LOOSE------ \n Your competitor chose {comp}, you chose {opt}")
		loose += 1
	elif comp == "rock" and opt == "scissors" :
		print (f"------YOU LOOSE------ \n Your competitor chose {comp}, and you chose {opt}")
		loose += 1
	elif comp == "scissors" and opt == "rock" :
		print (f"------YOU WIN------ \n Your competitor chose {comp}, and you chose {opt}")
		win += 1
	
	elif comp == "paper" and opt == "scissors" :
		print (f"------YOU WIN------ \n Your competitor chose {comp}, and you chose {opt}")
		win += 1
	elif comp == "scissors" and opt == "paper" :
		print (f"------YOU LOOSE------ \n Your competitor chose {comp}, and you chose {opt}")
		loose += 1
	elif opt.lower ( ) == "q" :
		boo = False
		
print (f"You won {win} times , lost {loose} times and drew {draw} times")
