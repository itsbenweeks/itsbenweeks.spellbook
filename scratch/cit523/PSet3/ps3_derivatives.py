def computeDeriv(poly):
	'''
	Computes and returns the derivative of a polynomial function as a list of
	floats. If the derivative is 0, returns [0.0].
					 
	poly: list of numbers, length &gt; 0
	returns: list of numbers (floats)
'''
	result=[]; count=1.0
	if len(poly)==1:
		return [0.0]
	else:
		poly=poly[1:]
		for number in poly:
			coefficent = float(poly.index(number))
			result.append(number*count)
			count+=1
	return result
