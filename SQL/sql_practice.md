# SQL Practice Exercises

Practice your SQL skills with these exercises. Sample data and schema are provided.

---

## Sample Tables

```sql
-- Create tables
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location VARCHAR(50)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    salary DECIMAL(10,2),
    hire_date DATE,
    department_id INT,
    manager_id INT
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock_quantity INT
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    status VARCHAR(20)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2)
);

-- Sample Data
INSERT INTO departments VALUES
(10, 'Engineering', 'New York'),
(20, 'Sales', 'Chicago'),
(30, 'Marketing', 'Los Angeles'),
(40, 'HR', 'Boston');

INSERT INTO employees VALUES
(1, 'John', 'Doe', 'john.doe@company.com', 85000, '2020-01-15', 10, NULL),
(2, 'Jane', 'Smith', 'jane.smith@company.com', 75000, '2021-03-20', 10, 1),
(3, 'Bob', 'Johnson', 'bob.johnson@company.com', 65000, '2019-07-10', 20, NULL),
(4, 'Alice', 'Williams', 'alice.williams@company.com', 70000, '2022-02-14', 20, 3),
(5, 'Charlie', 'Brown', 'charlie.brown@company.com', 55000, '2023-06-01', 30, NULL),
(6, 'Diana', 'Miller', 'diana.miller@company.com', 90000, '2018-11-05', 10, 1),
(7, 'Eve', 'Davis', 'eve.davis@company.com', 62000, '2021-09-15', 30, 5),
(8, 'Frank', 'Garcia', 'frank.garcia@company.com', 58000, '2022-04-22', 40, NULL);

INSERT INTO products VALUES
(1, 'Laptop', 'Electronics', 999.99, 50),
(2, 'Mouse', 'Electronics', 29.99, 200),
(3, 'Keyboard', 'Electronics', 79.99, 150),
(4, 'Desk', 'Furniture', 299.99, 30),
(5, 'Chair', 'Furniture', 199.99, 40),
(6, 'Monitor', 'Electronics', 349.99, 75);

INSERT INTO orders VALUES
(1, 101, '2024-01-15', 1099.98, 'Completed'),
(2, 102, '2024-01-20', 229.98, 'Completed'),
(3, 101, '2024-02-10', 79.99, 'Pending'),
(4, 103, '2024-02-15', 549.98, 'Completed'),
(5, 102, '2024-03-01', 399.99, 'Shipped');

INSERT INTO order_items VALUES
(1, 1, 1, 1, 999.99),
(2, 1, 2, 2, 29.99),
(3, 2, 3, 1, 79.99),
(4, 2, 2, 3, 29.99),
(5, 4, 1, 1, 999.99),
(6, 5, 5, 2, 199.99);
```

---

## Exercise Set 1: Basic Queries

1. Select all columns from the employees table.
2. Select only first_name, last_name, and salary from employees.
3. Get all distinct department_id values from employees.
4. Select employees with salary greater than 60000.
5. Find employees in department 10 or 20.
6. Find employees hired after January 1, 2022.
7. Find employees with salary between 50000 and 80000.
8. Select employees sorted by salary in descending order.
9. Find employees whose last_name starts with 'S'.
10. Find employees who don't have a manager.
11. Select top 3 highest paid employees.

---

## Exercise Set 2: Joins

1. Get employee names with their department names.
2. Get all employees and their department names, including those without departments.
3. Find employees who earn more than their manager.
4. Find departments with no employees.
5. Find total amount spent by each customer.
6. Get order details with product information.
7. Find products that have never been ordered.

---

## Exercise Set 3: Aggregate Functions

1. Count the total number of employees.
2. Find the average salary of all employees.
3. Find the highest and lowest salary.
4. Count employees in each department.
5. Find average salary per department, only for departments with more than 1 employee.
6. Find the total salary expense per department.
7. Find the most expensive product in each category.
8. Count employees by salary ranges (less than 60000, 60000-80000, above 80000).

---

## Exercise Set 4: Subqueries & CTEs

1. Find employees whose salary is above the average salary.
2. Find the department with the highest average salary.
3. Find employees who are in the same department as 'Jane Smith'.
4. Find the second highest salary in the company.
5. Find products that have never been ordered.
6. Find the first hired employee in each department.
7. Find employees with above-average salary in their department.

---

## Exercise Set 5: Window Functions

1. Add a row number to each employee ordered by salary descending.
2. Rank employees by salary within their department.
3. Calculate the running total of salaries ordered by hire_date.
4. Compare each employee's salary to the department average.
5. Get the previous employee's salary ordered by hire_date.
6. Find the top 2 highest paid employees in each department.
7. Calculate the difference between current and previous order amount.

---

## Exercise Set 6: DDL Operations

1. Create a customers table with customer_id, name, email, phone, city.
2. Add a new column 'bonus' to the employees table.
3. Remove the 'bonus' column from employees.
4. Add a CHECK constraint to ensure salary is positive.
5. Rename the employees table to staff.
6. Create an index on the email column.
7. Drop the customers table.

---

## Exercise Set 7: DML Operations

1. Insert a new employee into the employees table.
2. Insert multiple employees at once.
3. Update the salary of employee with ID 1 to 90000.
4. Give all employees in department 10 a 10% raise.
5. Delete employee with ID 9.
6. Delete all employees with salary less than 50000.

---

## Exercise Set 8: Advanced Queries

1. Find the percentage of total salary each department contributes.
2. Find the second highest salary in the company.
3. Generate a report showing month-over-month revenue growth.
4. Find cumulative distribution of salaries.
5. Create a report showing employee name, department, manager, salary, and difference from department average.
6. Find all orders with more than 2 items.
7. Identify employees with the same hire_date.

---

## Exercise Set 9: String & Date Functions

1. Extract the domain from email addresses.
2. Get the year, month, and day from hire_date.
3. Find employees hired in the last 6 months.
4. Concatenate first_name and last_name as full_name.
5. Find employees hired in 2022 or 2023.
6. Format salary as currency format.

---

## Exercise Set 10: Set Operations

1. Find common department_ids between employees and departments.
2. Find department_ids in departments but not in employees.
3. Combine names from employees and customers tables.

---

## Challenge Questions

**Challenge 1:** Create a comprehensive employee report showing:
- Employee full name
- Department name
- Manager name
- Salary
- Department average salary
- Percentage of department total

**Challenge 2:** Create a sales analysis report showing:
- Monthly revenue
- Month-over-month growth percentage
- Top 3 products by revenue
- Percentage of total revenue per product

**Challenge 3:** Find all employee pairs in the same department (excluding self-matches).

**Challenge 4:** Build an organizational hierarchy tree using recursive CTE.
