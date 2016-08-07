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


-- Search for Item Name using SKU--

Select "ItemName","Size" 
from  ITEM
Where ITEM."ItemSKU" = '&SKU';


-- Update Inventory quantities for an Item--
UPDATE INVENTORY 
SET "Quantity" = '&Quantity'
WHERE INVENTORY."ItemSKU" = '&SKU';


-- Query orders place by customer--
Select "OrderID", ITEM."ItemSKU", ITEM."ItemName", CUSTOMER."CustomerID"
from "ORDER", CUSTOMER, ITEM
where "ORDER"."CustomerID" = CUSTOMER."CustomerID" and "ORDER"."ItemSKU" = ITEM."ItemSKU" and CUSTOMER."CustomerID" = &CustomerID ; 


-- Query to get inventory count--
select INVENTORY."ItemSKU", sum(INVENTORY."Quantity") as "Quantity"
from INVENTORY 
group by INVENTORY."ItemSKU";

-- Query to get most ordered items in the past year--

SELECT "ITEM"."ItemName" as "Name", "ORDER"."ItemSKU" as "SKU", SUM("ORDER"."Quantity") AS "Quantity"
FROM "ORDER" INNER JOIN "ITEM" ON "ITEM"."ItemSKU" = "ORDER"."ItemSKU" WHERE "ORDER"."Date" > SYSDATE - 365 -- May want to worry about leap years
GROUP BY "ORDER"."ItemSKU", "ITEM"."ItemName" ORDER BY "Quantity" DESC;
