CREATE TABLE "EMPLOYEE" (
  "EmployeeID" number primary key,
  "FirstName" varchar2(25),
  "LastName" varchar2(25),
  "SSN" varchar2(11)
);
create sequence employee_id_seq start with 1 increment by 1;
create trigger trg_employee_id
  before insert on EMPLOYEE
  for each row
    begin
          select employee_id_seq.nextval
          into :new."EmployeeID"
          from dual;
    end;
/

CREATE TABLE "CUSTOMER" (
  "CustomerID" number primary key,
  "FirstName" varchar2(25),
  "LastName" varchar2(25),
  "Address" varchar2(60),
  "City" varchar2(40),
  "ZipCode" varchar2(14),
  "TelephoneNumber" varchar2(17)
);
CREATE sequence customer_id_seq start with 1 increment by 1;
CREATE trigger trg_customer_id
  before insert on CUSTOMER
  for each row
    begin
          select customer_id_seq.nextval
          into :new."CustomerID"
          from dual;
    end;
/

CREATE TABLE "VENDOR" (
  "VendorID" number primary key,
  "FirstName" varchar2(25),
  "LastName" varchar2(25),
  "Address" varchar2(60),
  "City" varchar2(25),
  "ZipCode" varchar2(14),
  "TelephoneNumber" varchar2(17)
);
CREATE sequence vendor_id_seq start with 1 increment by 1;
CREATE trigger trg_vendor_id
  before insert on VENDOR
  for each row
    begin
          select vendor_id_seq.nextval
          into :new."VendorID"
          from dual;
    end;
/

CREATE TABLE "ITEM" (
  "ItemSKU" varchar2(11) primary key,
  "ItemName" varchar2(40),
  "Size" varchar2(25),
  "Color" varchar2(25)
);

CREATE TABLE "INVENTORY" (
  "ItemSKU" varchar2(11) references ITEM("ItemSKU"),
  "Location" varchar2(40),
  "Quantity" number(3),
  primary key("ItemSKU", "Location")
);

CREATE TABLE "PURCHASE" (
  "PurchaseID" number primary key,
  "VendorID" number references VENDOR("VendorID"),
  "ItemSKU" varchar2(11) references ITEM("ItemSKU"),
  "PurchaseDate" date,
  "PurchaseReceive" date,
  "Available" number(3)
);
CREATE sequence purchase_id_seq start with 1 increment by 1;
CREATE trigger trg_purchase_id
  before insert on PURCHASE
  for each row
    begin
          select purchase_id_seq.nextval
          into :new."PurchaseID":
          from dual;
    end;
/

CREATE TABLE "ORDER" (
  "OrderID" number primary key,
  "Date" date,
  "Quantity" number(3),
  "ItemSKU" varchar2(11) references ITEM("ItemSKU"),
  "CustomerID" number references CUSTOMER("CustomerID"),
  "EmployeeID" number references EMPLOYEE("EmployeeID")
);
CREATE sequence order_id_seq start with 1 increment by 1;
CREATE trigger trg_order_id
  before insert on "ORDER"
  for each row
    begin
          select order_id_seq.nextval
          into :new."OrderID"
          from dual;
    end;
/
