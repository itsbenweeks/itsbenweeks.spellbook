## Ben Weeks
## 02/13/13
## CIT 523
## 
## Problem Set 2 
##

def payment_plan(monthlyPaymentRate, annualInterestRate, balance):
    month = 0
    total = 0
    while month < 12:
        payment = balance*monthlyPaymentRate
        balance -= payment
        interest = balance * (annualInterestRate/12)
        balance += interest
        month += 1
        total += payment
        print "Month: %s \nMinimum monthly payment: %s \nRemaining balance: %s" % (month, round(payment,2), round(balance,2))
        #The two decimal portion of this problem is solved by the round function.

    print "Total Paid: %s \nRemaining Balance: %s" %(round(total,2),round(balance,2))

def debt_in_year(annualInterestRate, balance):
    minimumPayment = 0
    monthlyInterestRate = annualInterestRate/(12.0)
    originalBalance = balance

    while balance > 0:
        balance = originalBalance
        minimumPayment += 10
        for month in range(12):
            balance -= minimumPayment
            balance *= 1+monthlyInterestRate

    print "Lowest Payment:", minimumPayment

def debt_in_year_bisect (annualInterestRate, balance):
    minimumPayment = 0
    monthlyInterestRate = annualInterestRate/(12.0)
    originalBalance = balance

    while abs(balance) > .02:
        minimumPayment += balance /12
        balance = originalBalance
        for month in range(12):
            balance -= minimumPayment
            balance *= 1+monthlyInterestRate
    print "Lowest Payment:", round(minimumPayment, 2)
    
def test (function):
    if str(function) == 'payment_plan':
        print "Tests for the Payment Plan portion"
        print '-'*12
        print "This is Test 1"
        print "="*12
        payment_plan(0.04,0.2,4213)

        print "\nThis is Test 2"
        print "="*12
        payment_plan(0.04,0.2,4842)

    elif str(function) == 'debt_in_year':
        print "Tests for the Exhaustive Ennumerative Portion"
        print '-'*12
        print "This is Test 1"
        print "="*12
        debt_in_year(0.2, 3329)
      
        print "\nThis is Test 2"
        print "="*12
        debt_in_year(0.2, 4773)
      
        print "\nThis is Test 3"
        print "="*12
        debt_in_year(0.2, 3926)


    elif str(function) == 'debt_in_year_bisect':
        print "Tests for the Bisecting Portion"
        print '-'*12
        print "This is Test 1"
        print "="*12
        debt_in_year_bisect(0.2,320000)

        print "\nThis is Test 2"
        print "="*12
        debt_in_year_bisect(0.18,999999)

    else:
        print 'Try that again.'

a= 'payment_plan'
b= 'debt_in_year'
c= 'debt_in_year_bisect'
