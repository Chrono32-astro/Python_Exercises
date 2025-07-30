#quizz game

q1 = "How many days are in a week?: "
q2 = "How many months are in a year?: "
q3 = "How many seconds are in a minute?: "
q4 = "How many weeks are in a year?: "
q5 = "How many years are in a decade?: "

questions = (q1, q2, q3, q4, q5)


op1 = ("a. 3 ", "b. 4  ", "c. 6 ", "d. 7 ")
op2 = ("a. 10 ", "b. 12 ", "c. 14  ", "d. 30 ")
op3 = ("a. 60 ", "b. 30  ", "c. 12 ", "d. 5 ")
op4 = ("a. 43 ", "b. 52  ", "c. 54 ", "d. 12 ")
op5 = ("a. 9 ", "b. 8  ", "c. 7  ", "d. 10 ")

options = (op1, op2, op3, op4, op5)

question_num = 0

answers ="d" , "b" , "a" , "c" , "d" 
guesses = [ ]
score = 0

for question in questions :
	print ("-----------------------------------------------")
	print(question)
	for option in options[question_num] :
		print(option)

	
	guess = input ("Choose the correct answer (a. b. c. d. ) ").lower( )
	guesses.append(guess)
	if guess == answers[question_num]:
		print("correct")
		score += 1
	else :
		print(f"Incorrect, the correct answer is {answers[0]}")
	question_num += 1
	
print("-----------------------------")
print("           Results        ")
print("-----------------------------")
print ("answers: " , end = " ")
for answer in answers :
	print(answer, end = " ")
print ( )
print ( )
print ( "guesses: " , end = " ")
for guess in guesses :
	print(guess, end = " ")
	
perc = (score / len(questions)) * 100
print ( )
print ( )
print(f"You scored {perc} % ")
