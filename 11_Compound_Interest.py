# Compound Interest calculator

principal= float(input("What is the principal amount? : "))
while principal <= 0 :
	print("Invalid input, the principal can't be negative or zero")
	principal= float(input("What is the principal amount? : "))
rate = float(input("What is the interest rate percentage? : "))
while rate > 100 or rate < 0 :
	print("The interest rate can only be a percentage, meaning it must not be larger than 100 or less than or equal to zero.")
	rate = float(input("What is the interest rate percentage? : "))
time = float(input("Input what is the time period that the interest is accrued for in years? : "))
	
interest = principal*(1+rate/(100))**time
print(f"Your interest considering these values is ${round(interest, 2)} . ")