def factR (n):
	'''Assumes that n is an int > 0
	returns n!'''
	if n==1:
		return n
	return n*factR(n-1)

def factL (n):
	'''Assumes that n is an int > 0
	returns n!'''
	res = 1
	while n>1:
		res *= n
		n-= 1
		#print res
	return res

def recurPowerNew(base, exp):
	'''
	    base: int or float.
		exp: int >= 0

		returns: int or float; base^exp
	'''
	if exp > 0 and exp %2 == 0:
		return recurPowerNew(base*base, exp/2)
	elif exp > 0 and exp %2 == 1:
		return base*recurPowerNew(base, exp-1)
	else:
		return 1

def gcdIter(a, b):
	'''
	a, b: positive integers
		 
	returns: a positive integer, the greatest common divisor of a & b.
	'''
	if a > b:
		divisor = b
	elif b > a:
	    divisor = a
	else: 
	    return a
																	        
	while a %divisor != 0 and b %divisor !=0:
		divisor -=1        
	
	return divisor

def gcdRecur(a, b):
	    '''
		a, b: positive integers
		returns: a positive integer, the greatest common divisor of a & b.
		'''
		if b == 0:
			return a
		else:
			return gcdRecur(b, a%b)

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
			    
    returns: True if char is in aStr; False otherwise
    '''
							    
    if aStr == '':
        return False
											        
    elif len(aStr)== 1:
        return aStr == char

    midStr = len(aStr)/2
    midChar = aStr[midStr]

	if  midChar == char:
	    return True
																			    
	elif midChar < char:
	    return isIn(char, aStr[midStr:])
														        
	else:
		return isIn(char, aStr[:midStr])
