#Temperature program
temp = 25
is_sunny = True
if temp > 30 and is_sunny :
	print("We will go to the beach")
else :
	print("Stay in doors please")
	


temp = float(input("what is the temperature? : "))
is_sunny = input("Is it sunny?(True/False) : ")
if temp >= 30 and not is_sunny :
	print("We will not go to the beach")
elif is_sunny and not temp >= 30:
	print("Can't go, it's cold outside")
else :
	print("Those are all the possibilities")
	