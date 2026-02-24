# SQL Theory & Tutorial

## Table of Contents
1. [SQL Categories (DDL, DML, DQL)](#1-sql-categories-ddl-dml-dql)
2. [SQL Fundamentals](#2-sql-fundamentals)
3. [Joins](#3-joins)
4. [Aggregate Functions](#4-aggregate-functions)
5. [Subqueries \& CTEs](#5-subqueries--ctes)
6. [Window Functions](#6-window-functions)
7. [Advanced SQL](#7-advanced-sql)
8. [Database Design](#8-database-design)
9. [Performance \& Optimization](#9-performance--optimization)
10. [Database Specifics](#10-database-specifics)

---

## 1. SQL Categories (DDL, DML, DQL)

SQL (Structured Query Language) is categorized into different types based on their purpose. Understanding these categories is fundamental to working with databases.

### 📖 What are DDL, DML, and DQL?

**DDL (Data Definition Language)** - Commands that define database structure
- **CREATE**: Create databases, tables, indexes, views
- **ALTER**: Modify existing database objects
- **DROP**: Delete database objects
- **TRUNCATE**: Remove all data from a table
- **RENAME**: Rename database objects

**DML (Data Manipulation Language)** - Commands that manipulate data
- **INSERT**: Add new data
- **UPDATE**: Modify existing data
- **DELETE**: Remove data

**DQL (Data Query Language)** - Commands that retrieve data
- **SELECT**: Query and retrieve data

**Why is this important for Data Engineering?**
- DDL: Building and modifying data pipelines, schema design
- DML: ETL processes, data transformation
- DQL: Data analysis and reporting

---

### DDL - Data Definition Language

```sql
-- CREATE DATABASE
CREATE DATABASE company_db;
USE company_db;

-- CREATE TABLE
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10,2),
    hire_date DATE,
    department_id INT
);

-- CREATE TABLE with constraints
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE,
    total_amount DECIMAL(10,2) CHECK (total_amount >= 0),
    status VARCHAR(20) DEFAULT 'pending',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- CREATE INDEX
CREATE INDEX idx_department ON employees(department_id);
CREATE INDEX idx_salary ON employees(salary);
CREATE UNIQUE INDEX idx_email ON employees(email);

-- CREATE VIEW
CREATE VIEW v_employee_details AS
SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;

-- ALTER TABLE - Add column
ALTER TABLE employees
ADD phone_number VARCHAR(20);

-- ALTER TABLE - Modify column
ALTER TABLE employees
MODIFY COLUMN salary DECIMAL(12,2);

-- ALTER TABLE - Drop column
ALTER TABLE employees
DROP COLUMN phone_number;

-- ALTER TABLE - Add constraint
ALTER TABLE employees
ADD CONSTRAINT chk_salary CHECK (salary > 0);

-- ALTER TABLE - Rename
ALTER TABLE employees
RENAME TO staff;

-- TRUNCATE TABLE (remove all data, keep structure)
TRUNCATE TABLE employees;

-- DROP TABLE (delete table completely)
DROP TABLE employees;

-- DROP DATABASE
DROP DATABASE company_db;

-- RENAME TABLE
RENAME TABLE employees TO staff;
```

---

### DML - Data Manipulation Language

```sql
-- INSERT - Add new data
INSERT INTO employees (employee_id, first_name, last_name, email, salary, department_id)
VALUES (1, 'John', 'Doe', 'john.doe@company.com', 75000, 10);

-- INSERT multiple rows
INSERT INTO employees (employee_id, first_name, last_name, email, salary, department_id)
VALUES
    (2, 'Jane', 'Smith', 'jane.smith@company.com', 65000, 20),
    (3, 'Bob', 'Johnson', 'bob.johnson@company.com', 60000, 10),
    (4, 'Alice', 'Williams', 'alice.williams@company.com', 80000, 30);

-- INSERT from SELECT
INSERT INTO high_earners
SELECT * FROM employees
WHERE salary > 70000;

-- UPDATE - Modify existing data
UPDATE employees
SET salary = 80000
WHERE employee_id = 1;

-- UPDATE multiple columns
UPDATE employees
SET department_id = 20,
    salary = salary * 1.1
WHERE employee_id = 2;

-- UPDATE with calculations
UPDATE products
SET price = price * 0.9
WHERE category = 'Electronics';

-- DELETE - Remove data
DELETE FROM employees
WHERE employee_id = 1;

-- DELETE with subquery
DELETE FROM orders
WHERE customer_id IN (
    SELECT customer_id
    FROM customers
    WHERE status = 'inactive'
);

-- DELETE all rows
DELETE FROM temp_data;

-- MERGE (upsert - insert or update)
MERGE INTO target_table t
USING source_table s
ON t.id = s.id
WHEN MATCHED THEN
    UPDATE SET t.value = s.value
WHEN NOT MATCHED THEN
    INSERT (id, value)
    VALUES (s.id, s.value);
```

---

### DQL - Data Query Language

```sql
-- SELECT - Retrieve data
SELECT * FROM employees;

-- SELECT specific columns
SELECT first_name, last_name, salary FROM employees;

-- WHERE clause
SELECT * FROM employees
WHERE department_id = 10 AND salary > 60000;

-- ORDER BY
SELECT * FROM employees
ORDER BY salary DESC;

-- DISTINCT
SELECT DISTINCT department_id FROM employees;

-- LIMIT / TOP
SELECT * FROM employees LIMIT 10;
SELECT TOP 10 * FROM employees;  -- SQL Server

-- Aliases
SELECT
    first_name AS "First Name",
    last_name AS "Last Name",
    salary * 12 AS "Annual Salary"
FROM employees;

-- Aggregate queries
SELECT
    department_id,
    COUNT(*) as employee_count,
    AVG(salary) as avg_salary,
    SUM(salary) as total_salary
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;
```

---

### SQL Commands Quick Reference

| Category | Command | Purpose |
|----------|---------|---------|
| **DDL** | CREATE | Create database objects |
| **DDL** | ALTER | Modify database objects |
| **DDL** | DROP | Delete database objects |
| **DDL** | TRUNCATE | Remove all data from table |
| **DML** | INSERT | Add new data |
| **DML** | UPDATE | Modify existing data |
| **DML** | DELETE | Remove data |
| **DQL** | SELECT | Retrieve data |

---

## 2. SQL Fundamentals

### 📖 What are SQL Fundamentals?

**SQL (Structured Query Language)** is a standard language used to manage and manipulate relational databases. SQL Fundamentals cover the basic operations for retrieving, inserting, updating, and deleting data in database tables. These operations form the building blocks for all database interactions.

**Key Concepts:**
- **SELECT**: Retrieve data from one or more tables
- **INSERT**: Add new rows to a table
- **UPDATE**: Modify existing data in a table
- **DELETE**: Remove rows from a table
- **WHERE**: Filter rows based on conditions
- **ORDER BY**: Sort results
- **GROUP BY**: Group rows for aggregate operations
- **Aliases**: Rename columns or tables for readability

**Why is this important for Data Engineering?**
- Retrieving data from data warehouses
- Loading and transforming data in ETL pipelines
- Data cleaning and preprocessing
- Building analytical queries for reporting

### SELECT Statement

```sql
-- Basic SELECT
SELECT * FROM employees;

-- Select specific columns
SELECT first_name, last_name, salary FROM employees;

-- WHERE clause with conditions
SELECT * FROM employees
WHERE department = 'Engineering' AND salary > 50000;

-- ORDER BY (sorting)
SELECT * FROM employees
ORDER BY salary DESC;

-- DISTINCT (remove duplicates)
SELECT DISTINCT department FROM employees;

-- LIMIT and OFFSET (pagination)
SELECT * FROM employees
LIMIT 10 OFFSET 20;  -- Skip first 20, get next 10

-- Column aliases
SELECT
    first_name AS "First Name",
    last_name AS "Last Name",
    salary * 12 AS "Annual Salary"
FROM employees;
```

### INSERT Statement

```sql
-- Insert single row
INSERT INTO employees (first_name, last_name, department, salary)
VALUES ('John', 'Doe', 'Engineering', 75000);

-- Insert multiple rows
INSERT INTO employees (first_name, last_name, department, salary)
VALUES
    ('Jane', 'Smith', 'Marketing', 65000),
    ('Bob', 'Johnson', 'Sales', 60000),
    ('Alice', 'Williams', 'Engineering', 80000);

-- Insert from SELECT
INSERT INTO employees_archive
SELECT * FROM employees
WHERE hire_date < '2020-01-01';
```

### UPDATE Statement

```sql
-- Update single column
UPDATE employees
SET salary = 75000
WHERE employee_id = 100;

-- Update multiple columns
UPDATE employees
SET department = 'Senior Engineering',
    salary = salary * 1.1
WHERE employee_id = 100;

-- Update with calculation
UPDATE products
SET price = price * 0.9
WHERE category = 'Electronics';
```

### DELETE Statement

```sql
-- Delete with condition
DELETE FROM employees
WHERE employee_id = 100;

-- Delete all rows (use with caution!)
DELETE FROM temp_table;

-- Delete based on another table
DELETE FROM orders
WHERE customer_id IN (
    SELECT customer_id
    FROM customers
    WHERE status = 'inactive'
);
```

### WHERE Clause & Operators

```sql
-- Comparison operators
SELECT * FROM employees WHERE salary = 50000;
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE salary < 50000;
SELECT * FROM employees WHERE salary >= 50000;
SELECT * FROM employees WHERE salary <= 50000;
SELECT * FROM employees WHERE salary != 50000;
SELECT * FROM employees WHERE salary <> 50000;

-- Logical operators
SELECT * FROM employees
WHERE department = 'Engineering' AND salary > 60000;

SELECT * FROM employees
WHERE department = 'Engineering' OR department = 'Sales';

SELECT * FROM employees
WHERE NOT department = 'HR';

-- IN operator
SELECT * FROM employees
WHERE department IN ('Engineering', 'Sales', 'Marketing');

-- BETWEEN operator
SELECT * FROM employees
WHERE salary BETWEEN 50000 AND 80000;

-- LIKE operator (pattern matching)
SELECT * FROM employees
WHERE first_name LIKE 'J%';  -- Starts with J

SELECT * FROM employees
WHERE email LIKE '%@gmail.com';  -- Ends with gmail

SELECT * FROM employees
WHERE last_name LIKE '_mith';  -- 5 letters ending in mith

-- IS NULL / IS NOT NULL
SELECT * FROM employees
WHERE manager_id IS NOT NULL;

-- EXISTS subquery
SELECT * FROM departments d
WHERE EXISTS (
    SELECT 1 FROM employees e
    WHERE e.department_id = d.id
);
```

### ORDER BY, GROUP BY, HAVING

```sql
-- ORDER BY - Sorting
SELECT * FROM employees
ORDER BY salary DESC;

-- Multiple columns sorting
SELECT * FROM employees
ORDER BY department ASC, salary DESC;

-- GROUP BY - Grouping
SELECT department, COUNT(*) as employee_count
FROM employees
GROUP BY department;

-- GROUP BY with multiple columns
SELECT department, job_title, COUNT(*) as count
FROM employees
GROUP BY department, job_title;

-- HAVING - Filter after grouping
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;

-- ORDER BY with aggregate
SELECT department, COUNT(*) as count
FROM employees
GROUP BY department
ORDER BY count DESC;
```

---

## 2. Joins

### 📖 What are Joins?

**Joins** are SQL operations that combine rows from two or more tables based on a related column. They allow you to retrieve data that spans multiple tables in a relational database. Understanding different types of joins is essential for working with normalized databases where data is distributed across tables.

**Key Concepts:**
- **INNER JOIN**: Returns rows with matches in both tables
- **LEFT JOIN**: Returns all rows from left table and matched rows from right
- **RIGHT JOIN**: Returns all rows from right table and matched rows from left
- **FULL OUTER JOIN**: Returns all rows when there's a match in either table
- **CROSS JOIN**: Returns Cartesian product of both tables
- **SELF JOIN**: Joins a table to itself

**Why is this important for Data Engineering?**
- Combining data from multiple source tables
- Building denormalized views for analytics
- Data warehouse dimension modeling
- ETL transformations involving multiple tables

### INNER JOIN

```sql
-- Basic INNER JOIN
SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    d.department_name
FROM employees e
INNER JOIN departments d
    ON e.department_id = d.department_id;

-- INNER JOIN with multiple conditions
SELECT
    o.order_id,
    o.order_date,
    c.customer_name,
    p.product_name
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;
```

### LEFT JOIN / RIGHT JOIN

```sql
-- LEFT JOIN - All from left + matched from right
SELECT
    e.employee_id,
    e.first_name,
    d.department_name
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.department_id;

-- RIGHT JOIN - All from right + matched from left
SELECT
    e.employee_id,
    e.first_name,
    d.department_name
FROM employees e
RIGHT JOIN departments d
    ON e.department_id = d.department_id;

-- Find employees without departments
SELECT e.employee_id, e.first_name
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.department_id
WHERE d.department_id IS NULL;
```

### FULL OUTER JOIN

```sql
-- FULL OUTER JOIN - All rows from both tables
SELECT
    e.employee_id,
    e.first_name,
    d.department_name
FROM employees e
FULL OUTER JOIN departments d
    ON e.department_id = d.department_id;

-- Find unmatched records from both tables
SELECT
    e.employee_id,
    e.first_name,
    d.department_id,
    d.department_name
FROM employees e
FULL OUTER JOIN departments d
    ON e.department_id = d.department_id
WHERE e.employee_id IS NULL OR d.department_id IS NULL;
```

### CROSS JOIN

```sql
-- CROSS JOIN - Cartesian product
SELECT
    e.first_name,
    p.project_name
FROM employees e
CROSS JOIN projects p;

-- Practical example: Generate all combinations
SELECT
    s.size_name,
    c.color_name
FROM sizes s
CROSS JOIN colors c;
```

### SELF JOIN

```sql
-- SELF JOIN - Join table to itself
SELECT
    e.first_name AS "Employee",
    m.first_name AS "Manager"
FROM employees e
INNER JOIN employees m
    ON e.manager_id = m.employee_id;

-- Employees without managers
SELECT e.first_name AS "Employee"
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.employee_id
WHERE m.employee_id IS NULL;
```

### Multiple Table Joins

```sql
-- Joining multiple tables
SELECT
    o.order_id,
    c.customer_name,
    e.first_name AS "Sales Rep",
    p.product_name,
    oi.quantity,
    oi.unit_price
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN employees e ON o.sales_rep_id = e.employee_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
WHERE o.order_date >= '2024-01-01';
```

---

## 3. Aggregate Functions

### 📖 What are Aggregate Functions?

**Aggregate Functions** perform calculations on sets of rows and return a single result. They are commonly used with GROUP BY to analyze data in groups. Aggregate functions ignore NULL values (except COUNT(*)).

**Key Concepts:**
- **COUNT**: Counts rows or non-null values
- **SUM**: Adds all values
- **AVG**: Calculates average
- **MIN**: Returns minimum value
- **MAX**: Returns maximum value
- **GROUP BY**: Groups rows for aggregate calculations
- **HAVING**: Filters groups after aggregation

**Why is this important for Data Engineering?**
- Calculating KPIs and metrics
- Data summarization and reporting
- Building analytics queries
- Data quality checks

### COUNT, SUM, AVG, MIN, MAX

```sql
-- COUNT
SELECT COUNT(*) FROM employees;  -- Total rows
SELECT COUNT(manager_id) FROM employees;  -- Non-null values
SELECT COUNT(DISTINCT department) FROM employees;  -- Unique values

-- SUM
SELECT SUM(salary) FROM employees;
SELECT SUM(salary) FROM employees WHERE department = 'Engineering';

-- AVG
SELECT AVG(salary) FROM employees;
SELECT AVG(DISTINCT salary) FROM employees;

-- MIN and MAX
SELECT MIN(hire_date) FROM employees;
SELECT MAX(salary) FROM employees;

-- Multiple aggregates
SELECT
    COUNT(*) as total_employees,
    SUM(salary) as total_salary,
    AVG(salary) as avg_salary,
    MIN(salary) as min_salary,
    MAX(salary) as max_salary
FROM employees;
```

### GROUP BY with Aggregates

```sql
-- Basic GROUP BY
SELECT
    department,
    COUNT(*) as employee_count,
    AVG(salary) as avg_salary
FROM employees
GROUP BY department;

-- GROUP BY with multiple columns
SELECT
    department,
    job_title,
    COUNT(*) as count,
    AVG(salary) as avg_salary
FROM employees
GROUP BY department, job_title;

-- Using ROUND with aggregates
SELECT
    department,
    ROUND(AVG(salary), 2) as avg_salary
FROM employees
GROUP BY department;

-- Filter groups with HAVING
SELECT
    department,
    COUNT(*) as count,
    SUM(salary) as total_salary
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

### HAVING vs WHERE

```sql
-- WHERE - Filters rows BEFORE grouping
SELECT department, AVG(salary) as avg_sal
FROM employees
WHERE department != 'HR'
GROUP BY department;

-- HAVING - Filters groups AFTER grouping
SELECT department, AVG(salary) as avg_sal
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;

-- Combining WHERE and HAVING
SELECT department, AVG(salary) as avg_sal
FROM employees
WHERE hire_date >= '2020-01-01'  -- Filter rows first
GROUP BY department
HAVING AVG(salary) > 50000;      -- Then filter groups
```

---

## 4. Subqueries & CTEs

### 📖 What are Subqueries & CTEs?

**Subqueries** are queries nested inside other queries. They can be used in SELECT, FROM, or WHERE clauses. **Common Table Expressions (CTEs)** are temporary named result sets that exist only for the duration of a single query. Both are used to break down complex queries into manageable parts.

**Key Concepts:**
- **Scalar Subquery**: Returns single value
- **Correlated Subquery**: References outer query
- **CTE (Common Table Expression)**: Named temporary result set
- **Recursive CTE**: CTE that references itself
- **Subquery in FROM**: Creates inline view

**Why is this important for Data Engineering?**
- Complex data transformations
- Building reusable logic in ETL pipelines
- Hierarchical data processing
- Analytical queries

### Scalar Subqueries

```sql
-- Scalar subquery in SELECT
SELECT
    first_name,
    salary,
    (SELECT AVG(salary) FROM employees) as avg_salary
FROM employees;

-- Scalar subquery in WHERE
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Scalar subquery in ORDER BY
SELECT * FROM employees
ORDER BY (SELECT salary FROM employees WHERE employee_id = 100) DESC;
```

### Correlated Subqueries

```sql
-- Correlated subquery - references outer query
SELECT e.first_name, e.salary, e.department_id
FROM employees e
WHERE e.salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = e.department_id
);

-- Find employees with above-average salary in their department
SELECT
    e.first_name,
    e.salary,
    e.department_id,
    (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id) as dept_avg
FROM employees e;

-- EXISTS with correlated subquery
SELECT d.department_name
FROM departments d
WHERE EXISTS (
    SELECT 1 FROM employees e WHERE e.department_id = d.department_id
);
```

### Common Table Expressions (CTEs)

```sql
-- Basic CTE
WITH dept_salary AS (
    SELECT
        department_id,
        AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT
    e.first_name,
    e.salary,
    d.avg_salary
FROM employees e
JOIN dept_salary d ON e.department_id = d.department_id
WHERE e.salary > d.avg_salary;

-- Multiple CTEs
WITH
    active_employees AS (
        SELECT * FROM employees WHERE status = 'active'
    ),
    high_earners AS (
        SELECT * FROM active_employees WHERE salary > 70000
    )
SELECT * FROM high_earners;

-- CTE with aggregation
WITH monthly_sales AS (
    SELECT
        DATE_TRUNC('month', order_date) as month,
        SUM(total_amount) as revenue
    FROM orders
    WHERE order_date >= '2024-01-01'
    GROUP BY DATE_TRUNC('month', order_date)
)
SELECT
    month,
    revenue,
    revenue - LAG(revenue) OVER (ORDER BY month) as growth
FROM monthly_sales;
```

### Recursive CTEs

```sql
-- Recursive CTE for hierarchy
WITH RECURSIVE org_chart AS (
    -- Base case: top-level managers
    SELECT
        employee_id,
        first_name,
        manager_id,
        1 as level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive case: employees with managers
    SELECT
        e.employee_id,
        e.first_name,
        e.manager_id,
        o.level + 1
    FROM employees e
    JOIN org_chart o ON e.manager_id = o.employee_id
)
SELECT * FROM org_chart;

-- Recursive CTE for number sequence
WITH RECURSIVE numbers AS (
    SELECT 1 as n

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 10
)
SELECT * FROM numbers;

-- Recursive CTE for tree structure
WITH RECURSIVE category_tree AS (
    SELECT
        category_id,
        category_name,
        parent_id,
        0 as level,
        CAST(category_name AS VARCHAR(500)) as path
    FROM categories
    WHERE parent_id IS NULL

    UNION ALL

    SELECT
        c.category_id,
        c.category_name,
        c.parent_id,
        ct.level + 1,
        ct.path || ' > ' || c.category_name
    FROM categories c
    JOIN category_tree ct ON c.parent_id = ct.category_id
)
SELECT * FROM category_tree;
```

### Subquery in FROM, WHERE, SELECT

```sql
-- Subquery in FROM (inline view)
SELECT
    dept_name,
    employee_count
FROM (
    SELECT
        d.department_name as dept_name,
        COUNT(e.employee_id) as employee_count
    FROM departments d
    LEFT JOIN employees e ON d.department_id = e.department_id
    GROUP BY d.department_name
) subquery
WHERE employee_count > 5;

-- Subquery in WHERE
SELECT * FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE location = 'New York'
);

-- Subquery in SELECT with JOIN
SELECT
    e.first_name,
    e.salary,
    d.avg_salary
FROM employees e
JOIN (
    SELECT department_id, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
) d ON e.department_id = d.department_id;
```

---

## 5. Window Functions

### 📖 What are Window Functions?

**Window Functions** perform calculations across a set of rows related to the current row. Unlike aggregate functions, window functions don't group rows - each row retains its identity while gaining access to aggregated data from other rows. The "window" is the set of rows the function operates on.

**Key Concepts:**
- **OVER()**: Defines the window for the function
- **PARTITION BY**: Divides rows into groups (like GROUP BY but keeps rows)
- **ORDER BY**: Orders rows within the window
- **ROW_NUMBER()**: Assigns unique sequential numbers
- **RANK()**: Assigns ranks with gaps
- **DENSE_RANK()**: Assigns ranks without gaps
- **LEAD/LAG**: Access subsequent/previous rows

**Why is this important for Data Engineering?**
- Running totals and moving averages
- Ranking and percentiles
- Identifying trends over time
- Top N per group problems

### ROW_NUMBER(), RANK(), DENSE_RANK()

```sql
-- ROW_NUMBER() - Sequential number regardless of ties
SELECT
    first_name,
    salary,
    department_id,
    ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num
FROM employees;

-- RANK() - Same rank for ties, with gaps
SELECT
    first_name,
    salary,
    department_id,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as rank
FROM employees;

-- DENSE_RANK() - Same rank for ties, without gaps
SELECT
    first_name,
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank
FROM employees;

-- Top 3 earners per department
SELECT * FROM (
    SELECT
        first_name,
        salary,
        department_id,
        ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) as row_num
    FROM employees
) ranked
WHERE row_num <= 3;
```

### LEAD(), LAG()

```sql
-- LAG() - Previous row value
SELECT
    order_date,
    total_amount,
    LAG(total_amount, 1) OVER (ORDER BY order_date) as prev_day_amount,
    total_amount - LAG(total_amount, 1) OVER (ORDER BY order_date) as growth
FROM daily_sales;

-- LEAD() - Next row value
SELECT
    first_name,
    hire_date,
    LEAD(hire_date, 1) OVER (ORDER BY hire_date) as next_hire_date
FROM employees;

-- LAG with partition
SELECT
    department_id,
    salary,
    LAG(salary, 1) OVER (PARTITION BY department_id ORDER BY salary DESC) as prev_salary
FROM employees;

-- Compare with previous period
SELECT
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) as prev_month,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY month)) / LAG(revenue) OVER (ORDER BY month) * 100, 2) as pct_growth
FROM monthly_revenue;
```

### FIRST_VALUE(), LAST_VALUE()

```sql
-- FIRST_VALUE() - First value in window
SELECT
    first_name,
    department_id,
    salary,
    FIRST_VALUE(salary) OVER (PARTITION BY department_id ORDER BY hire_date) as first_salary
FROM employees;

-- LAST_VALUE() - Last value in window (requires frame specification)
SELECT
    first_name,
    department_id,
    hire_date,
    salary,
    LAST_VALUE(salary) OVER (
        PARTITION BY department_id
        ORDER BY hire_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) as current_salary
FROM employees;

-- NTH_VALUE() - nth value in window
SELECT
    first_name,
    salary,
    NTH_VALUE(salary, 3) OVER (ORDER BY salary DESC) as third_highest
FROM employees;
```

### SUM(), AVG() OVER()

```sql
-- Running total (cumulative sum)
SELECT
    order_date,
    daily_sales,
    SUM(daily_sales) OVER (ORDER BY order_date) as running_total
FROM daily_sales;

-- Moving average (last 3 rows)
SELECT
    order_date,
    sales,
    AVG(sales) OVER (
        ORDER BY order_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) as moving_avg_3
FROM daily_sales;

-- Running average by department
SELECT
    first_name,
    department_id,
    salary,
    AVG(salary) OVER (PARTITION BY department_id ORDER BY hire_date) as running_avg
FROM employees;

-- SUM with PARTITION
SELECT
    first_name,
    department_id,
    salary,
    SUM(salary) OVER (PARTITION BY department_id) as dept_total,
    salary / SUM(salary) OVER (PARTITION BY department_id) * 100 as pct_of_dept
FROM employees;
```

### PARTITION BY vs GROUP BY

```sql
-- GROUP BY - Reduces to single row per group
SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id;

-- PARTITION BY - Keeps all rows with group calculations
SELECT
    first_name,
    department_id,
    salary,
    AVG(salary) OVER (PARTITION BY department_id) as dept_avg,
    salary - AVG(salary) OVER (PARTITION BY department_id) as diff_from_avg
FROM employees;

-- GROUP BY with HAVING
SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 60000;

-- Equivalent with window function
SELECT * FROM (
    SELECT
        department_id,
        AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
) sub
WHERE avg_salary > 60000;
```

---

## 6. Advanced SQL

### 📖 What is Advanced SQL?

**Advanced SQL** covers sophisticated query techniques beyond basic CRUD operations. This includes conditional logic (CASE WHEN), handling NULL values, string manipulation, date operations, and set operations. These skills enable complex data transformations and analytics.

**Key Concepts:**
- **CASE WHEN**: Conditional expressions
- **COALESCE**: Return first non-null value
- **NULLIF**: Return NULL if values are equal
- **String functions**: CONCAT, SUBSTRING, TRIM, etc.
- **Date functions**: DATEADD, DATEDIFF, FORMAT
- **Set operations**: UNION, INTERSECT, EXCEPT

**Why is this important for Data Engineering?**
- Complex data transformations
- Data cleansing and standardization
- Building analytical features
- Handling edge cases in ETL

### CASE WHEN (Conditional Logic)

```sql
-- Basic CASE WHEN
SELECT
    first_name,
    salary,
    CASE
        WHEN salary < 50000 THEN 'Low'
        WHEN salary < 80000 THEN 'Medium'
        ELSE 'High'
    END as salary_bracket
FROM employees;

-- CASE in ORDER BY
SELECT * FROM employees
ORDER BY
    CASE department
        WHEN 'Engineering' THEN 1
        WHEN 'Sales' THEN 2
        ELSE 3
    END;

-- CASE with aggregates
SELECT
    CASE
        WHEN age < 30 THEN 'Young'
        WHEN age < 50 THEN 'Middle-aged'
        ELSE 'Senior'
    END as age_group,
    COUNT(*) as count
FROM customers
GROUP BY
    CASE
        WHEN age < 30 THEN 'Young'
        WHEN age < 50 THEN 'Middle-aged'
        ELSE 'Senior'
    END;

-- CASE in UPDATE
UPDATE employees
SET salary_level =
    CASE
        WHEN salary >= 100000 THEN 'L4'
        WHEN salary >= 75000 THEN 'L3'
        WHEN salary >= 50000 THEN 'L2'
        ELSE 'L1'
    END;
```

### COALESCE, NULLIF, ISNULL

```sql
-- COALESCE - Return first non-null value
SELECT COALESCE(NULL, NULL, 'Default', 'Value');  -- Returns 'Default'

-- Practical example: Replace NULL with default
SELECT
    first_name,
    COALESCE(phone, mobile, 'No phone') as contact_phone
FROM customers;

-- Use COALESCE in calculations
SELECT
    first_name,
    salary,
    commission,
    salary + COALESCE(commission, 0) as total_compensation
FROM employees;

-- NULLIF - Return NULL if values are equal
SELECT NULLIF(10, 10);   -- Returns NULL
SELECT NULLIF(10, 20);   -- Returns 10

-- Practical example: Avoid division by zero
SELECT
    product_name,
    units_sold,
    units_in_stock,
    CASE
        WHEN units_in_stock = 0 THEN NULL
        ELSE units_sold * 1.0 / units_in_stock
    END as sell_through_rate
FROM products;

-- Equivalent with NULLIF
SELECT
    product_name,
    units_sold,
    units_in_stock,
    units_sold * 1.0 / NULLIF(units_in_stock, 0) as sell_through_rate
FROM products;

-- ISNULL (SQL Server) / IFNULL (MySQL)
-- SQL Server
SELECT ISNULL(phone, 'N/A') FROM customers;
```

### String Functions

```sql
-- CONCAT / CONCAT_WS
SELECT CONCAT(first_name, ' ', last_name) as full_name FROM employees;
SELECT CONCAT_WS(', ', first_name, city, country) as location FROM customers;

-- SUBSTRING / SUBSTR
SELECT SUBSTRING('Hello World', 1, 5);    -- 'Hello'
SELECT SUBSTRING('Hello World', 7);        -- 'World'

-- TRIM / LTRIM / RTRIM
SELECT TRIM('  hello  ');   -- 'hello'
SELECT LTRIM('  hello');    -- 'hello'
SELECT RTRIM('hello  ');   -- 'hello'

-- UPPER / LOWER
SELECT UPPER('hello');  -- 'HELLO'
SELECT LOWER('HELLO');  -- 'hello'

-- LENGTH / CHAR_LENGTH
SELECT LENGTH('Hello');        -- 5 (bytes)
SELECT CHAR_LENGTH('Hello');   -- 5 (characters)

-- REPLACE
SELECT REPLACE('Hello World', 'World', 'Python');  -- 'Hello Python'

-- LEFT / RIGHT
SELECT LEFT('Hello World', 5);   -- 'Hello'
SELECT RIGHT('Hello World', 5);   -- 'World'

-- String concatenation example
SELECT
    CONCAT(
        UPPER(LEFT(first_name, 1)),
        LOWER(SUBSTRING(first_name, 2))
    ) as proper_name
FROM employees;
```

### Date Functions

```sql
-- GETDATE() / CURRENT_DATE / NOW()
SELECT GETDATE();           -- SQL Server
SELECT CURRENT_DATE;        -- PostgreSQL/MySQL
SELECT NOW();               -- PostgreSQL/MySQL

-- DATEADD
SELECT DATEADD(year, 1, '2024-01-01');    -- 2025-01-01
SELECT DATEADD(month, -3, '2024-01-01'); -- 2023-10-01
SELECT DATEADD(day, 7, '2024-01-01');    -- 2024-01-08

-- DATEDIFF
SELECT DATEDIFF(year, '2020-01-01', '2024-01-01');  -- 4
SELECT DATEDIFF(month, '2024-01-01', '2024-06-01'); -- 5
SELECT DATEDIFF(day, '2024-01-01', '2024-01-10');   -- 9

-- DATEPART / EXTRACT
SELECT DATEPART(year, '2024-06-15');     -- 2024 (SQL Server)
SELECT EXTRACT(year FROM '2024-06-15');  -- 2024 (PostgreSQL/MySQL)

-- YEAR / MONTH / DAY
SELECT YEAR('2024-06-15');   -- 2024
SELECT MONTH('2024-06-15');  -- 6
SELECT DAY('2024-06-15');    -- 15

-- CAST / CONVERT for dates
SELECT CAST('2024-01-01' AS DATE);
SELECT CONVERT(DATE, '2024-01-01');

-- Date arithmetic
SELECT '2024-01-01' + INTERVAL 1 DAY;     -- PostgreSQL
SELECT DATEADD(day, 1, '2024-01-01');    -- SQL Server
```

### UNION vs UNION ALL

```sql
-- UNION - Combines results, removes duplicates
SELECT first_name FROM employees
UNION
SELECT first_name FROM contractors;

-- UNION ALL - Combines results, keeps duplicates
SELECT first_name FROM employees
UNION ALL
SELECT first_name FROM contractors;

-- UNION with different columns
SELECT 'Employee' as type, first_name FROM employees
UNION
SELECT 'Contractor', contractor_name FROM contractors;

-- Practical example: Combine data from multiple sources
SELECT order_id, order_date, total FROM online_orders
UNION
SELECT order_id, order_date, total FROM store_orders
ORDER BY order_date;

-- UNION with WHERE
SELECT product_name, price FROM products WHERE category = 'Electronics'
UNION
SELECT product_name, price FROM products WHERE category = 'Books'
ORDER BY price;
```

### INTERSECT, EXCEPT

```sql
-- INTERSECT - Common rows in both queries
SELECT customer_id FROM orders
INTERSECT
SELECT customer_id FROM returns;

-- Find customers who both ordered and returned items
SELECT DISTINCT customer_id FROM orders
WHERE customer_id IN (
    SELECT customer_id FROM returns
);

-- EXCEPT - Rows in first query but not in second
SELECT customer_id FROM orders
EXCEPT
SELECT customer_id FROM returns;

-- Find customers who ordered but never returned
SELECT DISTINCT customer_id FROM orders
WHERE customer_id NOT IN (
    SELECT customer_id FROM returns
);

-- Using EXCEPT for data validation
SELECT * FROM current_employees
EXCEPT
SELECT * FROM previous_employees;
-- Shows new employees
```

---

## 7. Database Design

### 📖 What is Database Design?

**Database Design** is the process of structuring a database to store data efficiently and maintain data integrity. It involves defining tables, relationships, constraints, indexes, and normalization rules. Well-designed databases minimize redundancy and ensure data accuracy.

**Key Concepts:**
- **Normalization**: Organizing data to reduce redundancy (1NF, 2NF, 3NF, BCNF)
- **Primary Key**: Unique identifier for each record
- **Foreign Key**: Reference to primary key in another table
- **Indexes**: Structures that improve query performance
- **Constraints**: Rules that enforce data integrity
- **Views**: Virtual tables based on queries

**Why is this important for Data Engineering?**
- Building efficient data models
- Ensuring data quality and integrity
- Optimizing query performance
- Supporting ETL and data warehousing

### Normalization (1NF, 2NF, 3NF, BCNF)

```sql
-- 1NF (First Normal Form)
-- Each column contains atomic values, no repeating groups
-- Bad: phone_numbers VARCHAR with "123-456, 789-012"
-- Good: phone_number_id, phone_number (separate rows)

-- 2NF (Second Normal Form)
-- Must be in 1NF, no partial dependencies
-- Bad: OrderItems(order_id, product_id, product_name, quantity)
-- Fix: Products(product_id, product_name), OrderItems(order_id, product_id, quantity)

-- 3NF (Third Normal Form)
-- Must be in 2NF, no transitive dependencies
-- Bad: Employees(employee_id, name, department, department_location)
-- Fix: Departments(department_id, name, location), Employees(employee_id, name, department_id)

-- BCNF (Boyce-Codd Normal Form)
-- More strict than 3NF
-- Every determinant must be a candidate key

-- Example: Normalized schema
-- Customers(customer_id PK, name, email)
-- Orders(order_id PK, customer_id FK, order_date, total)
-- Products(product_id PK, name, price, category_id FK)
-- Categories(category_id PK, category_name)
-- OrderItems(order_item_id PK, order_id FK, product_id FK, quantity, price)
```

### Primary Keys & Foreign Keys

```sql
-- Primary Key (unique identifier)
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);

-- Composite Primary Key
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id)
);

-- Foreign Key (reference to another table)
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Foreign Key with ON DELETE
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON DELETE CASCADE  -- or SET NULL, NO ACTION
);

-- Add constraints to existing table
ALTER TABLE orders
ADD CONSTRAINT fk_customer
FOREIGN KEY (customer_id) REFERENCES customers(customer_id);
```

### Indexes (Clustered, Non-clustered)

```sql
-- Clustered Index (one per table, defines physical order)
CREATE CLUSTERED INDEX idx_employee_id ON employees(employee_id);

-- Non-Clustered Index (multiple per table, pointer-based)
CREATE NONCLUSTERED INDEX idx_department ON employees(department_id);
CREATE NONCLUSTERED INDEX idx_salary ON employees(salary);

-- Composite Index
CREATE NONCLUSTERED INDEX idx_dept_salary
ON employees(department_id, salary);

-- Unique Index
CREATE UNIQUE INDEX idx_email ON users(email);

-- Covering Index (includes all columns needed)
CREATE NONCLUSTERED INDEX idx_covering
ON orders(customer_id, order_date)
INCLUDE (total_amount, status);

-- Drop Index
DROP INDEX idx_department ON employees;

-- PostgreSQL: CREATE INDEX
CREATE INDEX idx_department ON employees(department_id);
CREATE INDEX idx_dept_salary ON employees(department_id, salary);
```

### Constraints (NOT NULL, UNIQUE, CHECK)

```sql
-- NOT NULL - Column must have a value
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- UNIQUE - No duplicate values
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) UNIQUE
);

-- CHECK - Custom validation rule
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2) CHECK (price > 0),
    quantity INT CHECK (quantity >= 0),
    status VARCHAR(20) CHECK (status IN ('active', 'inactive'))
);

-- DEFAULT - Set default value
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE DEFAULT GETDATE(),
    status VARCHAR(20) DEFAULT 'pending'
);

-- Add constraint to existing table
ALTER TABLE employees
ADD CONSTRAINT chk_salary CHECK (salary > 0);

-- Remove constraint
ALTER TABLE employees
DROP CONSTRAINT chk_salary;
```

### Views (Simple, Materialized)

```sql
-- Simple View (virtual table)
CREATE VIEW v_active_employees AS
SELECT
    employee_id,
    first_name,
    last_name,
    department
FROM employees
WHERE status = 'active';

-- Using the view
SELECT * FROM v_active_employees;

-- View with JOIN
CREATE VIEW v_order_details AS
SELECT
    o.order_id,
    o.order_date,
    c.customer_name,
    p.product_name,
    oi.quantity,
    oi.unit_price
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;

-- Materialized View (stores data physically)
-- PostgreSQL
CREATE MATERIALIZED VIEW mv_monthly_sales AS
SELECT
    DATE_TRUNC('month', order_date) as month,
    SUM(total_amount) as revenue
FROM orders
GROUP BY DATE_TRUNC('month', order_date);

-- Refresh materialized view
REFRESH MATERIALIZED VIEW mv_monthly_sales;

-- SQL Server (indexed view)
CREATE VIEW v_sales_summary WITH SCHEMABINDING AS
SELECT
    DATEPART(year, order_date) as year,
    DATEPART(month, order_date) as month,
    SUM(total_amount) as revenue
FROM dbo.orders
GROUP BY DATEPART(year, order_date), DATEPART(month, order_date);

CREATE UNIQUE CLUSTERED INDEX idx_sales_summary ON v_sales_summary(year, month);
```

---

## 8. Performance & Optimization

### 📖 What is Performance & Optimization?

**Performance & Optimization** involves techniques to make database queries run faster and use fewer resources. This includes analyzing query execution plans, creating proper indexes, rewriting queries, and using database-specific features like partitioning. Optimized queries reduce costs and improve user experience.

**Key Concepts:**
- **Query Execution Plan**: How database processes a query
- **Index Optimization**: Creating right indexes for performance
- **Query Tuning**: Rewriting queries for efficiency
- **Partitioning**: Splitting large tables into smaller pieces
- **Query Hints**: Directives to influence query execution

**Why is this important for Data Engineering?**
- Processing large datasets efficiently
- Reducing ETL pipeline execution time
- Lowering cloud database costs
- Ensuring timely data delivery

### Query Execution Plans

```sql
-- SQL Server: View estimated execution plan
-- Ctrl + M in SSMS or
SET SHOWPLAN_ALL ON;
GO
SELECT * FROM orders WHERE order_date > '2024-01-01';
GO
SET SHOWPLAN_ALL OFF;

-- PostgreSQL: EXPLAIN
EXPLAIN SELECT * FROM orders WHERE order_date > '2024-01-01';

-- PostgreSQL: EXPLAIN ANALYZE (actual execution)
EXPLAIN ANALYZE
SELECT department, AVG(salary)
FROM employees
GROUP BY department;

-- MySQL: EXPLAIN
EXPLAIN SELECT * FROM orders WHERE customer_id = 100;

-- Look for:
-- - Seq Scan (sequential scan) vs Index Scan
-- - Index Seek (good) vs Table Scan (bad)
-- - Nested Loops, Hash Join, Merge Join
-- - High cost operations

-- SQL Server: Actual execution plan
SET STATISTICS IO ON;
SET STATISTICS TIME ON;
-- Run query
```

### Index Optimization

```sql
-- Create covering index for common query
-- Query: WHERE status = 'active' ORDER BY created_date
CREATE INDEX idx_status_date
ON orders(status, created_date);

-- Composite index ordering matters
-- This index supports:
-- WHERE a = 1
-- WHERE a = 1 AND b = 2
-- But NOT: WHERE b = 2
CREATE INDEX idx_a_b ON table(a, b);

-- Index on high-cardinality columns for equality
CREATE INDEX idx_customer_id ON orders(customer_id);

-- Avoid indexes on:
-- Low-cardinality columns (gender, status)
-- Frequently updated columns
-- Large text columns

-- Include columns to avoid key lookups
CREATE NONCLUSTERED INDEX idx_covering
ON orders(customer_id, order_date)
INCLUDE (total, status);

-- Partial index (PostgreSQL)
CREATE INDEX idx_active_orders
ON orders(order_date)
WHERE status = 'active';
```

### Query Tuning

```sql
-- Avoid SELECT * - specify columns
-- Bad
SELECT * FROM orders;
-- Good
SELECT order_id, order_date, total FROM orders;

-- Use EXISTS instead of IN for large tables
-- Bad
SELECT * FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders);
-- Good
SELECT * FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id);

-- Use UNION ALL instead of UNION when possible
-- Bad (removes duplicates unnecessarily)
SELECT email FROM employees
UNION
SELECT email FROM contractors;
-- Good
SELECT email FROM employees
UNION ALL
SELECT email FROM contractors
WHERE email IS NOT NULL;

-- Avoid functions on indexed columns in WHERE
-- Bad
SELECT * FROM orders WHERE YEAR(order_date) = 2024;
-- Good
SELECT * FROM orders WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01';

-- Use parameterized queries
-- Bad
SELECT * FROM orders WHERE customer_id = 100;
-- Good (prevents SQL injection, allows plan caching)
-- @customer_id parameter

-- Avoid correlated subqueries in SELECT
-- Bad
SELECT
    name,
    (SELECT COUNT(*) FROM orders WHERE customer_id = c.customer_id) as order_count
FROM customers c;
-- Good
SELECT c.name, o.order_count
FROM customers c
JOIN (SELECT customer_id, COUNT(*) as order_count FROM orders GROUP BY customer_id) o
    ON c.customer_id = o.customer_id;
```

### Partitioning

```sql
-- SQL Server: Partition by range
CREATE PARTITION FUNCTION pf_date (DATETIME)
AS RANGE RIGHT FOR VALUES (
    '2024-01-01',
    '2024-04-01',
    '2024-07-01',
    '2024-10-01'
);

CREATE PARTITION SCHEME ps_date
AS PARTITION pf_date ALL TO (PRIMARY);

CREATE TABLE orders_partitioned (
    order_id INT,
    order_date DATETIME,
    customer_id INT,
    total DECIMAL(10,2)
) ON ps_date(order_date);

-- PostgreSQL: Partition by range
CREATE TABLE orders_partitioned (
    order_id INT,
    order_date DATE,
    customer_id INT,
    total DECIMAL(10,2)
) PARTITION BY RANGE (order_date);

CREATE TABLE orders_2024 PARTITION OF orders_partitioned
    FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');

-- Query partition
SELECT * FROM orders_partitioned WHERE order_date = '2024-06-15';

-- Partition pruning happens automatically
```

### Query Hints

```sql
-- SQL Server: Use index hint
SELECT *
FROM orders WITH (INDEX(idx_customer_date))
WHERE customer_id = 100 AND order_date > '2024-01-01';

-- SQL Server: Force join type
SELECT *
FROM orders o
INNER HASH JOIN customers c ON o.customer_id = c.customer_id;

-- PostgreSQL: Enable specific join method
SELECT *
FROM orders o, customers c
WHERE o.customer_id = c.customer_id
AND c.region = 'West';

-- PostgreSQL: Set execution parameters
SET work_mem = '256MB';
SELECT * FROM big_table ORDER BY column;

-- MySQL: Use index
SELECT * FROM orders USE INDEX (idx_customer) WHERE customer_id = 100;
```

---

## 9. Database Specifics

### 📖 What are Database Specifics?

Different database systems (SQL Server, PostgreSQL, MySQL, etc.) have unique features and syntax. This section covers database-specific functionalities like stored procedures, user-defined functions, triggers, and advanced data types that are specific to certain database platforms.

**Key Concepts:**
- **Stored Procedures**: Precompiled SQL code
- **User Defined Functions (UDF)**: Custom functions
- **Triggers**: Automatic actions on events
- **Temp Tables vs Table Variables**: Temporary storage
- **JSON/JSONB**: JSON data type (PostgreSQL)
- **Arrays**: Array data type (PostgreSQL)

**Why is this important for Data Engineering?**
- Database-specific optimizations
- Complex business logic implementation
- Advanced data processing
- Integration with specific database features

### SQL Server / T-SQL

```sql
-- Stored Procedure
CREATE PROCEDURE usp_get_employees_by_department
    @department VARCHAR(50) = NULL,
    @min_salary DECIMAL = 0
AS
BEGIN
    SELECT
        employee_id,
        first_name,
        last_name,
        department,
        salary
    FROM employees
    WHERE (@department IS NULL OR department = @department)
      AND salary >= @min_salary
    ORDER BY department, salary DESC;
END;

-- Execute stored procedure
EXEC usp_get_employees_by_department @department = 'Engineering', @min_salary = 50000;

-- User Defined Function (Scalar)
CREATE FUNCTION fn_get_employee_count(@department VARCHAR(50))
RETURNS INT
AS
BEGIN
    RETURN (
        SELECT COUNT(*)
        FROM employees
        WHERE department = @department
    );
END;

-- Use function
SELECT d.name, dbo.fn_get_employee_count(d.name) as employee_count
FROM departments d;

-- User Defined Function (Table-valued)
CREATE FUNCTION fn_get_employees_by_dept(@dept VARCHAR(50))
RETURNS TABLE
AS
RETURN (
    SELECT *
    FROM employees
    WHERE department = @dept
);

-- Use table-valued function
SELECT * FROM fn_get_employees_by_dept('Sales');

-- Trigger
CREATE TRIGGER tr_audit_employee
ON employees
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    INSERT INTO employee_audit (employee_id, action, action_date)
    SELECT employee_id, 'INSERT', GETDATE()
    FROM inserted

    UNION ALL

    SELECT employee_id, 'DELETE', GETDATE()
    FROM deleted;
END;

-- Temp Tables
CREATE TABLE #temp_employees (
    employee_id INT,
    first_name VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO #temp_employees
SELECT employee_id, first_name, salary FROM employees;

SELECT * FROM #temp_employees;

-- Table Variable
DECLARE @employees TABLE (
    employee_id INT,
    first_name VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO @employees
SELECT employee_id, first_name, salary FROM employees;

-- When to use:
-- Temp Table: Large datasets, complex queries, indexes needed
-- Table Variable: Small datasets, simple queries
```

### PostgreSQL

```sql
-- JSON Data Type
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    preferences JSONB
);

-- Insert JSON data
INSERT INTO users (name, preferences)
VALUES (
    'John',
    '{"theme": "dark", "notifications": true}'::jsonb
);

-- Query JSON
SELECT preferences->>'theme' FROM users;
SELECT * FROM users WHERE preferences->>'theme' = 'dark';

-- JSON functions
SELECT jsonb_object_keys(preferences) FROM users;
SELECT * FROM users WHERE preferences @> '{"theme": "dark"}';

-- Arrays
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    tags TEXT[]
);

INSERT INTO products (name, tags)
VALUES ('Laptop', ARRAY['electronics', 'computer', 'portable']);

-- Query arrays
SELECT * FROM products WHERE 'electronics' = ANY(tags);
SELECT * FROM products WHERE tags @> ARRAY['electronics'];

-- Array functions
SELECT unnest(tags) FROM products;
SELECT array_agg(name) FROM products;

-- Full-Text Search
CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT
);

-- Create tsvector column
ALTER TABLE articles ADD COLUMN tsv TSVECTOR;

-- Populate tsvector
UPDATE articles
SET tsv = to_tsvector('english', title || ' ' || content);

-- Create index
CREATE INDEX idx_fts ON articles USING GIN(tsv);

-- Search
SELECT * FROM articles
WHERE tsv @@ plainto_tsquery('english', 'python programming');

-- tsquery operators
SELECT * FROM articles
WHERE tsv @@ to_tsquery('english', 'python & sql');
```

---

## Quick Reference

### SQL Order of Operations

| Order | Clause |
|-------|--------|
| 1 | FROM / JOIN |
| 2 | WHERE |
| 3 | GROUP BY |
| 4 | HAVING |
| 5 | SELECT |
| 6 | ORDER BY |
| 7 | LIMIT / OFFSET |

### Common SQL Commands

| Command | Description |
|---------|-------------|
| SELECT | Retrieve data |
| INSERT | Add data |
| UPDATE | Modify data |
| DELETE | Remove data |
| CREATE | Create table/database |
| ALTER | Modify structure |
| DROP | Delete table/database |

### Data Types

| Type | Description |
|------|-------------|
| INT/INTEGER | Whole numbers |
| DECIMAL/NUMERIC | Exact numbers |
| FLOAT/REAL | Approximate numbers |
| VARCHAR/TEXT | Variable-length text |
| DATE | Date only |
| DATETIME/TIMESTAMP | Date and time |
| BOOLEAN | True/False |

---

**Happy Learning! Remember: Practice makes perfect.**
