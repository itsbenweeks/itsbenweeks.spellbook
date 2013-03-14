# Here are some global variables
product_cost = 61.74
tax = 0 
prices = [29.99, 9.00, 22.00, 0.50, 0.25]

def chooseState():
    ''' choice int
        choice >= 0 & choice < 4
    returns tax rate, if an improper choice is made, it will asks again.'''
    
    print ('1. Massachsetts')
    print ('2. Alabama')
    print ('3. California')
    state = raw_input('What state were the products purchased in? ')
    
    if [state == 1]:
        tax= (4.6305/61.74)
        return 'Massachusetts'

    elif [state == 2]:
        tax= (2.96352/61.74)
        return 'Alabama'
    
    elif [state == 3]:
        tax= (5.5566/61.74)
        return 'California'
    
    else:
        print 'That\'s not an answer!, do it again...'
        chooseState()

def cost(price, quantity):
    ''' price int or float, quantity int
    returns float cost such that the amount being paid can be easily calculated'''
    return price*quantity

def shippingRate (cost):
    '''cost int or float'''
    return cost*.2

def tarrif (cost, tax, shipping, tarrifRate):
    '''cost and tax and shipping and tarrifRate int or float
    returns a float for the amount added by a tarrifRate'''
    return (cost * (1+tax) + cost * shipping)*tarrifRate

def total (cost, tax, shipping, tarrif):
    '''cost and tax and shipping and tarrif int or float'''
    return (cost * (1+tax) + cost * shipping)*1.3

def profitMargin (total):
    ''' '''
    return (total * 3)

def foreignCurrency (profit):
    ''' '''
    return (profit * 1.79)

def report ():
    chooseState()
    while 
