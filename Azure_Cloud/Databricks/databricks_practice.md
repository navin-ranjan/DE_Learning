# Azure Databricks Practice Exercises

Practice your Azure Databricks skills with these exercises.

---

## Setup - Sample Environment

```python
# Databricks Configuration
storage_path = "abfss://datalake@storage.dfs.core.windows.net/"
delta_path = f"{storage_path}delta/"

# Create Spark Session
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DatabricksPractice") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .getOrCreate()
```

---

## Exercise Set 1: Delta Lake Basics

### Exercise 1.1: Create Delta Table
Create a Delta table from a DataFrame.

```python
# YOUR CODE HERE:
# Create sample data
data = [
    (1, "Product A", 100, "2024-01-01"),
    (2, "Product B", 200, "2024-01-02"),
    (3, "Product C", 150, "2024-01-03")
]
df = spark.createDataFrame(data, ["id", "name", "price", "date"])

# Write to Delta format
# YOUR CODE HERE:
```

### Exercise 1.2: Read Delta Table
Read data from the Delta table you created.

```python
# YOUR CODE HERE:
# Read using spark.read.format("delta")
```

### Exercise 1.3: Append Data
Append new records to the Delta table.

```python
# YOUR CODE HERE:
# Add new records using mode("append")
```

### Exercise 1.4: Overwrite Data
Overwrite the entire Delta table.

```python
# YOUR CODE HERE:
# Use mode("overwrite")
```

### Exercise 1.5: Partitioned Delta Table
Create a Delta table partitioned by date.

```python
# YOUR CODE HERE:
# Use partitionBy("date")
```

---

## Exercise Set 2: Delta Lake CRUD Operations

### Exercise 2.1: Update Records
Update specific records in a Delta table.

```python
# YOUR CODE HERE:
# Use DeltaTable for update operation
from delta.tables import DeltaTable

# Update price where id = 1
```

### Exercise 2.2: Delete Records
Delete records based on a condition.

```python
# YOUR CODE HERE:
# Delete records where price < 150
```

### Exercise 2.3: MERGE Operation (Upsert)
Perform MERGE to insert new and update existing records.

```python
# YOUR CODE HERE:
# Create updates DataFrame
updates_data = [
    (1, "Product A Updated", 120, "2024-01-01"),
    (4, "Product D", 300, "2024-01-04")
]
updates_df = spark.createDataFrame(updates_data, ["id", "name", "price", "date"])

# MERGE into target table
```

### Exercise 2.4: Schema Enforcement
Verify schema enforcement - try to write DataFrame with different schema.

```python
# YOUR CODE HERE:
# Try writing with extra column - should fail
```

### Exercise 2.5: Schema Evolution
Enable schema evolution to add new columns.

```python
# YOUR CODE HERE:
# Use option("mergeSchema", "true")
```

---

## Exercise Set 3: Time Travel & History

### Exercise 3.1: View Table History
View the history of changes to a Delta table.

```python
# YOUR CODE HERE:
# Use DESCRIBE HISTORY
```

### Exercise 3.2: Time Travel by Version
Query a previous version of the table.

```python
# YOUR CODE HERE:
# Use option("versionAsOf", 0)
```

### Exercise 3.3: Time Travel by Timestamp
Query table at a specific timestamp.

```python
# YOUR CODE HERE:
# Use option("timestampAsOf", "2024-01-01")
```

### Exercise 3.4: Restore Table
Restore a Delta table to a previous version.

```python
# YOUR CODE HERE:
# Use RESTORE TABLE TO VERSION AS OF
```

### Exercise 3.5: Vacuum Old Files
Clean up old data files.

```python
# YOUR CODE HERE:
# Use VACUUM command
```

---

## Exercise Set 4: Medallion Architecture

### Exercise 4.1: Bronze Layer - Raw Ingestion
Ingest raw data into Bronze layer.

```python
# YOUR CODE HERE:
# Create Bronze table with raw data
# Read from CSV, write to Delta with partitionBy("ingestion_date")
```

### Exercise 4.2: Silver Layer - Data Cleansing
Clean and transform data from Bronze to Silver.

```python
# YOUR CODE HERE:
# Read from Bronze
# Apply transformations:
# - Remove duplicates
# - Handle nulls
# - Add derived columns
# - Cast data types
# Write to Silver
```

### Exercise 4.3: Gold Layer - Business Aggregates
Create aggregated tables for analytics.

```python
# YOUR CODE HERE:
# Read from Silver
# Create aggregations by product, customer, region
# Write to Gold
```

### Exercise 4.4: Complete Pipeline
Build the complete Bronze -> Silver -> Gold pipeline.

```python
# YOUR CODE HERE:
# Combine all three layers in one notebook cell
```

---

## Exercise Set 5: Structured Streaming

### Exercise 5.1: Read from Kafka
Connect to Kafka and read streaming data.

```python
# YOUR CODE HERE:
# Configure Kafka source
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker:9092") \
    .option("subscribe", "sales_topic") \
    .load()
```

### Exercise 5.2: Parse JSON Stream
Parse JSON data from Kafka stream.

```python
# YOUR CODE HERE:
# Use from_json to parse JSON
schema = "sale_id INT, product_id INT, amount DECIMAL(10,2)"
```

### Exercise 5.3: Write Stream to Delta
Write streaming data to Delta table.

```python
# YOUR CODE HERE:
# Use writeStream with checkpointLocation
```

### Exercise 5.4: Windowed Aggregations
Calculate aggregations over time windows.

```python
# YOUR CODE HERE:
# Use window() function for 5-minute windows
```

### Exercise 5.5: Streaming Join
Join stream with static reference data.

```python
# YOUR CODE HERE:
# Join streaming data with product dimension table
```

---

## Exercise Set 6: Auto Loader

### Exercise 6.1: Basic Auto Loader
Use Auto Loader to ingest files incrementally.

```python
# YOUR CODE HERE:
# Use cloudFiles format
spark.readStream \
    .format("cloudFiles") \
    .option("cloudFiles.format", "json") \
    .option("cloudFiles.schemaLocation", "/mnt/delta/schema") \
    .load("/mnt/source/data")
```

### Exercise 6.2: Schema Inference
Configure Auto Loader for automatic schema inference.

```python
# YOUR CODE HERE:
# Set schemaLocation for inference
```

### Exercise 6.3: Schema Evolution
Enable schema evolution for new columns.

```python
# YOUR CODE HERE:
# Use cloudFiles.schemaEvolutionMode
```

### Exercise 6.4: Triggered Batch Load
Load data using Auto Loader in batch mode.

```python
# YOUR CODE HERE:
# Use read (not readStream) with cloudFiles
```

---

## Exercise Set 7: Unity Catalog

### Exercise 7.1: Create Catalog
Create a new catalog in Unity Catalog.

```python
# YOUR CODE HERE:
spark.sql("""
    CREATE CATALOG IF NOT EXISTS practice_catalog
    COMMENT 'Practice catalog for learning'
""")
```

### Exercise 7.2: Create Schema
Create a schema within the catalog.

```python
# YOUR CODE HERE:
spark.sql("""
    CREATE SCHEMA IF NOT EXISTS practice_catalog.sales
""")
```

### Exercise 7.3: Grant Permissions
Grant SELECT permission to a user or group.

```python
# YOUR CODE HERE:
# Grant table access
GRANT SELECT ON TABLE practice_catalog.sales.table_name TO `user@company.com`
```

### Exercise 7.4: Create External Location
Set up external location for ADLS.

```python
# YOUR CODE HERE:
spark.sql("""
    CREATE EXTERNAL LOCATION IF NOT EXISTS landing_zone
    URL 'abfss://landing@storage.dfs.core.windows.net/'
    STORAGE CREDENTIAL adls_credential
""")
```

### Exercise 7.5: View Lineage
Query data lineage information.

```python
# YOUR CODE HERE:
spark.sql("""
    SELECT * FROM system.information_schema.lineage
    WHERE table_name = 'gold_table'
""")
```

---

## Exercise Set 8: Performance Optimization

### Exercise 8.1: Repartition Data
Repartition DataFrame for optimal processing.

```python
# YOUR CODE HERE:
# Use repartition() to control file count
```

### Exercise 8.2: Coalesce Files
Reduce number of output files.

```python
# YOUR CODE HERE:
# Use coalesce() for fewer files after aggregation
```

### Exercise 8.3: Optimize Delta Table
Run OPTIMIZE on Delta table.

```python
# YOUR CODE HERE:
spark.sql("OPTIMIZE delta_table")
```

### Exercise 8.4: Z-Order Optimization
Apply Z-ORDER for better query performance.

```python
# YOUR CODE HERE:
# Z-ORDER by frequently filtered columns
```

### Exercise 8.5: Configure Broadcast Join
Set broadcast join threshold for small tables.

```python
# YOUR CODE HERE:
# Configure spark.sql.autoBroadcastJoinThreshold
```

### Exercise 8.6: Cache DataFrame
Cache frequently accessed DataFrame.

```python
# YOUR CODE HERE:
# Use df.cache() and df.persist()
```

---

## Exercise Set 9: Data Engineering Patterns

### Exercise 9.1: Incremental Loading with Watermark
Implement incremental loading pattern.

```python
# YOUR CODE HERE:
# 1. Get last watermark
# 2. Read new data
# 3. Update watermark
```

### Exercise 9.2: Change Data Capture (CDC)
Process CDC data with MERGE.

```python
# YOUR CODE HERE:
# Handle inserts, updates, deletes from CDC
```

### Exercise 9.3: Slowly Changing Dimension (SCD Type 2)
Implement SCD Type 2 for dimension tables.

```python
# YOUR CODE HERE:
# Track historical changes with start/end dates
```

### Exercise 9.4: Data Quality Checks
Add data quality validation in pipeline.

```python
# YOUR CODE HERE:
# Check for nulls, duplicates, valid values
```

---

## Exercise Set 10: Spark SQL Operations

### Exercise 10.1: Create Temp View
Create temporary view from DataFrame.

```python
# YOUR CODE HERE:
df.createOrReplaceTempView("sales")
```

### Exercise 10.2: Run SQL Query
Execute SQL query on the view.

```python
# YOUR CODE HERE:
spark.sql("SELECT * FROM sales WHERE amount > 100")
```

### Exercise 10.3: Aggregations with SQL
Perform aggregations using SQL.

```python
# YOUR CODE HERE:
# Group by and aggregate functions
```

### Exercise 10.4: Joins with SQL
Join multiple tables using SQL.

```python
# YOUR CODE HERE:
# Inner join on product_id
```

### Exercise 10.5: Window Functions
Use window functions for ranking.

```python
# YOUR CODE HERE:
# ROW_NUMBER(), RANK(), SUM() OVER
```

---

## Challenge Exercises

### Challenge 1: Build Complete Lakehouse
Create a complete lakehouse with:
1. Bronze: Ingest raw sales data
2. Silver: Clean and deduplicate
3. Gold: Sales aggregations by region and product

```python
# YOUR CODE HERE:



```

### Challenge 2: Real-Time Dashboard Pipeline
Build streaming pipeline:
1. Read from Kafka
2. Process with windowed aggregations
3. Write to Delta for real-time dashboard

```python
# YOUR CODE HERE:



```

### Challenge 3: CDC Pipeline
Implement CDC processing:
1. Read CDC changes from staging
2. Apply MERGE to target table
3. Track history with Delta

```python
# YOUR CODE HERE:



```

---

## Testing Your Code

### Common Commands

```python
# Show DataFrame schema
df.printSchema()

# Show execution plan
df.explain(True)

# Count rows
df.count()

# Show first N rows
df.show(10)

# Check if cached
spark.catalog.isCached("tableName")

# List tables
spark.catalog.listTables()

# Clear cache
spark.catalog.clearCache()
```

### Delta Lake Commands

```sql
-- View history
DESCRIBE HISTORY table_name

-- Time travel
SELECT * FROM table VERSION AS OF 0

-- Optimize
OPTIMIZE table_name ZORDER BY (col1, col2)

-- Vacuum
VACUUM table_name RETAIN 168 HOURS

-- Merge
MERGE INTO target USING source ON condition
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *
```

---

## Practice Complete!

After completing these exercises, you should be comfortable with:
- Creating and managing Delta tables
- CRUD operations (Create, Read, Update, Delete)
- Time travel and history
- Medallion architecture (Bronze/Silver/Gold)
- Structured Streaming
- Auto Loader for file ingestion
- Unity Catalog for governance
- Performance optimization
- Data engineering patterns
- Spark SQL operations

---

## Next Steps

1. Set up a Databricks workspace
2. Connect to ADLS for storage
3. Practice with real data sources
4. Explore MLflow for ML workflows
5. Set up production jobs
