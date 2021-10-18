--Insert data to Customers table
INSERT INTO Customers (id, name, city, country)
VALUES(001, 'Benyamin', 'mashhad', 'IR')
INSERT INTO Customers (id, name, city, country)
VALUES(002, 'bob', 'newyork', 'USA')

--Insert data to Products table
INSERT INTO Products (id, name, price, count)
VALUES(001, 'glue', 1000, 380)
INSERT INTO Products (id, name, price, count)
VALUES(002, 'cable', 55000, 610)

--Select available products
SELECT * FROM Products WHERE count!=0

--Delete foreign customers
DELETE FROM Customers WHERE country!='IR'

--Update price of all goods
UPDATE Products
SET price = price*80/100
WHERE count!=0
