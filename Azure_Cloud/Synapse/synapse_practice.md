# Azure Synapse Analytics Practice Exercises

Practice your Azure Synapse Analytics skills with these exercises.

---

## Setup - Sample Environment

```sql
-- Synapse Workspace Configuration
-- Storage: abfss://datalake@storage.dfs.core.windows.net/
-- SQL Endpoint: synapse.sql.azuresynapse.net

-- Connect using T-SQL or Python
```

---

## Exercise Set 1: Dedicated SQL Pool - Table Creation

### Exercise 1.1: Create Table with Hash Distribution
Create a fact table with hash distribution on ProductKey.

```sql
-- YOUR CODE HERE:
-- Create FactSales table with hash distribution
-- Columns: SaleKey BIGINT, ProductKey INT, CustomerKey INT, SaleDate DATETIME, SalesAmount DECIMAL(10,2)
```

### Exercise 1.2: Create Table with Round-Robin Distribution
Create a staging table with round-robin distribution.

```sql
-- YOUR CODE HERE:
-- Create StagingTable with round-robin distribution
```

### Exercise 1.3: Create Replicated Table
Create a dimension table that is replicated on all nodes.

```sql
-- YOUR CODE HERE:
-- Create DimProduct table with replicated distribution
```

### Exercise 1.4: Create Table with Clustered Columnstore Index
Create a large table using the default clustered columnstore index.

```sql
-- YOUR CODE HERE:
```

### Exercise 1.5: Create Table with Heap
Create a small staging table with heap (no index).

```sql
-- YOUR CODE HERE:
```

---

## Exercise Set 2: Table Partitioning

### Exercise 2.1: Create Partitioned Table
Create a fact table partitioned by month.

```sql
-- YOUR CODE HERE:
-- Partition by SaleDate (monthly partitions)
```

### Exercise 2.2: Switch Partitions
Move data between tables using partition switching.

```sql
-- YOUR CODE HERE:
-- Switch partition from FactSales to FactSalesArchive
```

### Exercise 2.3: Query with Partition Pruning
Write a query that benefits from partition pruning.

```sql
-- YOUR CODE HERE:
-- Query only January 2024 data
```

---

## Exercise Set 3: Data Loading

### Exercise 3.1: COPY Statement
Load data from ADLS using COPY statement.

```sql
-- YOUR CODE HERE:
-- COPY INTO Sales from parquet files
-- Use Managed Identity authentication
```

### Exercise 3.2: CTAS (Create Table As Select)
Create a table using CTAS with data transformation.

```sql
-- YOUR CODE HERE:
-- Create FactSales from StagingSales with type casting
```

### Exercise 3.3: CETAS (Create External Table As Select)
Export data to ADLS using CETAS.

```sql
-- YOUR CODE HERE:
-- Create external table that exports to parquet
```

### Exercise 3.4: PolyBase External Table
Create and use a PolyBase external table.

```sql
-- YOUR CODE HERE:
-- Create external data source, file format, and external table
```

---

## Exercise Set 4: Materialized Views

### Exercise 4.1: Create Materialized View
Create a materialized view for sales aggregations.

```sql
-- YOUR CODE HERE:
-- Aggregate by ProductKey, Year, Month
-- Include COUNT, SUM, AVG
```

### Exercise 4.2: Query Materialized View
Query that automatically uses the materialized view.

```sql
-- YOUR CODE HERE:
-- Query total sales by product for 2024
```

### Exercise 4.3: Refresh Materialized View
Refresh the materialized view.

```sql
-- YOUR CODE HERE:
-- Rebuild or refresh the view
```

---

## Exercise Set 5: Serverless SQL Pool

### Exercise 5.1: Query Parquet with OPENROWSET
Query Parquet files directly using OPENROWSET.

```sql
-- YOUR CODE HERE:
-- Query sales data from Parquet files in data lake
```

### Exercise 5.2: Query CSV with Schema
Query CSV files with explicit column definitions.

```sql
-- YOUR CODE HERE:
-- Use WITH clause to define schema
```

### Exercise 5.3: Query with Wildcards
Query multiple files using folder paths and wildcards.

```sql
-- YOUR CODE HERE:
-- Query all Parquet files for year 2024
```

### Exercise 5.4: Create External Table in Serverless
Create an external table for easy querying.

```sql
-- YOUR CODE HERE:
-- Create database scoped credential
-- Create external data source
-- Create external table
```

---

## Exercise Set 6: Spark Pool in Synapse

### Exercise 6.1: Configure Spark Session
Set up Spark configuration for Synapse.

```python
# YOUR CODE HERE:
# Configure Spark for Synapse
spark.conf.set("spark.sql.shuffle.partitions", "200")
```

### Exercise 6.2: Read from Dedicated SQL Pool
Read data from SQL pool using Spark.

```python
# YOUR CODE HERE:
# Use spark.read.format("com.databricks.spark.sqldw")
```

### Exercise 6.3: Write to Delta Lake
Write data to Delta format in ADLS.

```python
# YOUR CODE HERE:
# Write DataFrame to Delta
```

### Exercise 6.4: Read Delta Lake
Read from Delta table.

```python
# YOUR CODE HERE:
```

### Exercise 6.5: MERGE with Delta
Perform MERGE operation on Delta table.

```python
# YOUR CODE HERE:
# Use DeltaTable for upsert
```

---

## Exercise Set 7: Query Optimization

### Exercise 7.1: Create Statistics
Create statistics on frequently queried columns.

```sql
-- YOUR CODE HERE:
-- Create statistics on ProductKey, CustomerKey
```

### Exercise 7.2: Update Statistics
Update statistics after data load.

```sql
-- YOUR CODE HERE:
```

### Exercise 7.3: View Statistics
Check statistics information.

```sql
-- YOUR CODE HERE:
-- Use DBCC SHOW_STATISTICS
```

### Exercise 7.4: Optimize Join Query
Write an optimized join query.

```sql
-- YOUR CODE HERE:
-- Join fact and dimension tables with proper distribution
```

---

## Exercise Set 8: Workload Management

### Exercise 8.1: Create Workload Group
Create a workload group for priority processing.

```sql
-- YOUR CODE HERE:
-- Create SalesGroup with min 20% resources
```

### Exercise 8.2: Create Workload Classifier
Classify queries to workload group.

```sql
-- YOUR CODE HERE:
-- Create classifier for SalesTeam
```

### Exercise 8.3: Monitor Workloads
Query workload management views.

```sql
-- YOUR CODE HERE:
-- Check dm_pdw_workload_groups and dm_pdw_waits
```

---

## Exercise Set 9: Security

### Exercise 9.1: Managed Identity for ADLS
Create external data source using Managed Identity.

```sql
-- YOUR CODE HERE:
-- Use IDENTITY = 'Managed Identity'
```

### Exercise 9.2: Grant SQL Permissions
Grant appropriate permissions to users.

```sql
-- YOUR CODE HERE:
-- Grant SELECT on schema, CREATE TABLE
```

### Exercise 9.3: Row-Level Security
Implement row-level security for regional data access.

```sql
-- YOUR CODE HERE:
-- Create security function and policy
```

### Exercise 9.4: Column-Level Security
Restrict access to sensitive columns.

```sql
-- YOUR CODE HERE:
-- Use column-level permissions
```

---

## Exercise Set 10: Data Integration

### Exercise 10.1: Create Linked Service
Define a linked service for ADLS.

```json
// YOUR CODE HERE:
{
  "name": "ls_adls",
  "type": "AzureBlobFS",
  "typeProperties": {
    "url": "https://storage.dfs.core.windows.net"
  }
}
```

### Exercise 10.2: Create Dataset
Create input and output datasets.

```json
// YOUR CODE HERE:
{
  "name": "ds_source",
  "type": "Parquet",
  "linkedServiceName": {"referenceName": "ls_adls"}
}
```

### Exercise 10.3: Create Copy Activity
Create a pipeline with copy activity.

```json
// YOUR CODE HERE:
{
  "name": "CopyData",
  "type": "Copy",
  "inputs": [{"referenceName": "ds_source"}],
  "outputs": [{"referenceName": "ds_target"}]
}
```

### Exercise 10.4: Create Pipeline with Data Flow
Create a pipeline that includes a data flow transformation.

```json
// YOUR CODE HERE:
{
  "name": "TransformPipeline",
  "activities": [
    {
      "name": "TransformData",
      "type": "DataFlow",
      "typeProperties": {
        "transformations": ["Filter", "Aggregate"]
      }
    }
  ]
}
```

---

## Exercise Set 11: Advanced Patterns

### Exercise 11.1: Slowly Changing Dimension (SCD Type 1)
Implement SCD Type 1 (update on match).

```sql
-- YOUR CODE HERE:
-- MERGE to update existing records
```

### Exercise 11.2: Incremental Data Load
Implement incremental load pattern.

```sql
-- YOUR CODE HERE:
-- Load only new records based on watermark
```

### Exercise 11.3: Audit Trail
Create audit trail for data changes.

```sql
-- YOUR CODE HERE:
-- Track insert/update timestamps
```

---

## Challenge Exercises

### Challenge 1: Build Complete Data Warehouse
Create a star schema:
1. FactSales (hash distributed)
2. DimProduct (replicated)
3. DimCustomer (replicated)
4. DimDate (replicated)
5. Load sample data using COPY

```sql
-- YOUR CODE HERE:



```

### Challenge 2: Serverless Exploration
Explore data lake using serverless SQL:
1. Query raw Parquet files
2. Create external table
3. Run analytical queries

```sql
-- YOUR CODE HERE:



```

### Challenge 3: Hybrid Pipeline
Build pipeline using both SQL and Spark:
1. Load data with COPY
2. Transform with Spark
3. Aggregate with Materialized View

```sql
-- YOUR CODE HERE:



```

---

## Testing Your Code

### Common Commands

```sql
-- Check table distribution
DBCC PDW_SHOWSPACEUSED('dbo.FactSales');

-- Check query execution
SET STATISTICS IO ON;
SET STATISTICS TIME ON;

-- Monitor queries
SELECT * FROM sys.dm_pdw_exec_requests;

-- Check partitions
SELECT * FROM sys.pdw_partitions;
```

### Serverless Query Examples

```sql
-- Query cost
SELECT * FROM sys.dm_external_query_stats;

-- List files
SELECT file_name, file_size
FROM OPENROWSET(BULK '*.parquet', ...) AS t;
```

---

## Practice Complete!

After completing these exercises, you should be comfortable with:
- Creating and managing Dedicated SQL Pool tables
- Using distribution strategies (Hash, Round-Robin, Replicated)
- Table partitioning and partition switching
- Data loading with COPY, CTAS, CETAS
- Materialized views
- Serverless SQL Pool queries
- Spark Pool integration
- Query optimization and statistics
- Workload management
- Security implementation
- Data integration pipelines

---

## Next Steps

1. Set up a Synapse workspace
2. Connect to ADLS Gen2
3. Practice with real data
4. Explore Synapse Studio
5. Set up production pipelines
