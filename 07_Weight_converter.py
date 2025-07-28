#Python weight converter
weight = float(input ("What is the weight you want to convert? : "))
unit = input ("What unit is the weight? (kg/pounds) : ")
if unit == "kg" :
	convert = weight * 2.205
	print(f"Your weight in pounds is {convert}")

elif unit == "pounds" :
	convert = weight / 2.205
	print(f"Your weight in kilograms is {convert} ")
else :
	print("unit is required in said format")
