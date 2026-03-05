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

-- Create Transactions table
CREATE TABLE Transactions (
    Transaction_ID INT PRIMARY KEY,
    Customer_ID INT,
    Product_ID INT,
    Quantity INT,
    Total_Price DECIMAL(10,2),
    Transaction_Date DATE,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product1(Product_ID)
);

-- Insert data into Transactions table
INSERT INTO Transactions VALUES
(1,1,1,2,21.98,'2023-05-24'),
(2,2,2,3,26.97,'2023-05-25'),
(3,3,3,1,5.99,'2023-05-26'),
(4,4,4,5,64.95,'2023-05-27'),
(5,5,5,2,5.98,'2023-05-28');

-- Display Transactions table
SELECT * FROM Transactions;

-- Join query to find product and available quantity
SELECT Product_Name, Available_Quantity
FROM Stock
INNER JOIN Product1
ON Stock.Product_ID = Product1.Product_ID
WHERE Product_Name = 'Rice';

-- Insert another transaction
INSERT INTO Transactions VALUES
(6,1,1,5,250,'2023-05-24');

SELECT Transaction_ID, Product_Name, Quantity, Total_Price, Transaction_Date
FROM Transactions
INNER JOIN Product1
ON Transactions.Product_ID = Product1.Product_ID
WHERE Customer_ID = 1;
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50)
);

DELIMITER //

CREATE PROCEDURE add_student (
    IN p_id INT,
    IN p_name VARCHAR(100),
    IN p_dept VARCHAR(50)
)
BEGIN
    INSERT INTO students (id, name, department)
    VALUES (p_id, p_name, p_dept);
END //

DELIMITER ;

CALL add_student(1, 'Anu', 'CSE');
INSERT INTO book_det (bid, btitle, copies)
VALUES
(101, 'Wings of Fire', 3),
(102, 'Harry Potter', 5);

INSERT INTO book_issue (bid, sid, btitle)
VALUES
(101, 1, 'Wings of Fire');



...

-- Create Employee table
CREATE TABLE Employee (
    id INT,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

-- Insert records
INSERT INTO Employee (id, name, department, salary)
VALUES
(1, 'Alice', 'HR', 30000),
(2, 'Bob', 'IT', 40000),
(3, 'Carol', 'HR', 35000),
(4, 'David', 'Finance', 45000);

-- Create View
CREATE VIEW HR_Employees AS
SELECT id, name, salary
FROM Employee
WHERE department = 'HR';

-- Display view
SELECT * FROM HR_Employees;

-- Modify the view
CREATE OR REPLACE VIEW HR_Employees AS
SELECT id, name, department, salary
FROM Employee
WHERE department = 'HR';

-- Drop the view
DROP VIEW HR_Employees;
