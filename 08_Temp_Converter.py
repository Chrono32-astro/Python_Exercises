#Celsius to Fahrenheit
unit = input("What unit of measurement is it?(celsius or fahrenheit): ")
temp = float(input("What is the temperature?: "))
 
if unit == "celcius" :
	convert = temp * 9/5 + 32
	print(f"The temperature in fahrenheit is {round(convert, 2)}")
elif unit == "fahrenheit" :
	convert = (5 * temp - 160)/9
	print(f"The temperature in celcius is {round(convert, 2)},")
else :
	print("You must use (celcius/fahrenheit) for the unit and use any number for the temperature to be converted.")