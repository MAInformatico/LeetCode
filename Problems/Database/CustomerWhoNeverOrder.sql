SELECT Name AS Customers FROM Customers
where Id NOT IN (SELECT Customers.Id FROM Orders WHERE Orders.CustomerId = Customers.Id);
