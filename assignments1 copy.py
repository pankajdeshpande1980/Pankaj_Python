

def addition(a:float, b:float)-> float:
	"""
	Perform addition of two numbers.

	arg
	----
	a: float => First number 	
	b: float => Second number 
	return	
	-------
	result: float => The sum of the two numbers

	"""
	# Perform addition
	if a > b:
		diffrence= a - b
	else:
		diffrence= b - a
	addition_result = a + b
	# Return the result
	return addition_result

def subtraction(a:float,b:float)->float:
