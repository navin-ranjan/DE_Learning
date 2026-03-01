# 02 - Relational Data on Azure (DP-900)

## Learning Goals

By the end of this tutorial, you should be able to:

- Explain relational design fundamentals
- Write and read core SQL queries
- Understand common relational database objects
- Choose the correct Azure relational service for a scenario

---

## 2.1 Relational Concepts

### Core Building Blocks

Relational databases organize data into tables with rows representing records and columns representing attributes. The power of relational databases comes from their ability to define relationships between tables and enforce data integrity.

#### Table

A table is the fundamental structure in a relational database. It stores rows of related records, with each row representing a single entity and each column representing an attribute of that entity.

**Example: Customers Table**

| CustomerId | Name  | Email              | City     |
|------------|-------|--------------------|----------|
| 1001       | Alice | alice@email.com    | Seattle  |
| 1002       | Bob   | bob@email.com      | New York |
| 1003       | Carol | carol@email.com    | Chicago  |

Every row has the same columns, and each column has a specific data type (integer, string, date, etc.).

---

#### Column (Attribute)

A column represents a single attribute of an entity. For example, a Customer table might have columns for CustomerId, Name, Email, Phone, Address, and City.

Each column has:
- **Data type:** Defines what values the column can hold (INT, VARCHAR, DATE, etc.)
- **Constraints:** Rules that data must follow (NOT NULL, UNIQUE, etc.)
- **Name:** Descriptive name for the attribute

---

#### Primary Key (PK)

A primary key is a column or combination of columns that uniquely identifies each row in a table. No two rows can have the same primary key value, and this value cannot be null.

**Rules:**
- Must be unique for every row
- Cannot be null (NOT NULL + UNIQUE)
- Should never change once assigned

**Examples:**
- CustomerId in a Customers table
- OrderId in an Orders table
- SSN in an Employees table (where applicable)

**Good practice:** Use auto-generated numeric IDs unless you have a natural key (like ISBN for books).

---

#### Foreign Key (FK)

A foreign key is a column in one table that references the primary key of another table. This creates a relationship between tables.

**Example:**

```
Customers Table
--------------
CustomerId (PK) | Name  | City
----------------|-------|----------
1001            | Alice | Seattle
1002            | Bob   | New York

Orders Table
------------
OrderId (PK) | CustomerId (FK) | OrderDate | Amount
-------------|-----------------|-----------|-------
5001         | 1001            | 2024-01-15| 150.00
5002         | 1001            | 2024-02-20| 75.00
5003         | 1002            | 2024-03-10| 200.00
```

The CustomerId in Orders references the CustomerId in Customers, linking each order to a specific customer.

**Benefits:**
- Enforces referential integrity (can't have orders for non-existent customers)
- Enables joining related data across tables
- Prevents orphaned records

---

#### Relationship Types

Relationships define how tables connect to each other:

**One-to-One (1:1)**
- One record in Table A relates to exactly one record in Table B
- Example: One employee has one employee badge
- Often combined into a single table for simplicity

**One-to-Many (1:N)**
- One record in Table A relates to multiple records in Table B
- Example: One customer has many orders
- Most common relationship type in analytical models
- Implemented via foreign key

**Many-to-Many (N:M)**
- Multiple records in Table A relate to multiple records in Table B
- Example: Students enroll in many courses; courses have many students
- Requires a bridge/junction table

**Example with bridge table:**

```
Students Table          StudentCourses Table        Courses Table
-------------          --------------------         -------------
StudentId (PK)         StudentId (FK)               CourseId (PK)
Name                   CourseId (FK)                CourseName
                       Grade
```

---

### Why Normalization Matters

Normalization is the process of organizing data to minimize redundancy and prevent update anomalies. It involves structuring tables and relationships to ensure data integrity.

#### Normal Forms (Simplified)

**1NF (First Normal Form):**
- Each column contains atomic (indivisible) values
- No repeating groups or arrays within a column
- Each row is unique

**Bad 1NF (repeating groups):**
| CustomerId | Name  | PhoneNumbers            |
|------------|-------|-------------------------|
| 1001       | Alice | 555-1234, 555-5678      |

**Good 1NF (atomic values):**
| CustomerId | Name  | Phone  |
|------------|-------|--------|
| 1001       | Alice | 555-1234|
| 1001       | Alice | 555-5678|

**2NF (Second Normal Form):**
- Must be in 1NF
- Remove partial dependencies (non-key columns depend on the entire primary key)

**3NF (Third Normal Form):**
- Must be in 2NF
- Remove transitive dependencies (non-key columns depend on other non-key columns)

**Example of transitive dependency (violates 3NF):**
| OrderId | ProductId | UnitPrice | TotalPrice |
|---------|-----------|-----------|------------|
| 5001    | A10       | 10.00     | 50.00      |

TotalPrice depends on UnitPrice × Quantity, not directly on OrderId. This should be calculated, not stored.

 Normalization

----

#### Benefits of **Reduced data redundancy:** Each piece of data stored once
- **Better data integrity:** Fewer places for data to become inconsistent
- **Easier updates:** Update in one place, reflected everywhere
- **Cleaner schema:** Logical organization reflects real-world entities

---

#### Tradeoffs

- **More joins for reporting:** Complex queries often require multiple joins
- **Performance overhead:** Joins add query complexity and time
- **Denormalization for analytics:** Data warehouses often denormalize for read performance

**Key insight:** OLTP systems use normalized designs for transaction integrity; OLAP systems often use denormalized designs for query performance.

---

### Common SQL Commands

#### SELECT and WHERE (Query and Filter)

```sql
-- Select specific columns with filtering
SELECT CustomerId, Name, City
FROM Customers
WHERE City = 'Seattle'
ORDER BY Name;
```

**Explanation:**
- SELECT specifies columns to return
- FROM identifies the table
- WHERE filters rows (only Seattle customers)
- ORDER BY sorts results (alphabetically by Name)

**Output:**
| CustomerId | Name  | City   |
|------------|-------|--------|
| 1001       | Alice | Seattle|
| 1005       | David | Seattle|

---

#### Aggregate with GROUP BY

```sql
-- Sum orders by customer
SELECT CustomerId, SUM(Amount) AS TotalAmount
FROM Orders
GROUP BY CustomerId
HAVING SUM(Amount) > 1000;
```

**Explanation:**
- SUM(Amount) calculates total per customer
- GROUP BY groups rows by CustomerId
- HAVING filters groups (only customers with > $1000 total)

**Output:**
| CustomerId | TotalAmount |
|------------|-------------|
| 1001       | 5000.00     |
| 1003       | 2500.00     |

**Common aggregate functions:**
- COUNT: Number of rows
- SUM: Total of values
- AVG: Average value
- MIN: Smallest value
- MAX: Largest value

---

#### JOIN Tables

```sql
-- Join customers with their orders
SELECT c.Name, o.OrderId, o.Amount
FROM Customers c
JOIN Orders o ON c.CustomerId = o.CustomerId;
```

**Explanation:**
- `c` and `o` are table aliases (shorthand)
- JOIN connects rows where CustomerId matches
- ON specifies the join condition

**Output:**
| Name  | OrderId | Amount |
|-------|---------|--------|
| Alice | 5001    | 150.00 |
| Alice | 5002    | 75.00  |
| Bob   | 5003    | 200.00 |

**Types of JOINs:**
- INNER JOIN: Only matching rows from both tables
- LEFT JOIN: All rows from left table, matching from right
- RIGHT JOIN: All rows from right table, matching from left
- FULL OUTER JOIN: All rows from both tables

---

#### Data Modification

**INSERT - Add new rows:**
```sql
INSERT INTO Customers (CustomerId, Name, City)
VALUES (1003, 'Priya', 'Austin');
```

**UPDATE - Modify existing rows:**
```sql
UPDATE Customers
SET City = 'Dallas'
WHERE CustomerId = 1003;
```

**DELETE - Remove rows:**
```sql
DELETE FROM Customers
WHERE CustomerId = 1003;
```

**⚠️ Warning:** Always include WHERE clause with UPDATE and DELETE, or you'll modify/DELETE all rows!

---

### Common Database Objects

#### Views

A view is a saved SQL query that acts like a virtual table. It doesn't store data but queries underlying tables when accessed.

**Benefits:**
- Simplify complex queries
- Hide sensitive columns from users
- Provide consistent interface despite table changes

```sql
-- Create view for customer order summary
CREATE VIEW CustomerOrderSummary AS
SELECT c.CustomerId, c.Name, COUNT(o.OrderId) AS OrderCount, SUM(o.Amount) AS TotalSpent
FROM Customers c
LEFT JOIN Orders o ON c.CustomerId = o.CustomerId
GROUP BY c.CustomerId, c.Name;
```

---

#### Indexes

An index is a data structure that improves read query speed at the cost of additional storage and slower writes.

**How it works:**
- Like a book index—find information without scanning every page
- Creates a separate structure with pointers to table rows

**Best for:**
- Columns in WHERE clauses
- Columns in JOIN conditions
- Columns in ORDER BY

**Tradeoffs:**
- Faster reads
- Slower writes (index must be updated)
- Additional storage space

```sql
-- Create index on City for faster filtering
CREATE INDEX idx_customers_city ON Customers(City);
```

---

#### Stored Procedures

A stored procedure is reusable SQL logic that executes as a single unit. It can accept parameters and contain multiple statements.

**Benefits:**
- Reduced network traffic (one call vs multiple queries)
- Reusable logic
- Security (grant execute permission, not table access)

```sql
CREATE PROCEDURE GetCustomerOrders
    @CustomerId INT
AS
BEGIN
    SELECT * FROM Orders
    WHERE CustomerId = @CustomerId;
END;

-- Execute
EXEC GetCustomerOrders @CustomerId = 1001;
```

---

#### Functions

Functions return a value and can be used in SQL expressions. Unlike stored procedures, functions can be used within SELECT statements.

**Built-in functions:**
- String: LENGTH, UPPER, SUBSTRING
- Date: GETDATE, DATEADD, DATEDIFF
- Math: ROUND, ABS, POWER

**User-defined functions:**
```sql
CREATE FUNCTION CalculateDiscount
    (@Amount DECIMAL, @DiscountRate DECIMAL)
RETURNS DECIMAL
AS
BEGIN
    RETURN @Amount * @DiscountRate;
END;

-- Use in query
SELECT Amount, dbo.CalculateDiscount(Amount, 0.1) AS Discount
FROM Orders;
```

---

### Exam Focus

- **Understand when relational systems are best:** Transactions + strong consistency requirements
- **Know PK/FK purpose:** Primary keys uniquely identify records; foreign keys create relationships
- **Know join basics:** Understand how to combine data from multiple tables

---

## 2.2 Azure Relational Data Services

### Azure SQL Database

**What it is:** Fully managed Platform-as-a-Service (PaaS) SQL Server database in Azure.

**Best for:**
- Cloud-native SQL workloads
- Applications wanting minimal infrastructure management
- Elastic scaling requirements
- Built-in high availability

**Key features:**
- **PaaS simplicity:** Microsoft manages infrastructure, backups, patching
- **Automatic backups:** Point-in-time restore capability
- **Elastic pools:** Share resources across multiple databases
- **Active geo-replication:** Distribute reads globally
- **Intelligent performance:** Automatic query tuning

**When to choose:**
- New cloud applications
- Migration from on-premises with app refactoring
- When you want to focus on data, not infrastructure
- Scenarios where PaaS limitations are acceptable

**Service tiers:**
- Basic: Development and light workloads
- Standard: General purpose workloads
- Premium/Business Critical: Performance-intensive workloads

---

### Azure SQL Managed Instance

**What it is:** Managed instance of SQL Server with near-complete compatibility.

**Best for:**
- Migrating on-premises SQL Server with minimal changes
- Applications requiring SQL Server features not in Azure SQL Database
- Lift-and-shift scenarios

**Key features:**
- **High compatibility:** Supports SQL Server Agent, linked servers, Service Broker, CLR
- **Native network support:** Connect from on-premises using private IPs
- **Instance-level features:** Database mail, SQL Profiler, Database Tuning Advisor
- **Managed service:** Microsoft handles patching, backups, high availability

**When to choose:**
- Migration from on-premises where full compatibility is needed
- When you need features not available in Azure SQL Database
- When application changes should be minimal
- Enterprise applications with complex SQL Server usage

**Difference from Azure SQL Database:**
- Managed Instance = whole SQL Server instance (more features)
- Azure SQL Database = single database (simpler, more elastic)

---

### SQL Server on Azure Virtual Machines

**What it is:** SQL Server installed on an Azure virtual machine that you manage.

**Best for:**
- Maximum control over OS and SQL Server configuration
- Legacy applications requiring specific configurations
- Scenarios not supported by PaaS

**Key features:**
- **Full control:** Complete access to OS and SQL Server settings
- **Custom installations:** Any SQL Server version with custom configurations
- **Existing licenses:** Bring your own SQL Server license
- **Third-party software:** Install additional software as needed

**When to choose:**
- Regulatory requirements demanding specific configurations
- Need for features not in PaaS offerings
- Migration from on-premises with no refactoring
- Running other software on the same server

**Tradeoff:** Highest operational overhead—you manage everything (OS, SQL, backups, patching, high availability).

---

### Azure Database for PostgreSQL

**What it is:** Managed PostgreSQL database service in Azure.

**Best for:**
- Applications built on PostgreSQL
- Open-source preference with enterprise features
- Extensions like PostGIS, pgvector, Citus

**Deployment options:**
- **Single Server:** Simple, cost-effective for most workloads
- **Flexible Server:** Better control with burstable instances
- **Hyperscale (Citus):** Distributed PostgreSQL for massive scale

**When to choose:**
- New applications using PostgreSQL
- Migrating from on-premises PostgreSQL
- Need for PostgreSQL extensions
- When your team knows PostgreSQL

---

### Azure Database for MySQL

**What it is:** Managed MySQL database service in Azure.

**Best for:**
- MySQL-based web applications
- Content management systems (WordPress, Drupal)
- PHP, Python, or Node.js applications using MySQL

**Key features:**
- **High availability:** Single server with auto-failover
- **Import tools:** Easy migration from existing MySQL
- **Read replicas:** Scale read-heavy workloads
- **Automatic backups:** Point-in-time restore

**When to choose:**
- Existing MySQL applications
- LAMP stack applications
- PHP-based web applications

---

### Service Selection Quick Matrix

| Requirement | Recommended Service |
|-------------|---------------------|
| Lowest admin overhead for SQL Server | Azure SQL Database |
| Best SQL Server compatibility for migration | Azure SQL Managed Instance |
| Full server/OS control | SQL Server on Azure VM |
| Managed PostgreSQL | Azure Database for PostgreSQL |
| Managed MySQL | Azure Database for MySQL |
| New cloud-native SQL app | Azure SQL Database |
| Migrate with minimal changes | Azure SQL Managed Instance |
| Regulatory need for full control | SQL Server on Azure VM |

---

## Mini Hands-On Flow

### Step 1: Create Azure SQL Database
1. Go to Azure Portal
2. Create new resource → Azure SQL Database
3. Configure: Server, Database name, Pricing tier
4. Configure firewall rules for access

### Step 2: Connect Using Tools
- **Azure Data Studio:** Free cross-platform tool
- **SQL Server Management Studio (SSMS):** Full-featured Windows tool

### Step 3: Create Tables

```sql
-- Create Customers table
CREATE TABLE Customers (
    CustomerId INT PRIMARY KEY,
    Name VARCHAR(100),
    City VARCHAR(50)
);

-- Create Orders table
CREATE TABLE Orders (
    OrderId INT PRIMARY KEY,
    CustomerId INT,
    OrderDate DATE,
    Amount DECIMAL(10,2),
    FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId)
);
```

### Step 4: Insert Sample Data

```sql
INSERT INTO Customers VALUES
(1001, 'Alice', 'Seattle'),
(1002, 'Bob', 'New York'),
(1003, 'Carol', 'Chicago');

INSERT INTO Orders VALUES
(5001, 1001, '2024-01-15', 150.00),
(5002, 1001, '2024-02-20', 75.00),
(5003, 1002, '2024-03-10', 200.00);
```

### Step 5: Run Queries

**Join query:**
```sql
SELECT c.Name, o.OrderId, o.Amount
FROM Customers c
JOIN Orders o ON c.CustomerId = o.CustomerId;
```

**Aggregation with grouping:**
```sql
SELECT c.Name, SUM(o.Amount) AS TotalSpent
FROM Customers c
JOIN Orders o ON c.CustomerId = o.CustomerId
GROUP BY c.Name;
```

### Step 6: Add Index and Compare Performance

```sql
-- Add index
CREATE INDEX idx_orders_customer ON Orders(CustomerId);

-- Check query execution (in Azure Data Studio)
SET STATISTICS IO ON;
SELECT * FROM Orders WHERE CustomerId = 1001;
```

---

## Expected Learning Outcomes

After this hands-on exercise, you should understand:

- **SQL query patterns:** SELECT, JOIN, GROUP BY
- **Relational design:** How tables connect via keys
- **Index impact:** How indexes improve query performance

---

## Common Mistakes to Avoid

1. **Treating SQL Managed Instance and SQL Database as identical:** They have different capabilities—Managed Instance offers more SQL Server features
2. **Overusing indexes on frequently updated tables:** Every INSERT/UPDATE must maintain the index, slowing writes
3. **Mixing OLTP schema design with analytics query needs:** Normalized tables are great for transactions but may need denormalization for reporting

---

## Quick Self-Check Questions

1. **Can you explain when to choose SQL Database vs Managed Instance?**
   - SQL Database: New apps, cloud-native
   - Managed Instance: Migration with compatibility needs

2. **Can you write a query with JOIN + GROUP BY?**
   - JOIN tables on related columns
   - GROUP BY the dimension you want to aggregate by

3. **Can you explain one benefit and one tradeoff of normalization?**
   - Benefit: Reduced redundancy, better integrity
   - Tradeoff: More joins for complex queries
