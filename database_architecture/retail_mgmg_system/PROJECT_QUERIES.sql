--- Search for Customer Info from Customer Name
Select * 
from CUSTOMER
Where "CustomerID" = &ID;


-- Search for Customer Number from Customer First Name and Last Name
Select "CustomerID" 
from Customer
Where "FirstName" = '&FN' and "LastName" = '&LN';

