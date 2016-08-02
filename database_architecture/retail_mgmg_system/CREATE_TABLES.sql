CREATE TABLE "EMPLOYEE" (
  "EmployeeID" varchar2(9) primary key,
  "FirstName" varchar2(25),
  "LastName" varchar2(25),
  "SSN" varchar2(11)
);

CREATE TABLE "ORDER" (
  "OrderID" varchar2(6) primary key,
  "Date" date,
  "Quantity" number(3),
  "ItemSKU" varchar2(11),
  "CustomerID" varchar2(6),
  "EmployeeID" varchar2(9),
  foreign key ("ItemSKU") references ITEM("ItemSKU"),
  foreign key ("CustomerID") references CUSTOMER("CustomerID"),
  foreign key ("EmployeeID") references EMPLOYEE("EmployeeID")
);

CREATE TABLE "CUSTOMER" (
  "CustomerID" varchar2(6) primary key,
  "FirstName" varchar2(25),
  "LastName" varchar2(25),
  "Address" varchar2(60),
  "City" varchar2(25),
  "ZipCode" varchar2(13),
  "TelephoneNumber" varchar2(17)
);

CREATE TABLE "ITEM" (
  "ItemSKU" varchar2(11) primary key,
  "ItemName" varchar2(40),
  "Size" varchar2(25),
  "Color" varchar2(25)
);

CREATE TABLE "INVENTORY" (
  "ItemSKU" varchar2(11),
  "Location" varchar2(40)
  "Quantity" number(3),
  primary key("ItemSKU", "Location"),
  foreign key ("ItemSKU") references ITEM("ItemSKU")
);

CREATE TABLE "PURCHASE" (
  "PurchaseID" varchar2(25) primary key,
  "VendorID" varchar2(25),
  "ItemSKU" varchar2(11),
  "PurchaseDate" date,
  "PurchaseReceive" date
  "Available" number(3),
  foreign key ("ItemSKU") references ITEM("ItemSKU"),
  foreign key ("VendorID") references VENDOR("VendorID")
);

CREATE TABLE "VENDOR" (
  "VendorID" varchar2(6) primary key,
  "FirstName" varchar2(25),
  "LastName" varchar2(25),
  "Address" varchar2(60),
  "City" varchar2(25),
  "ZipCode" varchar2(13),
  "TelephoneNumber" varchar2(17)
);
