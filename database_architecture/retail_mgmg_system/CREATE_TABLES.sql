CREATE TABLE "EMPLOYEE" (
  "EmployeeID" number primary key,
  "FirstName" varchar2(25),
  "LastName" varchar2(25),
  "SSN" varchar2(11)
);

CREATE TABLE "CUSTOMER" (
  "CustomerID" number primary key,
  "FirstName" varchar2(25),
  "LastName" varchar2(25),
  "Address" varchar2(60),
  "City" varchar2(40),
  "ZipCode" varchar2(14),
  "TelephoneNumber" varchar2(17)
);

CREATE TABLE "VENDOR" (
  "VendorID" number primary key,
  "FirstName" varchar2(25),
  "LastName" varchar2(25),
  "Address" varchar2(60),
  "City" varchar2(25),
  "ZipCode" varchar2(14),
  "TelephoneNumber" varchar2(17)
);

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

CREATE TABLE "ORDER" (
  "OrderID" number primary key,
  "Date" date,
  "Quantity" number(3),
  "ItemSKU" varchar2(11) references ITEM("ItemSKU"),
  "CustomerID" number references CUSTOMER("CustomerID"),
  "EmployeeID" number references EMPLOYEE("EmployeeID")
);
