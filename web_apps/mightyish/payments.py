#!flask/bin/python
import requests
from dateutil.parser import parse
from models import Customer, Payment, PaymentMethod
from Queue import Queue
from threading import Thread



auth = HTTPBasicAuth()

'''
For this one, I would have a query select the "CLI" customer payments that were made 6 months
ago. Add these to a queue. If the is still active, then calcuate the cost through the number of
players. Send their payment information to the payment gateway.

Next, query the "FAM" customer payments that were made 1 month ago and add them to the queue.

This worker queue will provision calls to Python's Thread class, which aren't CPU threads, but will work
well enough for a process that is running at 2 AM.

Customers can be provided with payment history upon completion of a query to the Customer table.

There are a good number of edge cases here, what if a card stops working? Email the user, mark
payment method and customer as 'inactive'. This means that authentication will also need to
check customer status on login.

For testing,

## Confirm payment system needs
    Use a Dummy card & account for the payment service.
    That Customers get charged upon sign-up,

## DB needs
    Customer account is active.
    Customer can cancel their account.
    Customer is not active if payment is non-successful.

## UI Needs
    Customer can change payment method.
    Customer can add/remove players.
    Player cannot log in if parent customer is not active.
''' pass
