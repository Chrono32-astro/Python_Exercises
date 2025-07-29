#Validate user input
# 1. username is not longer than 12 character
# 2. Username must not contain spaces
# 3. Username must not contain digits

username = input("What is your username? : ")
if len(username) > 12  :
	print("Your username cannot be longer than 12 character, try again.")
elif username.find(" ") != -1 :
	print("Your username cannot contain spaces")
elif username.isalpha() == False :
	print ("Your username cannot contain numbers, only letters")
else :
	print(f"Hi {username}")