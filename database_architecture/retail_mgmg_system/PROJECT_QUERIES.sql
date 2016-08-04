--- Search for Customer Info from Customer Name
Select * 
from CUSTOMER
Where "CustomerID" = &ID;


-- Search for Customer Number from Customer First Name and Last Name
Select "CustomerID" 
from Customer
Where "FirstName" = '&FN' and "LastName" = '&LN';


-- Search for Available Quantity in Inventory for an Item--
Select "ItemName","Quantity" 
from INVENTORY, ITEM
Where INVENTORY."ItemSKU" = ITEM."ItemSKU" and INVENTORY."ItemSKU" = '&SK';


-- Update Inventory quantities for an Item--
UPDATE INVENTORY 
SET "Quantity" = '&Quantity'
WHERE INVENTORY."ItemSKU" = '&SKU';

