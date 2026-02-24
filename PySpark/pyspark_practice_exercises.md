# PySpark Practice Exercises

Practice your PySpark skills with these exercises.

---

## Sample Data Setup

```python
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

spark = SparkSession.builder \
    .appName("PracticeExercises") \
    .master("local[*]") \
    .getOrCreate()

# Create employees DataFrame
employees_data = [
    (1, "John", "Doe", "Engineering", 85000, "2020-01-15", "New York"),
    (2, "Jane", "Smith", "Engineering", 75000, "2021-03-20", "New York"),
    (3, "Bob", "Johnson", "Sales", 65000, "2019-07-10", "Chicago"),
    (4, "Alice", "Williams", "Sales", 70000, "2022-02-14", "Chicago"),
    (5, "Charlie", "Brown", "Marketing", 55000, "2023-06-01", "Los Angeles"),
    (6, "Diana", "Miller", "Engineering", 90000, "2018-11-05", "New York"),
    (7, "Eve", "Davis", "Marketing", 62000, "2021-09-15", "Los Angeles"),
    (8, "Frank", "Garcia", "HR", 58000, "2022-04-22", "Boston")
]

employees_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("department", StringType(), True),
    StructField("salary", DoubleType(), True),
    StructField("hire_date", StringType(), True),
    StructField("city", StringType(), True)
])

employees = spark.createDataFrame(employees_data, employees_schema)

# Create departments DataFrame
departments_data = [
    ("Engineering", "New York", 100),
    ("Sales", "Chicago", 200),
    ("Marketing", "Los Angeles", 300),
    ("HR", "Boston", 400),
    ("IT", "Seattle", 500)
]

departments = spark.createDataFrame(departments_data, ["department_name", "location", "dept_id"])

# Create products DataFrame
products_data = [
    (1, "Laptop", "Electronics", 999.99, 50),
    (2, "Mouse", "Electronics", 29.99, 200),
    (3, "Keyboard", "Electronics", 79.99, 150),
    (4, "Desk", "Furniture", 299.99, 30),
    (5, "Chair", "Furniture", 199.99, 40),
    (6, "Monitor", "Electronics", 349.99, 75)
]

products = spark.createDataFrame(products_data, ["product_id", "product_name", "category", "price", "stock"])

# Create orders DataFrame
orders_data = [
    (1, 101, "2024-01-15", 1099.98, "Completed"),
    (2, 102, "2024-01-20", 229.98, "Completed"),
    (3, 101, "2024-02-10", 79.99, "Pending"),
    (4, 103, "2024-02-15", 549.98, "Completed"),
    (5, 102, "2024-03-01", 399.99, "Shipped")
]

orders = spark.createDataFrame(orders_data, ["order_id", "customer_id", "order_date", "total", "status"])
```

---

## Exercise Set 1: Basic DataFrame Operations

1. Show all data from the employees DataFrame.
2. Select only `first_name`, `last_name`, and `salary` columns.
3. Add a new column `salary_annual` (multiply salary by 12).
4. Rename column `first_name` to `firstName`.
5. Drop the `city` column.
6. Filter employees with salary greater than 60000.
7. Filter employees in 'Engineering' department.
8. Sort employees by salary in descending order.
9. Get only the first 3 rows.
10. Remove duplicate department values.
11. Show the schema of the employees DataFrame.
12. Use `selectExpr` to add a column with salary divided by 12.
13. Show only distinct combinations of department and city.
14. Limit the result to 5 rows.
15. Use `filter` with multiple conditions (salary > 60000 AND department = 'Sales').

---

## Exercise Set 2: Working with Columns and Functions

1. Convert all first names to uppercase.
2. Concatenate first_name and last_name as `full_name`.
3. Get the length of each employee's first name.
4. Extract the year from hire_date.
5. Add a column `salary_category` where salary > 70000 is 'High', else 'Low'.
6. Replace null values in salary with 0.
7. Use `when` and `otherwise` to categorize departments.
8. Use `substring` to extract first 3 characters of department.
9. Trim whitespace from employee names.
10. Use `regexp_replace` to replace 'Engineering' with 'Eng'.
11. Add a column with current date using `current_date()`.
12. Use `datediff` to calculate days since hire.
13. Round the salary to nearest integer.
14. Use `concat_ws` to join columns with separator.
15. Use `split` to split department names into array.

---

## Exercise Set 3: Aggregations

1. Count the total number of employees.
2. Find the average salary.
3. Find the minimum and maximum salary.
4. Sum all salaries per department.
5. Count employees per department.
6. Find the average salary per city.
7. Get distinct department names.
8. Use `agg` to get multiple aggregations at once.
9. Use `groupBy` with multiple columns (department, city).
10. Find the total salary expense for the company.
11. Use `pivot` to pivot data by department.
12. Count distinct cities per department.
13. Use `cube` to get all combinations of grouping.
14. Use `rollup` for hierarchical aggregation.
15. Find employees with above-average salary using subquery.
16. Use `grouping` function to identify subtotal rows.

---

## Exercise Set 4: Joins

1. Join employees with departments (by department name).
2. Perform a left join and keep all employees.
3. Perform a right join and keep all departments.
4. Perform an outer join.
5. Join orders with employees (using customer_id = id).
6. Join multiple DataFrames (employees, departments, orders).
7. Perform a cross join and explain the result.
8. Use broadcast join for small department DataFrame.
9. Join with complex join condition (multiple columns).
10. Self-join employees to find manager relationships.
11. Handle join when column names are different.
12. Perform anti-join (employees not in any department).
13. Perform semi-join (employees in departments).
14. Join orders with products using multiple keys.
15. Handle duplicate column names after join using `alias`.

---

## Exercise Set 5: Window Functions

1. Add row number to employees ordered by salary.
2. Rank employees by salary within each department.
3. Calculate running total of salaries ordered by hire_date.
4. Get the previous employee's salary.
5. Calculate the difference from department average salary.
6. Get the top 2 highest paid employees per department.
7. Use `dense_rank` instead of `rank`.
8. Calculate moving average of salary (last 3 employees).
9. Use `lead` to get next hire date.
10. Use `percent_rank` to calculate percentile.
11. Use `cume_dist` for cumulative distribution.
12. Calculate sum over entire partition (no orderBy).
13. Use `nth_value` to get 3rd highest salary.
14. Use window functions with multiple partitions.
15. Calculate running count of employees hired.
16. Use `lag` with offset of 2.

---

## Exercise Set 6: Spark SQL

1. Create a temporary view from employees DataFrame.
2. Run a SQL query to select all Engineering employees.
3. Run a SQL query with GROUP BY and aggregate functions.
4. Register a UDF and use it in SQL.
5. Create a global temp view.
6. Create a view with a specific column list.
7. Run SQL with HAVING clause.
8. Use SQL window functions.
9. Register a pandas UDF and use in SQL.
10. Use SQL JOIN in spark.sql().
11. Drop a temporary view.
12. List all existing tables/views.
13. Run a SQL query with subquery.
14. Use SQL to filter with LIKE pattern.
15. Use SQL to perform CASE WHEN operations.
16. Use SQL with ORDER BY and LIMIT.

---

## Exercise Set 7: Handling NULL Values

1. Find rows with null values in any column.
2. Fill null salaries with 50000.
3. Drop rows with any null values.
4. Use `coalesce` to replace nulls with a default value.
5. Find rows where city is NULL.
6. Fill null values in multiple columns at once.
7. Drop duplicates after filling nulls.
8. Use `na.fill` with dictionary for selective filling.
9. Use `na.replace` to replace specific values.
10. Use `when` to conditionally handle nulls.
11. Check for null using `isnull` and `isnotnull`.
12. Use `nullif` to return NULL for specific values.
13. Filter out rows with null in critical columns.
14. Use `fill` with subset of columns.
15. Handle nulls in string columns.
16. Use `ifnull` equivalent in PySpark.

---

## Exercise Set 8: Working with Different File Formats

1. Read a CSV file with header and inferred schema.
2. Write employees DataFrame to Parquet format.
3. Read a JSON file.
4. Write to CSV with header.
5. Read from multiple CSV files using wildcard.
6. Read Parquet with specific columns.
7. Write with partitionBy (e.g., by year).
8. Read JSON with multiline option.
9. Write to JSON format.
10. Read CSV with custom delimiter.
11. Write Parquet with compression (snappy/gzip).
12. Read from multiple directories.
13. Write to ORC format.
14. Read CSV with header false.
15. Write DataFrame to a specific number of files.
16. Read specific columns from CSV.

---

## Exercise Set 9: RDD Operations

1. Create an RDD from the employees DataFrame.
2. Create an RDD from a list.
3. Map the RDD to extract only names.
4. Filter RDD elements with salary > 60000.
5. Use reduceByKey to sum salaries per department.
6. Count the number of elements in RDD.
7. Use flatMap to split a list of strings.
8. Perform a groupByKey operation.
9. Use aggregate to calculate sum and count.
10. Save RDD to text file.
11. Use mapPartitions for partition-level operations.
12. Use union to combine two RDDs.
13. Use intersection to find common elements.
14. Use distinct to remove duplicates.
15. Use sortByKey to sort by salary.
16. Use cartesian to create cartesian product.
17. Use coalesce to reduce partitions.
18. Use repartition to increase partitions.
19. Convert RDD back to DataFrame.
20. Use fold to calculate sum with initial value.

---

## Exercise Set 10: Performance Optimization

1. Cache the employees DataFrame.
2. Check if DataFrame is cached.
3. Unpersist a cached DataFrame.
4. Repartition the DataFrame to 4 partitions.
5. Use coalesce to reduce partitions.
6. Explain the query plan.
7. Use broadcast for a small DataFrame join.
8. Check storage level of cached DataFrame.
9. Use `persist` with MEMORY_AND_DISK.
10. Use `unpersist` blocking mode.
11. Configure shuffle partitions.
12. Use AQE (Adaptive Query Execution).
13. Optimize join order.
14. Use filter pushdown.
15. Check partition count.

---

## Exercise Set 11: DataFrame Transformations

1. Use `union` to combine two DataFrames.
2. Use `unionByName` with different column order.
3. Use `intersect` to find common rows.
4. Use `except` to find different rows.
5. Use `sample` to get fraction of data.
6. Use `randomSplit` to split data.
7. Use `stat` for statistical operations.
8. Use `crosstab` for cross-tabulation.
9. Use `freqItems` for frequent items.
10. Use `summary` for statistics.
11. Use `describe` for basic statistics.
12. Use `cov` and `corr` for correlation.
13. Use `approxQuantile` for quantile approximation.
14. Use `foreach` for row-level operations.
15. Use `repartitionAndSortWithinPartitions`.

---

## Exercise Set 12: Advanced Data Operations

1. Use `explode` to flatten arrays.
2. Use `array` to create array column.
3. Use `map` to create map column.
4. Use `json_tuple` to parse JSON.
5. Use `from_json` to convert string to JSON.
6. Use `to_json` to convert to JSON string.
7. Use `array_agg` to aggregate into array.
8. Use `collect_list` for aggregation.
9. Use `struct` to create struct column.
10. Use `array_contains` for array filtering.
11. Use `array_position` to find index.
12. Use `array_remove` to remove elements.
13. Use `flatten` to flatten nested arrays.
14. Use `array_distinct` to remove duplicates.
15. Use `map_keys` and `map_values`.

---

## Challenge Questions

**Challenge 1:** Create a report showing:
- Employee full name
- Department
- Salary
- Department average salary
- Percentage of department total salary

**Challenge 2:** Calculate month-over-month revenue growth from orders.

**Challenge 3:** Find the second highest salary in each department.

**Challenge 4:** Create a pivot table showing total sales by department and year.

**Challenge 5:** Find employees hired after 2020 whose salary is above their department's average.

**Challenge 6:** Create a complete employee hierarchy using self-join and window functions.

**Challenge 7:** Implement a running total and moving average for daily sales.

**Challenge 8:** Find the most popular product category by revenue.

**Challenge 9:** Calculate employee tenure and categorize into experience levels.

**Challenge 10:** Build a complete ETL pipeline reading from CSV, transforming, and writing to Parquet.
