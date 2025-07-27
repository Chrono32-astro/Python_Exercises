#Python calculator
operator = input("Enter the operator you want to use ; addition(+) ; subtraction (-) ; multiplication (*) ; division (/) : ")
n1 = float(input ("Enter the first number: "))
n2 = float(input ("Enter the second number: "))
if operator == "+" :
	add = n1 + n2
	print (round(add, 2))
elif operator == "-" :
	minus = n1 - n2
	print (round(minus, 2))
elif operator == "*" :
	multiply = n1 * n2
	print (round(multiply, 2))
elif operator == "/" :
	divide = n1 / n2
	print (round(divide, 2))
else :
	print(f"Out of bounds, {operator} is invalid")