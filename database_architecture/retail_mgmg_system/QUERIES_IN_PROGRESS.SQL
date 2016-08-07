
-- Triger created from your trigger

CREATE OR REPLACE TRIGGER NEXT_ORDER 
BEFORE INSERT ON "ORDER" 

for EACH ROW

BEGIN
    select order_id_seq.nextval
    into :new."OrderID"
    from dual;
END;

-- Trigger created to check number of items available before a new order is inserted. Not compiling right now :(

CREATE OR REPLACE TRIGGER AVAILABLE_QUANTITY
BEFORE INSERT ON "ORDER" 

DECLARE

    available number(3,0);
    nquantity number(3,0);
    notenough exception;

BEGIN
-- get available quantity--
    SELECT "Quantity" := available
        FROM INVENTORY
        WHERE INVENTORY."ItemSKU" = :new."ItemSKU";

--Query to get the quantity of the new item--
    SELECT "Quantity"*:new.quantity := nquantity
        FROM "ItemSKU"
        WHERE "ItemSKU" = :new."ItemSKU";

    IF nquantity > available
        RAISE notenough;
    END IF;

EXCEPTION 
    when notenough then
    raise_application_error(-2001, "not enough items avaible to purchase!");
END;
/

-- Query to add new order. It shows a foreing key problem

 UPDATE "ORDER"
   SET "Date" = '&Date',
   "ORDER"."CustomerID" = &CustomeerID, 
   "ORDER"."ItemSKU" = &ItemSKU,
   "ORDER"."Quantity" = &Quantity, 
   "ORDER"."EmployeeID" = &Employee_ID; 
