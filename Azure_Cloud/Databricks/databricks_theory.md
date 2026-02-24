# Azure Databricks Theory & Tutorial

This file follows `README.md` and provides comprehensive theory explanations with practical examples for Databricks-based data engineering.

## Table of Contents

1. [Lakehouse Fundamentals](#1-lakehouse-fundamentals)
2. [Databricks Architecture & Compute](#2-databricks-architecture--compute)
3. [Delta Lake Deep Dive](#3-delta-lake-deep-dive)
4. [Data Engineering Patterns](#4-data-engineering-patterns)
5. [Unity Catalog & Governance](#5-unity-catalog--governance)
6. [Performance Optimization](#6-performance-optimization)
7. [Quick Reference](#7-quick-reference)

---

## 1. Lakehouse Fundamentals

### 📖 What is a Lakehouse?

A **Lakehouse** is a new, open architecture that combines the best elements of data lakes and data warehouses. It provides:

- **Data lake flexibility**: Store any type of data (structured, semi-structured, unstructured) at low cost in open formats
- **Data warehouse reliability**: ACID transactions, schema enforcement, and BI/analytics capabilities
- **Lakehouse unification**: Single platform for ML, analytics, and data engineering

**Key Principles:**
- Open file formats (Parquet, Delta) stored on object storage
- Separated storage and compute for elasticity
- ACID transactions on object storage
- Support for both batch and streaming workloads

**Why is this important for Data Engineering?**
- Eliminates data silos by supporting all data types
- Reduces costs by using commodity object storage
- Enables single platform for all data workloads
- Simplifies architecture by removing the need for separate lake and warehouse systems

### Traditional Architecture vs Lakehouse

| Aspect | Data Lake + Warehouse | Lakehouse |
|--------|----------------------|-----------|
| Storage | Separate systems | Single object storage |
| Format | Various (CSV, JSON, Parquet) | Open formats (Parquet, Delta) |
| Transactions | Not supported | ACID compliant |
| Schema | Schema-on-read | Schema enforcement |
| Consistency | Eventual | Strong consistency |
| Cost | High | Lower (commodity storage) |

### Lakehouse Key Components

```python
# Databricks Lakehouse Architecture

# 1. Storage Layer - Cloud Object Storage (ADLS, S3, GCS)
# - Cost-effective, scalable
# - Stores data in open formats (Parquet, Delta)

# 2. Compute Layer - Databricks Clusters
# - Elastic, auto-scaling compute
# - Separate from storage
# - Supports multiple languages (Python, SQL, Scala, R)

# 3. Abstraction Layer - Unity Catalog
# - Unified governance
# - Lineage tracking
# - Access control

# 4. Workload Layer
# - Data Engineering (ETL/ELT)
# - SQL Analytics
# - Machine Learning
# - Real-time Analytics
```

---

## 2. Databricks Architecture & Compute

### 📖 What is Databricks?

**Azure Databricks** is a fully managed, cloud-based analytics platform built on Apache Spark. It provides:

- **Unified workspace**: Collaborative notebooks for data scientists and engineers
- **Elastic clusters**: Auto-scaling compute resources
- **Integrated security**: Azure AD integration and role-based access control
- **Delta Lake**: ACID transactions on object storage
- **MLflow**: End-to-end ML lifecycle management

**Why is this important for Data Engineering?**
- Fast cluster provisioning and auto-scaling
- Built-in optimizations (Photon, caching)
- Seamless Azure ecosystem integration
- Enterprise-grade security and governance

### Workspace Architecture

```python
# Databricks Workspace Hierarchy

# 1. Workspace (Top-level container)
#    ├── Repos (Git integration)
#    ├── Notebooks
#    ├── Libraries
#    ├── Clusters
#    ├── Jobs
#    └── SQL Warehouses
#
# 2. Unity Catalog (Governance layer)
#    ├── Metastore (Top-level container)
#    │   ├── Catalogs (Top-level namespace)
#    │   │   ├── Schemas (Database)
#    │   │   │   ├── Tables
#    │   │   │   ├── Views
#    │   │   │   └── ML Models
#    │   │   │
#    │   │   └── External Locations
#    │   │
#    │   └── External Connections
```

### Clusters

Clusters provide the compute resources in Databricks. There are two types:

#### All-Purpose Clusters
- Interactive clusters for development
- Shared by multiple users
- Can be terminated manually
- Use for notebooks and Ad-hoc analysis

```python
# Cluster Configuration Example
# - Worker Type: Standard_D4s_v3 (4 cores, 16GB RAM)
# - Driver Type: Same as worker
# - Min Workers: 2
# - Max Workers: 8
# - Auto Scaling: Enabled
# - Spark Version: 12.2 LTS (includes Apache Spark 3.3.2)
# - Photon Acceleration: Enabled
```

#### Job Clusters
- Ephemeral clusters for production jobs
- Created per job run
- More cost-effective for production
- Better isolation and security

```python
# Job Cluster Configuration
# - Created when job starts
# - Terminated when job completes
# - Use for production ETL pipelines
# - More secure (no persistent configuration)
```

### Cluster Architecture

```python
# Spark Cluster Architecture

# Driver Node
# - Coordinates task execution
# - Creates SparkContext
# - Schedules tasks
# - Collects results

# Worker Nodes
# - Execute tasks
# - Store cached data
# - Report status to driver

# Communication
# - Driver <-> Executors via BlockManager
# - Shuffle data between nodes
# - Uses Akka for inter-node communication
```

### Spark Session Configuration

```python
# Creating Spark Session in Databricks
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DataEngineering") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .config("spark.delta.logStore.class", "org.apache.spark.sql.delta.storage.AzureBlobFileLogStore") \
    .getOrCreate()

# View Spark configuration
spark.sparkContext.getConf().getAll()

# Key configurations for Databricks
# - spark.sql.shuffle.partitions: Default 200
# - spark.adaptive.enabled: True (Databricks default)
# - spark.delta.autoCompact.enabled: True
```

---

## 3. Delta Lake Deep Dive

### 📖 What is Delta Lake?

**Delta Lake** is an open-source storage layer that brings ACID transactions to Apache Spark and Big Data workloads. It provides:

- **ACID transactions**: Serializability guarantees
- **Schema enforcement**: Prevents bad data from entering
- **Schema evolution**: Safe schema changes
- **Time travel**: Query historical data
- **Upserts**: MERGE for insert/update
- **Data lineage**: Complete audit trail

**Why is this important for Data Engineering?**
- Reliable data pipelines with transactional guarantees
- Easy rollback capabilities
- Simplified CDC (Change Data Capture) workflows
- Data quality enforcement at write time

### Delta Lake Architecture

```python
# Delta Lake Table Structure

# /delta/table/
# ├── _delta_log/
# │   ├── 00000000000000000000.json
#   ├── 00000000000000000001.json
#   └── ...
# ├── part-00000-c000.snappy.parquet
# ├── part-00001-c000.snappy.parquet
# └── ...

# _delta_log contains:
# - Transaction commit log
# - Schema information
# - Partition information
# - Metadata changes
```

### Creating Delta Tables

```python
# Create Delta Table from DataFrame
df.write.format("delta") \
    .mode("overwrite") \
    .save("/mnt/delta/sales")

# Create Delta Table using SQL
spark.sql("""
    CREATE TABLE sales (
        sale_id INT,
        product_id INT,
        quantity INT,
        sale_date DATE,
        amount DECIMAL(10,2)
    )
    USING DELTA
    LOCATION '/mnt/delta/sales'
""")

# Create Table with Partitioning
df.write.format("delta") \
    .partitionBy("sale_date") \
    .save("/mnt/delta/sales_partitioned")

# Create Table with Z-Ordering
spark.sql("""
    OPTIMIZE sales
    ZORDER BY (sale_date, product_id)
""")
```

### CRUD Operations

```python
# Read Delta Table
df = spark.read.format("delta").load("/mnt/delta/sales")

# Read with Time Travel (version)
df_v1 = spark.read.format("delta").option("versionAsOf", 0).load("/mnt/delta/sales")

# Read with Time Travel (timestamp)
df_timestamp = spark.read.format("delta") \
    .option("timestampAsOf", "2024-01-01") \
    .load("/mnt/delta/sales")

# Append Data
df_new.write.format("delta") \
    .mode("append") \
    .save("/mnt/delta/sales")

# Overwrite Data
df.write.format("delta") \
    .mode("overwrite") \
    .save("/mnt/delta/sales")

# Overwrite with Partition Filter
df.write.format("delta") \
    .mode("overwrite") \
    .partitionOverwriteMode("dynamic") \
    .save("/mnt/delta/sales")
```

### MERGE Operations

```python
# MERGE (Upsert) - Core Delta Lake Feature
from delta.tables import DeltaTable

target_table = DeltaTable.forPath(spark, "/mnt/delta/sales")

# Merge operation
target_table.alias("target").merge(
    source=df_updates.alias("source"),
    condition="target.sale_id = source.sale_id"
).whenMatchedUpdate(
    set={
        "quantity": "source.quantity",
        "amount": "source.amount"
    }
).whenNotMatchedInsert(
    values={
        "sale_id": "source.sale_id",
        "product_id": "source.product_id",
        "quantity": "source.quantity",
        "sale_date": "source.sale_date",
        "amount": "source.amount"
    }
).execute()

# SQL MERGE
spark.sql("""
    MERGE INTO sales target
    USING updates source
    ON target.sale_id = source.sale_id
    WHEN MATCHED THEN
        UPDATE SET quantity = source.quantity, amount = source.amount
    WHEN NOT MATCHED
        INSERT (sale_id, product_id, quantity, sale_date, amount)
        VALUES (source.sale_id, source.product_id, source.quantity, source.sale_date, source.amount)
""")
```

### Schema Evolution

```python
# Schema Enforcement (Automatic)
# Delta Lake automatically enforces schema
# Writing DataFrame with different schema will fail

# Schema Evolution Options
df_new.write.format("delta") \
    .mode("append") \
    .option("mergeSchema", "true") \
    .save("/mnt/delta/sales")

# Or using SQL
spark.sql("""
    ALTER TABLE sales ADD COLUMNS (new_column STRING)
""")

# Schema Evolution with Overwrite
df.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .save("/mnt/delta/sales")
```

### Time Travel & History

```python
# View History
spark.sql("DESCRIBE HISTORY sales").show()

# Output:
# +-------+-------------------+------+--------+-------------------+--------------------+
# |version|          timestamp|userId|userName|              operation| operationParameters|
# +-------+-------------------+------+--------+-------------------+--------------------+
# |      1|2024-01-15 10:30:00|  null|    null|               MERGE|              {mode..}|
# |      0|2024-01-15 10:00:00|  null|    null|          WRITE (mode=Overwrite)| {partitionBy...}|
# +-------+-------------------+------+--------+-------------------+--------------------+

# Restore to Previous Version
spark.sql("RESTORE TABLE sales TO VERSION AS OF 0")

# Vacuum (Clean up old files)
# Default retention is 7 days
spark.sql("VACUUM sales")  # 7 days default
spark.sql("VACUUM sales RETAIN 168 HOURS")  # 7 days explicitly

# Do not vacuum within 7 days (Cassandra)
spark.sql("SET spark.databricks.delta.retentionDurationCheck.enabled = false")
spark.sql("VACUUM sales RETAIN 0 HOURS")
```

---

## 4. Data Engineering Patterns

### 📖 Data Engineering on Databricks

Databricks supports multiple data engineering patterns:

- **Batch Processing**: Traditional ETL/ELT
- **Streaming**: Real-time data processing with Structured Streaming
- **Incremental**: Change Data Capture (CDC)
- **Medallion Architecture**: Quality progression layers (Bronze, Silver, Gold)

**Why is this important for Data Engineering?**
- Build scalable, maintainable data pipelines
- Support both batch and real-time use cases
- Implement data quality gates
- Enable incremental processing for efficiency

### Medallion Architecture

```python
# Medallion Architecture Pattern

# BRONZE (Raw Layer)
# - Raw ingestion from source systems
# - Schema-on-read approach
# - Preserves original data
# - Full history retained

# SILVER (Cleansed Layer)
# - Cleaned and standardized
# - Deduplicated
# - Enriched
# - Business rules applied
# - Quality validated

# GOLD (Curated Layer)
# - Business-level aggregates
# - Star schema dimensions
# - Ready for BI/Analytics
# - Performance optimized
```

### Bronze Layer - Raw Data Ingestion

```python
# Bronze: Raw Ingestion
# Auto Loader for incremental file ingestion

(spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.schemaLocation", "/mnt/delta/bronze/schema")
    .load("/mnt/source/raw_data")
    .writeStream
    .format("delta")
    .option("checkpointLocation", "/mnt/delta/bronze/checkpoint")
    .table("bronze_sales_raw"))

# Manual approach for batch ingestion
df = spark.read.format("csv") \
    .option("header", "true") \
    .load("/mnt/source/sales/*.csv")

df.write.format("delta") \
    .mode("append") \
    .partitionBy("ingestion_date") \
    .save("/mnt/delta/bronze/sales")
```

### Silver Layer - Data Cleansing

```python
# Silver: Clean and Transform

# Read from Bronze
bronze_df = spark.read.format("delta").table("bronze_sales_raw")

# Clean and transform
silver_df = (bronze_df
    # Remove duplicates
    .dropDuplicates(["sale_id"])
    # Handle nulls
    .fillna({"quantity": 0, "amount": 0})
    # Add derived columns
    .withColumn("year", year("sale_date"))
    .withColumn("month", month("sale_date"))
    .withColumn("revenue_category",
        when(col("amount") > 1000, "high")
        .when(col("amount") > 100, "medium")
        .otherwise("low"))
    # Data type conversions
    .withColumn("sale_id", col("sale_id").cast("int"))
    .withColumn("amount", col("amount").cast("decimal(10,2))")
    # Filter invalid records
    .filter(col("quantity") > 0))

# Write to Silver
silver_df.write.format("delta") \
    .mode("overwrite") \
    .partitionBy("year", "month") \
    .save("/mnt/delta/silver/sales")

# Using Auto Loader with Schema Hints
(spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schema", "sale_id INT, product_id INT, quantity INT, sale_date STRING")
    .load("/mnt/source/sales")
    .writeStream
    .format("delta")
    .option("checkpointLocation", "/mnt/delta/silver/checkpoint")
    .table("silver_sales"))
```

### Gold Layer - Business Aggregates

```python
# Gold: Business-Level Aggregates

# Read from Silver
silver_df = spark.read.format("delta").table("silver_sales")

# Sales Summary by Product
product_summary = (silver_df
    .groupBy("product_id", "year", "month")
    .agg(
        sum("amount").alias("total_revenue"),
        count("sale_id").alias("transaction_count"),
        avg("amount").alias("avg_transaction"),
        max("amount").alias("max_transaction"),
        min("amount").alias("min_transaction")
    )
    .orderBy("year", "month", "product_id"))

# Sales Summary by Customer
customer_summary = (silver_df
    .groupBy("customer_id", "year")
    .agg(
        sum("amount").alias("total_spent"),
        count("sale_id").alias("order_count"),
        countDistinct("product_id").alias("unique_products")
    )
    .filter(col("total_spent") > 1000))

# Write to Gold
product_summary.write.format("delta") \
    .mode("overwrite") \
    .save("/mnt/delta/gold/product_summary")

customer_summary.write.format("delta") \
    .mode("overwrite") \
    .save("/mnt/delta/gold/customer_summary")

# Create Gold Tables
spark.sql("""
    CREATE TABLE IF NOT EXISTS gold_product_summary
    USING DELTA
    LOCATION '/mnt/delta/gold/product_summary'
""")
```

### Structured Streaming

```python
# Structured Streaming Basics

# Read from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker:9092") \
    .option("subscribe", "sales_topic") \
    .option("startingOffsets", "latest") \
    .load()

# Parse JSON
from pyspark.sql.functions import from_json, col

schema = "sale_id INT, product_id INT, quantity INT, amount DECIMAL(10,2), timestamp TIMESTAMP"
parsed_df = kafka_df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Write to Delta with Streaming
stream_query = (parsed_df
    .writeStream
    .format("delta")
    .option("checkpointLocation", "/mnt/delta/checkpoints/sales")
    .outputMode("append")
    .start("/mnt/delta/sales_stream"))

# Windowed Aggregations
from pyspark.sql.functions import window, sum as spark_sum

windowed_sales = (parsed_df
    .groupBy(
        window("timestamp", "5 minutes"),
        "product_id"
    )
    .agg(
        spark_sum("amount").alias("total_amount"),
        count("sale_id").alias("transaction_count")
    ))

# Write windowed aggregation
(windowed_sales
    .writeStream
    .format("delta")
    .option("checkpointLocation", "/mnt/delta/checkpoints/windowed")
    .outputMode("complete")
    .start("/mnt/delta/sales_windowed"))

# Streaming Joins
# Join stream with static reference data
product_df = spark.read.format("delta").load("/mnt/delta/products")

enriched_stream = parsed_df.join(product_df, "product_id")
```

### Auto Loader

```python
# Auto Loader - Cloud File Ingestion

# Automatic schema inference and evolution
(spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.schemaLocation", "/mnt/delta/schema/inference")
    .option("cloudFiles.schemaEvolutionMode", "addNewColumns")
    .load("/mnt/source/incoming/data")
    .writeStream
    .format("delta")
    .option("checkpointLocation", "/mnt/delta/checkpoints/auto_loader")
    .table("raw_ingested_data"))

# Processing Options
# - addNewColumns: Add new columns discovered
# - failOnNewColumns: Fail if new columns found
# - none: Ignore new columns

# Auto Loader with SQL
CREATE STREAMING TABLE raw_data
AS SELECT * FROM cloud_files("/mnt/source/data", "json",
    schema => "sale_id INT, product_id STRING, quantity INT",
    schemaLocation => "/mnt/delta/schema")
```

---

## 5. Unity Catalog & Governance

### 📖 What is Unity Catalog?

**Unity Catalog** is Databricks' unified governance solution that provides:

- **Centralized access control**: Manage permissions across all workspaces
- **Data lineage**: Track data flow from source to consumption
- **Auditing**: Complete audit logs for compliance
- **Data discovery**: Browse and search data assets
- **Fine-grained security**: Column-level and row-level security

**Why is this important for Data Engineering?**
- Enterprise-grade security and compliance
- Centralized data governance across organization
- Data lineage for impact analysis
- Simplified access management

### Unity Catalog Hierarchy

```python
# Unity Catalog Object Hierarchy

# Metastore (Top-level container)
# - Owned by cloud account
# - Contains all catalogs
# - Manages storage credentials
#
# ├── Catalogs (Top-level namespace)
# │   ├── Production
# │   ├── Sandbox
# │   └── Staging
# │
# │   ├── Schemas (Database)
# │   │   ├── sales
# │   │   ├── marketing
# │   │   └── finance
# │   │
# │   │   ├── Tables
# │   │   │   ├── Managed (stored in Unity)
# │   │   │   └── External (in customer storage)
# │   │   │
# │   │   ├── Views
# │   │   ├── ML Models
# │   │   └── Functions
# │
# │   ├── External Locations
# │   │   └── S3/ADLS mount points
# │
# │   └── Connections
# │       └── Database connections
```

### Managing Catalogs and Schemas

```python
# Create Catalog
spark.sql("""
    CREATE CATALOG IF NOT EXISTS production
    COMMENT 'Production data catalog'
""")

# Create Schema
spark.sql("""
    CREATE SCHEMA IF NOT EXISTS production.sales
    COMMENT 'Sales data schema'
""")

# Set current catalog/schema
spark.sql("USE CATALOG production")
spark.sql("USE SCHEMA sales")

# Show objects
spark.sql("SHOW CATALOGS")
spark.sql("SHOW SCHEMAS")
spark.sql("SHOW TABLES")
spark.sql("SHOW VIEWS")
```

### Access Control

```python
# Grant Permissions

# Grant catalog access
GRANT USE CATALOG ON CATALOG production TO `user@company.com`
GRANT CREATE SCHEMA ON CATALOG production TO `user@company.com`

# Grant schema access
GRANT USE SCHEMA ON SCHEMA production.sales TO `user@company.com`
GRANT CREATE TABLE ON SCHEMA production.sales TO `user@company.com`

# Grant table access
GRANT SELECT ON TABLE production.sales.sales_table TO `user@company.com`
GRANT MODIFY ON TABLE production.sales.sales_table TO `user@company.com`

# Grant to group
GRANT SELECT ON TABLE production.sales.sales_table TO `analysts_group`

# Row-level security
# Create a function for row filtering
spark.sql("""
    CREATE FUNCTION filter_by_region(region STRING)
    RETURN CASE
        WHEN IS_MEMBER('sales_lead') THEN 'East'
        ELSE 'No Access'
    END
""")

# Apply row-level security
spark.sql("""
    CREATE TABLE sales_filtered
    AS SELECT * FROM sales
    WHERE region = filter_by_region(current_user())
""")
```

### Data Lineage

```python
# Automatic Lineage Tracking

# Unity Catalog automatically tracks lineage for:
# - CTAS (CREATE TABLE AS SELECT)
# - INSERT INTO
# - CREATE VIEW
# - MERGE operations
# - Stream operations

# View lineage
spark.sql("""
    SELECT * FROM system.information_schema.lineage
    WHERE table_name = 'gold_sales'
""")

# Lineage output example:
# +-------------+-------------+------------------+------------------+
# |   upstream   | downstream  |    upstream_id   |   downstream_id  |
# +-------------+-------------+------------------+------------------+
# | silver_sales| gold_sales  | table:silver.s..| table:gold.sales |
# | bronze_sales| silver_sales| table:bronze... | table:silver...  |
# +-------------+-------------+------------------+------------------+
```

### External Locations and Storage

```python
# Create Storage Credential
spark.sql("""
    CREATE STORAGE CREDENTIAL IF NOT EXISTS adls_credential
    AZURE SERVICE PRINCIPAL '<client-id>'
    AZURE TENANT '<tenant-id>'
""")

# Create External Location
spark.sql("""
    CREATE EXTERNAL LOCATION IF NOT EXISTS landing_zone
    URL 'abfss://landing@storageaccount.dfs.core.windows.net/'
    STORAGE CREDENTIAL adls_credential
""")

# Create External Table
spark.sql("""
    CREATE TABLE external_sales
    (sale_id INT, product_id INT, amount DECIMAL(10,2))
    USING DELTA
    LOCATION 'abfss://landing@storageaccount.dfs.core.windows.net/sales'
""")
```

---

## 6. Performance Optimization

### 📖 Performance in Databricks

Performance optimization in Databricks involves:

- **Cluster sizing**: Right-sizing compute resources
- **Data partitioning**: Partition strategy for parallelism
- **File sizing**: Optimal parquet file sizes
- **Caching**: In-memory caching strategies
- **Query optimization**: Spark optimizations

**Why is this important for Data Engineering?**
- Reduce processing costs
- Faster pipeline execution
- Better resource utilization
- Improved user experience

### Cluster Sizing

```python
# Cluster Sizing Guidelines

# General Guidelines
# - Small data (< 100GB): Single node cluster
# - Medium data (100GB - 1TB): 3-10 nodes
# - Large data (> 1TB): 10+ nodes, partitioned

# Node Types (Azure)
# - General Purpose: Dds_v4 (balanced)
# - Memory Optimized: Es_v4 (memory-intensive)
# - Compute Optimized: Fs_v2 (compute-intensive)

# Sizing Formula
# Workers = (Data Size / (Partition Size * Compression Factor))
# Example: 1TB / (128MB * 0.7) ≈ 11,000 partitions (too many!)
# Recommendation: 200-400 partitions for typical workloads
```

### Partitioning Strategies

```python
# Partition by Date (Temporal Data)
df.write.format("delta") \
    .partitionBy("year", "month", "day") \
    .save("/mnt/delta/table")

# Partition by Category (High Cardinality)
# Use only for columns with < 1000 unique values
df.write.format("delta") \
    .partitionBy("region") \
    .save("/mnt/delta/table")

# Partition Pruning
# Spark automatically reads only relevant partitions
df_filtered = spark.read.format("delta") \
    .load("/mnt/delta/table")

# Filter on partition column (prunes partitions)
result = df_filtered.filter("year = 2024 AND month = 1")

# Multiple partition columns - order matters!
# Put high-cardinality columns last
# .partitionBy("year", "region", "product_id")
# year: low cardinality → 5 values
# region: medium cardinality → 10 values
# product_id: high cardinality → 10000 values
```

### Delta Lake Optimizations

```python
# OPTIMIZE - File Compaction
spark.sql("OPTIMIZE delta_table")

# OPTIMIZE with Z-Ordering
# Z-Order reorders data to improve data skipping
spark.sql("OPTIMIZE delta_table ZORDER BY (date, region)")

# OPTIMIZE for Partition
spark.sql("OPTIMIZE delta_table WHERE year = 2024")

# Auto Compaction (Automatic)
spark.sql("SET spark.databricks.delta.autoCompact.enabled = true")

# Small File Merging
spark.sql("SET spark.databricks.delta.optimize.minFileSize = 128")  # MB

# Data Skipping Statistics
# Automatically collected by Delta Lake
# Improves filter performance
spark.sql("SET spark.databricks.delta.stats.skipping = true")
```

### Caching Strategies

```python
# Caching in Databricks

# Cache DataFrame
df.cache()  # Persists in memory
df.persist(StorageLevel.DISK_ONLY)  # Persists to disk

# Check cache
spark.catalog.isCached("tableName")
spark.catalog.cacheTable("tableName")

# Uncache
df.unpersist()
spark.catalog.uncacheTable("tableName")

# Delta Cache (Photon)
# Automatically caches frequently accessed data
# Enabled by default on DBFS

# Display cached data
spark.catalog.listTables()
spark.sql("CLEAR CACHE")

# Caching Best Practices
# - Cache intermediate results used multiple times
# - Don't cache data that will be filtered heavily
# - Uncache when done to free memory
```

### Spark Configuration Tuning

```python
# Key Spark Configurations

# Shuffle Partitions
spark.conf.set("spark.sql.shuffle.partitions", "200")

# Adaptive Query Execution (AQE)
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")

# Broadcast Join Threshold
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "100MB")  # Default: 10MB
spark.conf.set("spark.sql.broadcastTimeout", "600")  # seconds

# Memory Management
spark.conf.set("spark.memory.fraction", "0.6")  # Default: 0.6
spark.conf.set("spark.memory.storageFraction", "0.5")  # Default: 0.5

# File Sizing
spark.conf.set("spark.sql.files.maxPartitionBytes", "128MB")  # Default: 128MB
spark.conf.set("spark.sql.parquet.compression.codec", "snappy")

# Streaming
spark.conf.set("spark.sql.streaming.checkpointRetention", "7 days")
```

### Performance Monitoring

```python
# Using Spark UI in Databricks

# Access Spark UI
# Click "Spark UI" in Databricks notebook or cluster details

# Key Metrics to Monitor
# - DAG Visualization: Task execution plan
# - SQL Tab: Query execution details
# - Stages: Task stage information
# - Storage: Cached data and RDDs
# - Executors: Resource utilization

# Using Explain
df.explain(True)  # Detailed execution plan

# Using Observability
from pyspark.sql.functions import col, count, sum as spark_sum

# Slow query analysis
spark.sql("SET spark.sql.explain.extended=true")
spark.sql("SELECT * FROM table").explain()

# Databricks Metrics
# - Query duration
# - Data processed
# - Cluster utilization
```

---

## 7. Quick Reference

### Common Spark DataFrame Operations

| Operation | Code |
|-----------|------|
| Read Delta | `spark.read.format("delta").load("path")` |
| Write Delta | `df.write.format("delta").save("path")` |
| Create Temp View | `df.createOrReplaceTempView("name")` |
| Show Schema | `df.printSchema()` |
| Show Execution Plan | `df.explain()` |
| Count Rows | `df.count()` |
| Select Columns | `df.select("col1", "col2")` |
| Filter | `df.filter(condition)` |
| Group By | `df.groupBy("col").agg(...)` |
| Join | `df1.join(df2, condition)` |
| Union | `df1.union(df2)` |

### Delta Lake Commands

| Command | SQL |
|---------|-----|
| View History | `DESCRIBE HISTORY table_name` |
| Time Travel | `SELECT * FROM table VERSION AS OF 0` |
| Restore | `RESTORE TABLE table TO VERSION AS OF 0` |
| Vacuum | `VACUUM table RETAIN 168 HOURS` |
| Optimize | `OPTIMIZE table ZORDER BY (col1, col2)` |
| Merge | `MERGE INTO target USING source ON condition...` |

### Unity Catalog Commands

| Command | Description |
|---------|-------------|
| `SHOW CATALOGS` | List all catalogs |
| `SHOW SCHEMAS` | List schemas in current catalog |
| `SHOW TABLES` | List tables in current schema |
| `DESCRIBE EXTENDED table_name` | Show table metadata |
| `GRANT SELECT ON TABLE ... TO ...` | Grant permissions |
| `SHOW GRANTS ON TABLE ...` | Show current permissions |

### Best Practices Summary

1. **Data Organization**
   - Use medallion architecture (Bronze/Silver/Gold)
   - Partition by temporal columns
   - Use appropriate file sizes (128MB-1GB)

2. **Performance**
   - Enable Adaptive Query Execution
   - Use broadcast joins for small tables
   - Optimize and vacuum regularly
   - Cache wisely

3. **Governance**
   - Use Unity Catalog for access control
   - Enable data lineage tracking
   - Implement proper naming conventions
   - Document data assets

4. **Cost Optimization**
   - Use job clusters for production
   - Enable auto-scaling
   - Terminate idle clusters
   - Use spot instances

---

**Happy Learning! Remember: Practice makes perfect.**
