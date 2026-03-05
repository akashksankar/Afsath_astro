-- Create Customer table
CREATE TABLE customer (
    Customer_ID INT PRIMARY KEY,
    Name VARCHAR(20),
    Address VARCHAR(50),
    Contact_Number VARCHAR(15)
);

-- Insert data into Customer table
INSERT INTO customer VALUES
(1, 'John', '123 Main Street', '123-456-7890'),
(2, 'Jane', '456 Elm Street', '987-654-3210'),
(3, 'Michael', '789 Oak Avenue', '555-123-4567'),
(4, 'Emily', '321 Pine Road', '222-333-4444'),
(5, 'Sarah', '567 Maple Lane', '777-888-9999');

-- Display Customer table
SELECT * FROM customer;


-- Create Product table
CREATE TABLE Product1 (
    Product_ID INT PRIMARY KEY,
    Product_Name VARCHAR(20),
    Quantity_Per_Unit INT,
    Unit_Price DECIMAL(10,2)
);

-- Insert data into Product table
INSERT INTO Product1 VALUES
(1, 'Rice', 1, 10.99),
(2, 'Wheat Flour', 1, 8.99),
(3, 'Sugar', 1, 5.99),
(4, 'Oil', 1, 12.99),
(5, 'Grains', 1, 2.99);

-- Display Product table
SELECT * FROM Product1;


-- Create Stock table
CREATE TABLE Stock (
    Stock_ID INT PRIMARY KEY,
    Product_ID INT,
    Available_Quantity INT,
    FOREIGN KEY (Product_ID) REFERENCES Product1(Product_ID)
);

-- Insert data into Stock table
INSERT INTO Stock VALUES
(1,1,100),
(2,2,50),
(3,3,200),
(4,4,80),
(5,5,150);

-- Display Stock table
SELECT * FROM Stock;
