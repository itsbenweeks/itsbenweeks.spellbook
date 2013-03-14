# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    power = 0
    total = 0
    for number in poly:
        total += float(number * x**power)
        power += 1
    return total

# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    count=1;result=[];
    if len(poly)==1:
        return [0.0]
    else:
        poly=poly[1:]
    for number in poly:
        coefficent = float(poly.index(number))
        result.append(number*count)
        count+=1
    return result

# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    x_1 = x_0-(evaluatePoly(poly, x_0)/evaluatePoly(computeDeriv(poly),x_0))
    product=[x_1, 0]
    if abs(product[0]-x_0)> epsilon:
        #print x_1, count
        product=computeRoot(poly, x_1, epsilon)
        product[1]=product[1]+1
        return product
    product =[x_0, 0]
    return product

# Test Cases
def test(function):
    if function == 'newton':
        print computeRoot([-13.39, 0.0, 17.5, 3.0, 1.0], 0.1, .0001)==[0.806790753796352, 7]
        print computeRoot([1, 9, 8], -3, .01)==[-1.0000079170005467, 5]
        print computeRoot([1, -1, 1, -1], 2, .001)==[1.0002210630197605, 4]
        print computeRoot([1, 2, 3, 4.3, -5], 0.3, 0.0001)==[-0.47771869826311336, 6]
        print computeRoot([-8, 2, 1], 20, 0.0001)==[2.0000000605441395, 6]
        print computeRoot([-8, 2, 1], 2, 0.0001)==[2, 0]
        print computeRoot([-8, 2, 1], -20, 0.0001)==[-4.00000000844848, 6]
        print computeRoot([-8, 2, 1], -4, 0.0001) ==[-4, 0]
        print computeRoot([4, 56, 0, 28, 0, 14, 0, 1], 1, 0.0001)==[-0.07124736072967754, 4]
