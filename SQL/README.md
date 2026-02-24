# SQL for Data Engineering

## Core Theory Concepts (Must Know)
- Relational model fundamentals (relations, tuples, attributes, keys)
- Logical query processing order (`FROM` -> `WHERE` -> `GROUP BY` -> `HAVING` -> `SELECT` -> `ORDER BY`)
- Set-based thinking vs procedural thinking
- NULL and three-valued logic (TRUE, FALSE, UNKNOWN)
- ACID transactions and isolation levels (dirty, non-repeatable, phantom reads)
- OLTP vs OLAP workload patterns and schema design implications
- Cardinality/selectivity and why they matter for query planning

## SQL Fundamentals
- SELECT, INSERT, UPDATE, DELETE
- WHERE Clause & Operators
- ORDER BY, GROUP BY, HAVING
- DISTINCT, LIMIT, OFFSET
- Aliases (AS)

## Joins
- INNER JOIN
- LEFT JOIN / RIGHT JOIN
- FULL OUTER JOIN
- CROSS JOIN
- SELF JOIN
- Multiple Table Joins

## Aggregate Functions
- COUNT, SUM, AVG, MIN, MAX
- GROUP BY with Aggregates
- HAVING vs WHERE

## Subqueries & CTEs
- Scalar Subqueries
- Correlated Subqueries
- Common Table Expressions (CTEs)
- Recursive CTEs
- Subquery in FROM, WHERE, SELECT

## Window Functions
- ROW_NUMBER(), RANK(), DENSE_RANK()
- LEAD(), LAG()
- FIRST_VALUE(), LAST_VALUE()
- SUM(), AVG() OVER()
- PARTITION BY vs GROUP BY

## Advanced SQL
- CASE WHEN (Conditional Logic)
- COALESCE, NULLIF, dialect-specific null handling (ISNULL/IFNULL/NVL)
- String Functions (CONCAT, SUBSTRING, TRIM)
- Date Functions (dialect-aware: DATEADD/DATEDIFF vs INTERVAL/DATE_TRUNC)
- UNION vs UNION ALL
- INTERSECT, EXCEPT

## Database Design
- Normalization (1NF, 2NF, 3NF, BCNF)
- Dimensional Modeling (Star Schema, Snowflake, fact and dimension tables)
- Slowly Changing Dimensions (SCD Type 1/2 basics)
- Primary Keys & Foreign Keys
- Indexes (Clustered, Non-clustered)
- Constraints (NOT NULL, UNIQUE, CHECK)
- Views (Simple, Materialized)

## Performance & Optimization
- Query Execution Plans
- Index Optimization
- Query Tuning
- Partitioning
- Query Hints

## Database Specifics
### SQL Server / T-SQL
- Stored Procedures
- User Defined Functions
- Triggers
- Temp Tables vs Table Variables

### PostgreSQL
- JSON/JSONB Data Types
- Arrays
- Full-Text Search

## Useful Resources
- Theory Notes: `./sql_theory.md`
- SQLZoo: https://sqlzoo.net/
- LeetCode SQL Problems: https://leetcode.com/problemset/database/
- HackerRank SQL: https://www.hackerrank.com/domains/sql
- Mode SQL Tutorial: https://mode.com/sql-tutorial/
