total = 0
def problem_2 (x_0, x_1):
	"""The goal of this project is to determine the summ of all even numbers in the fibonacci sequence that are under four million.
	The goal of this function is to modify a number of 
	"""
	x_2=x_0+x_1
	if x_2 %2=0:
		global total
		total +=x_2
	while x_2 <4e6:
		return problem_2(x_1, x_2)
