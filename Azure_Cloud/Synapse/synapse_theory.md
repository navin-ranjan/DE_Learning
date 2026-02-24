# Azure Synapse Theory & Tutorial

This file follows `README.md` and provides comprehensive theory explanations with practical examples for Azure Synapse Analytics.

## Table of Contents

1. [Platform Fundamentals](#1-platform-fundamentals)
2. [MPP Architecture Deep Dive](#2-mpp-architecture-deep-dive)
3. [Dedicated SQL Pool](#3-dedicated-sql-pool)
4. [Serverless SQL Pool](#4-serverless-sql-pool)
5. [Spark Pool in Synapse](#5-spark-pool-in-synapse)
6. [Data Integration & Pipelines](#6-data-integration--pipelines)
7. [Security & Governance](#7-security--governance)
8. [Performance Optimization](#8-performance-optimization)
9. [Quick Reference](#9-quick-reference)

---

## 1. Platform Fundamentals

### 📖 What is Azure Synapse Analytics?

**Azure Synapse Analytics** is an enterprise analytics service that accelerates time-to-insight across data warehouses and big data systems. It combines:

- **SQL Analytics**: Enterprise data warehousing (dedicated and serverless)
- **Spark Analytics**: Big data processing and ML
- **Data Integration**: Pipelines for ETL/ELT
- **Studio**: Unified workspace for development and monitoring

**Key Capabilities:**
- Unified workspace for data engineering and analytics
- Query files directly in data lake without loading
- Build modern data warehouse with petabyte scale
- Integrate SQL and Spark seamlessly

**Why is this important for Data Engineering?**
- Single platform for all analytics workloads
- Cost-effective with serverless options
- Seamless integration with Azure ecosystem
- Enterprise-grade security and governance

### Synapse Architecture Overview

```sql
-- Synapse Workspace Architecture

/*
┌─────────────────────────────────────────────────────────────┐
│                    Synapse Workspace                        │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │   Synapse    │  │   Synapse    │  │  Synapse        │  │
│  │   SQL Pool   │  │   Spark Pool │  │  Pipelines      │  │
│  │  (Dedicated) │  │              │  │                 │  │
│  └──────────────┘  └──────────────┘  └─────────────────┘  │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │ Serverless   │  │    Studio    │  │  Linked         │  │
│  │    SQL       │  │   (Web UI)   │  │  Services       │  │
│  └──────────────┘  └──────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              Azure Data Lake Storage Gen2                   │
│                    (ADLS Gen2)                               │
└─────────────────────────────────────────────────────────────┘
*/
```

### Synapse vs Traditional Data Warehouses

| Aspect | Traditional DW | Azure Synapse |
|--------|---------------|---------------|
| **Architecture** | SMP (Symmetric Multiprocessing) | MPP (Massively Parallel Processing) |
| **Scale** | TB scale | PB scale |
| **Cost Model** | Fixed capacity | Pay-per-query / Provisioned |
| **Data Types** | Structured only | Structured + Semi-structured |
| **Lake Integration** | Separate lake needed | Built-in lake query |
| **Compute/Storage** | Coupled | Decoupled |

### Workspace Components

```sql
-- Synapse Workspace Components

-- 1. SQL Pools
--    ├── Dedicated SQL Pool (formerly SQL DW)
--    │   - Provisioned compute resources
--    │   - Pay for provisioned DWU
--    │   - Best for predictable workloads
--    │
--    └── Serverless SQL Pool
--        - On-demand query execution
--        - Pay per TB processed
--        - Best for ad-hoc analytics

-- 2. Spark Pools
--    - Managed Apache Spark
--    - Auto-scaling
--    - Notebook integration

-- 3. Pipelines
--    - Data movement
--    - Data transformation
--    - Orchestration

-- 4. Studio
--    - Development IDE
--    - Monitoring
--    - Management
```

---

## 2. MPP Architecture Deep Dive

### 📖 What is MPP?

**Massively Parallel Processing (MPP)** is a distributed computing architecture where:

- Data is distributed across multiple compute nodes
- Each node processes its portion of data in parallel
- Results are aggregated at the control node
- Enables handling of massive datasets

**Key Components:**
- **Control Node**: Receives queries, optimizes, creates execution plan
- **Compute Nodes**: Execute parallel portions of query
- **Data Distribution**: How data is partitioned across nodes
- **Data Movement**: shuffling data between nodes when needed

**Why is this important for Data Engineering?**
- Understand data distribution for query performance
- Design tables to minimize data movement
- Choose appropriate distribution strategies

### Control Node

```sql
-- Control Node Responsibilities

-- 1. Query Reception
--    - Receives T-SQL queries
--    - Validates syntax and permissions

-- 2. Query Optimization
--    - Creates optimized execution plan
--    - Determines parallel execution strategy

-- 3. Query Coordination
--    - Distributes work to compute nodes
--    - Collects and aggregates results

-- 4. Session Management
--    - Manages connections
--    - Enforces security
```

### Compute Nodes

```sql
-- Compute Node Architecture

-- Each compute node:
-- 1. Has local storage (or uses remote storage)
-- 2. Processes its portion of data independently
-- 3. Can communicate with other compute nodes
-- 4. Reports status to control node

-- Distribution Types on Compute Nodes:
-- - Hash Distribution: Deterministic assignment based on column
-- - Round-Robin: Random distribution
-- - Replicate: Full copy on each node
```

### Distribution Strategies

```sql
-- Distribution Strategy Examples

-- 1. Hash Distribution
--    - Good for: Joining large tables on same key
--    - Example: Distribute fact tables on foreign key

CREATE TABLE FactSales
(
    SaleKey BIGINT NOT NULL,
    ProductKey INT NOT NULL,
    CustomerKey INT NOT NULL,
    SaleDate DATETIME NOT NULL,
    SalesAmount DECIMAL(10,2)
)
WITH
(
    DISTRIBUTION = HASH(ProductKey),
    CLUSTERED COLUMNSTORE INDEX
);

-- 2. Round-Robin Distribution
--    - Good for: Staging tables, small dimensions
--    - Even distribution, no skew

CREATE TABLE StagingData
(
    ID INT NOT NULL,
    Data VARCHAR(1000)
)
WITH
(
    DISTRIBUTION = ROUND_ROBIN,
    HEAP
);

-- 3. Replicated Tables
--    - Good for: Small lookup tables
--    - Full copy on each compute node

CREATE TABLE DimProduct
(
    ProductKey INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50)
)
WITH
(
    DISTRIBUTION = REPLICATE
);
```

### Data Movement

```sql
-- Data Movement Operations

-- Shuffle Move
-- Occurs when joining tables on different distribution columns

-- Broadcast Move
-- Small table is broadcast to all nodes for join

-- Movement Minimization Tips:
-- 1. Co-locate fact and dimension tables on same key
-- 2. Use replicated tables for small dimensions
-- 3. Avoid distributions on high-skew columns

-- Example: Optimal Join Design
-- Fact table distributed on ProductKey
-- DimProduct replicated on all nodes
-- Join requires no data movement!
```

---

## 3. Dedicated SQL Pool

### 📖 What is Dedicated SQL Pool?

**Dedicated SQL Pool** (formerly SQL Data Warehouse) provides:

- Enterprise-grade data warehousing
- Massively Parallel Processing (MPP)
- Petabyte-scale storage
- Automated optimization

**Key Features:**
- Columnar storage (columnstore)
- Intelligent workload management
- PolyBase for data loading
- T-SQL compatibility

**Why is this important for Data Engineering?**
- Build modern data warehouse
- Handle PB-scale analytical workloads
- Leverage familiar T-SQL syntax

### Table Types and Indexes

```sql
-- Table Types in Dedicated SQL Pool

-- 1. Clustered Columnstore Index (Default)
--    - Best for: Large tables (1M+ rows)
--    - Compression ratio: 10x
--    - Query performance: Excellent

CREATE TABLE Sales
(
    SaleKey BIGINT NOT NULL,
    ProductKey INT NOT NULL,
    SaleDate DATETIME,
    SalesAmount DECIMAL(10,2)
)
WITH
(
    CLUSTERED COLUMNSTORE INDEX,
    DISTRIBUTION = HASH(SaleKey),
    PARTITION (SaleDate RANGE RIGHT FOR VALUES ('2024-01-01', '2024-02-01', '2024-03-01'))
);

-- 2. Heap Tables
--    - Best for: Staging, small tables
--    - No index overhead
--    - Fast inserts

CREATE TABLE StagingTable
(
    ID INT,
    Data VARCHAR(500)
)
WITH
(
    HEAP,
    DISTRIBUTION = ROUND_ROBIN
);

-- 3. Clustered Index
--    - Best for: Point queries
--    - Ordered storage

CREATE TABLE DimDate
(
    DateKey INT PRIMARY KEY,
    Date DATE,
    Year INT,
    Month INT,
    Day INT
)
WITH
(
    CLUSTERED INDEX (DateKey)
);
```

### Partitioning

```sql
-- Table Partitioning

-- Benefits:
-- 1. Partition pruning (query only relevant partitions)
-- 2. Efficient data loading
-- 3. Easy data archival

CREATE TABLE FactSales
(
    SaleKey BIGINT NOT NULL,
    SaleDate DATETIME NOT NULL,
    ProductKey INT NOT NULL,
    CustomerKey INT NOT NULL,
    SalesAmount DECIMAL(10,2)
)
WITH
(
    CLUSTERED COLUMNSTORE INDEX,
    DISTRIBUTION = HASH(ProductKey),
    PARTITION (SaleDate RANGE RIGHT FOR VALUES
        ('2024-01-01'), ('2024-02-01'), ('2024-03-01'),
        ('2024-04-01'), ('2024-05-01'), ('2024-06-01'),
        ('2024-07-01'), ('2024-08-01'), ('2024-09-01'),
        ('2024-10-01'), ('2024-11-01'), ('2024-12-01'))
);

-- Partition Switching
-- Fast metadata-only operation
ALTER TABLE FactSales SWITCH PARTITION 1 TO FactSalesArchive;
ALTER TABLE FactSalesArchive SWITCH TO FactSales PARTITION 12;

-- Query with Partition Pruning
SELECT * FROM FactSales
WHERE SaleDate >= '2024-01-01' AND SaleDate < '2024-02-01';
```

### Data Loading

```sql
-- Loading Data into Synapse

-- Method 1: COPY Statement (Preferred)
COPY INTO Sales
FROM 'https://mystorageaccount.dfs.core.windows.net/data/sales/'
WITH (
    FILE_TYPE = 'PARQUET',
    CREDENTIAL = (IDENTITY = 'Managed Identity'),
    HEADER = TRUE
);

-- Method 2: PolyBase (Legacy)
CREATE EXTERNAL DATA SOURCE MyDataLake
WITH (
    TYPE = HADOOP,
    LOCATION = 'abfss://container@storage.dfs.core.windows.net'
);

CREATE EXTERNAL TABLE StagingSales
(
    SaleKey BIGINT,
    ProductKey INT,
    SaleDate DATETIME,
    SalesAmount DECIMAL(10,2)
)
WITH
(
    DATA_SOURCE = MyDataLake,
    LOCATION = '/data/sales/',
    FILE_FORMAT = ParquetFile
);

-- Insert into managed table
INSERT INTO FactSales
SELECT * FROM StagingSales;

-- Method 3: CTAS (Create Table As Select)
CREATE TABLE FactSales
WITH
(
    CLUSTERED COLUMNSTORE INDEX,
    DISTRIBUTION = HASH(ProductKey)
)
AS
SELECT
    CAST(SaleKey AS BIGINT) AS SaleKey,
    CAST(ProductKey AS INT) AS ProductKey,
    CAST(SaleDate AS DATETIME) AS SaleDate,
    CAST(SalesAmount AS DECIMAL(10,2)) AS SalesAmount
FROM StagingSales
WHERE SaleDate >= '2024-01-01';

-- Method 4: CETAS (Create External Table As Select)
CREATE EXTERNAL TABLE SalesExport
WITH
(
    LOCATION = '/export/sales/',
    DATA_SOURCE = MyDataLake,
    FILE_FORMAT = ParquetFile
)
AS
SELECT * FROM FactSales WHERE SaleDate >= '2024-01-01';
```

### Materialized Views

```sql
-- Materialized Views

-- Pre-computed and stored results
-- Automatically maintained
-- Use for expensive aggregations

CREATE MATERIALIZED VIEW SalesSummary
WITH
(
    DISTRIBUTION = HASH(ProductKey)
)
AS
SELECT
    ProductKey,
    YEAR(SaleDate) AS Year,
    MONTH(SaleDate) AS Month,
    COUNT(*) AS TransactionCount,
    SUM(SalesAmount) AS TotalSales,
    AVG(SalesAmount) AS AvgSales
FROM FactSales
GROUP BY ProductKey, YEAR(SaleDate), MONTH(SaleDate);

-- Query automatically uses materialized view
SELECT ProductKey, Year, TotalSales
FROM SalesSummary
WHERE Year = 2024;

-- Refresh materialized view
ALTER MATERIALIZED VIEW SalesSummary REBUILD;
```

---

## 4. Serverless SQL Pool

### 📖 What is Serverless SQL Pool?

**Serverless SQL Pool** provides:

- On-demand SQL queries over data lake
- No infrastructure to manage
- Pay per TB processed
- Instant scalability

**Key Features:**
- Query Parquet, CSV, JSON directly
- No data movement
- Automatic scaling
- T-SQL surface area

**Why is this important for Data Engineering?**
- Explore data without loading
- Ad-hoc analytics on lake data
- Cost-effective for sporadic workloads

### Querying Files Directly

```sql
-- OPENROWSET Function

-- Query Parquet file
SELECT TOP 100 *
FROM OPENROWSET(
    BULK 'https://mystorage.dfs.core.windows.net/data/sales/*.parquet',
    FORMAT = 'PARQUET'
) AS rows;

-- Query CSV with header
SELECT *
FROM OPENROWSET(
    BULK 'https://mystorage.dfs.core.windows.net/data/sales.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    FIRSTROW = 1
)
WITH (
    SaleKey INT,
    ProductKey INT,
    SaleDate DATETIME,
    SalesAmount DECIMAL(10,2)
) AS rows;

-- Query JSON
SELECT *
FROM OPENROWSET(
    BULK 'https://mystorage.dfs.core.windows.net/data/events.json',
    FORMAT = 'JSON'
) AS rows;

-- Use folder paths and wildcards
SELECT *
FROM OPENROWSET(
    BULK 'https://mystorage.dfs.core.windows.net/data/year=2024/month=*/*.parquet',
    FORMAT = 'PARQUET'
) AS rows;
```

### External Tables in Serverless

```sql
-- External Tables (Serverless)

-- Create database scoped credential
CREATE DATABASE SCOPED CREDENTIAL StorageCred
WITH
    IDENTITY = 'Managed Identity';

-- Create external data source
CREATE EXTERNAL DATA SOURCE DataLake
WITH
(
    LOCATION = 'https://mystorage.dfs.core.windows.net/data/',
    CREDENTIAL = StorageCred
);

-- Create external file format
CREATE EXTERNAL FILE FORMAT ParquetFile
WITH (
    FORMAT_TYPE = PARQUET
);

-- Create external table
CREATE EXTERNAL TABLE Sales
(
    SaleKey BIGINT,
    ProductKey INT,
    SaleDate DATETIME,
    SalesAmount DECIMAL(10,2)
)
WITH
(
    LOCATION = 'sales/',
    DATA_SOURCE = DataLake,
    FILE_FORMAT = ParquetFile
);

-- Query external table
SELECT ProductKey, SUM(SalesAmount) AS TotalSales
FROM Sales
WHERE YEAR(SaleDate) = 2024
GROUP BY ProductKey;
```

### Serverless vs Dedicated

```sql
-- Choosing Between Serverless and Dedicated

-- Use Serverless When:
-- - Ad-hoc queries on data lake
-- - Unpredictable query patterns
-- - Data exploration and discovery
-- - Small to medium workloads

-- Use Dedicated When:
-- - Predictable, recurring workloads
-- - Large data volumes (TB+)
-- - Need for best query performance
-- - Heavy concurrent workloads

-- Cost Comparison Example
-- Serverless: $5 per TB processed
-- Dedicated: $500 per DWU/month

-- Example Workload Analysis
/*
Workload: 10TB data, 50 queries/day
- Serverless: 10TB * 50 * $5 = $2,500/month
- Dedicated (DW1000c): ~$3,000/month

Workload: 1TB data, 5 queries/day
- Serverless: 1TB * 5 * $5 = $25/month
- Dedicated: Minimum DW100c = ~$300/month
*/
```

---

## 5. Spark Pool in Synapse

### 📖 What is Spark Pool?

**Spark Pool** provides:

- Managed Apache Spark
- Auto-scaling compute
- Notebook integration
- Delta Lake support

**Key Features:**
- Node types: Compute optimized, Memory optimized
- Auto-pause (cost savings)
- Auto-scale
- Library management

**Why is this important for Data Engineering?**
- Big data processing
- Machine learning
- Complex transformations
- Delta Lake operations

### Spark Pool Configuration

```python
# Spark Pool Configuration in Synapse

# Pool Settings:
# - Node size: Small (4 vCPU), Medium (8 vCPU), Large (16 vCPU)
# - Auto-scaling: Yes/No
# - Min nodes: 3
# - Max nodes: 10
# - Auto-pause: Enabled after 15 min

# Spark Configuration Example
spark.conf.set("spark.sql.shuffle.partitions", "200")
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.delta.enabled", "true")

# Reading from Synapse
# Using Spark to read from Dedicated SQL Pool
df = spark.read \
    .format("com.databricks.spark.sqldw") \
    .option("url", "jdbc:sqlserver://synapse.sql.azuresynapse.net:1433;database=myDB") \
    .option("tempDir", "abfss://temp@storage.dfs.core.windows.net/temp") \
    .option("forwardSparkAzureStorageCredentials", "true") \
    .option("dbTable", "dbo.MyTable") \
    .load()
```

### Delta Lake with Spark

```python
# Delta Lake in Synapse Spark

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Write to Delta Lake
df.write.format("delta") \
    .mode("overwrite") \
    .partitionBy("year", "month") \
    .save("abfss://lake@storage.dfs.core.windows.net/delta/sales")

# Read from Delta
df = spark.read.format("delta").load("abfss://lake@storage.dfs.core.windows.net/delta/sales")

# Time Travel
df_old = spark.read.format("delta").option("versionAsOf", 0).load("path")

# MERGE Operation
from delta.tables import DeltaTable

deltaTable = DeltaTable.forPath(spark, "path/to/table")

deltaTable.upsert(
    df_updates,
    "target.id = source.id"
)

# Optimize
spark.sql("OPTIMIZE delta.`path/to/table` ZORDER BY (date)")
```

---

## 6. Data Integration & Pipelines

### 📖 What is Data Integration?

Synapse Pipelines provide:

- Visual ETL/ELT
- 90+ connectors
- Data flows
- Triggers and scheduling

**Key Components:**
- Pipeline: Orchestration container
- Activity: Single operation
- Dataset: Data structure
- Linked Service: Connection info
- Trigger: Execution schedule

**Why is this important for Data Engineering?**
- Ingest data from multiple sources
- Transform data at scale
- Orchestrate complex workflows

### Copy Activity

```json
{
    "name": "CopySalesData",
    "type": "Copy",
    "inputs": [{
        "referenceName": "SourceDataset",
        "type": "DatasetReference"
    }],
    "outputs": [{
        "referenceName": "TargetDataset",
        "type": "DatasetReference"
    }],
    "typeProperties": {
        "source": {
            "type": "ParquetSource"
        },
        "sink": {
            "type": "SqlSink",
            "writeBatchSize": 10000,
            "writeBatchTimeout": "00:10:00"
        },
        "enableStaging": true,
        "stagingSettings": {
            "linkedServiceName": "StagingStorage"
        }
    }
}
```

### Data Flows

```json
{
    "name": "TransformSalesData",
    "type": "MappingDataFlow",
    "typeProperties": {
        "sources": [{
            "dataset": "SalesSource",
            "name": "SalesSource"
        }],
        "sinks": [{
            "dataset": "SalesTarget",
            "name": "SalesTarget"
        }],
        "transformations": [
            {
                "name": "FilterValidRecords",
                "type": "filter",
                "condition": "SalesAmount > 0"
            },
            {
                "name": "AddDerivedColumns",
                "type": "derivedColumn",
                "derivedColumns": [{
                    "name": "Year",
                    "expression": "year(SaleDate)"
                }]
            },
            {
                "name": "AggregateSales",
                "type": "aggregate",
                "groupBy": ["ProductKey", "Year"],
                "aggregates": [{
                    "name": "TotalSales",
                    "expression": "sum(SalesAmount)"
                }]
            }
        ]
    }
}
```

### Pipeline Orchestration

```json
{
    "name": "DailyETLPipeline",
    "properties": {
        "activities": [
            {
                "name": "CheckFileExists",
                "type": "GetMetadata",
                "inputs": [{
                    "referenceName": "SourceFolder",
                    "type": "DatasetReference"
                }]
            },
            {
                "name": "CopyToStaging",
                "type": "Copy",
                "dependsOn": [{
                    "activity": "CheckFileExists",
                    "dependencyConditions": ["Succeeded"]
                }],
                "inputs": [{
                    "referenceName": "SourceDataset",
                    "type": "DatasetReference"
                }],
                "outputs": [{
                    "referenceName": "StagingDataset",
                    "type": "DatasetReference"
                }]
            },
            {
                "name": "TransformData",
                "type": "DataFlow",
                "dependsOn": [{
                    "activity": "CopyToStaging",
                    "dependencyConditions": ["Succeeded"]
                }]
            }
        ],
        "triggers": [{
            "name": "DailyTrigger",
            "type": "ScheduleTrigger",
            "typeProperties": {
                "recurrence": {
                    "frequency": "Day",
                    "interval": 1,
                    "startTime": "2024-01-01T02:00:00Z"
                }
            }
        }]
    }
}
```

---

## 7. Security & Governance

### 📖 What is Security in Synapse?

Synapse provides multiple security layers:

- **Network Security**: Private endpoints, Managed VNet
- **Identity**: Azure AD, Managed Identity
- **Access Control**: Role-based, object-level
- **Data Protection**: Encryption, masking

**Why is this important for Data Engineering?**
- Protect sensitive data
- Compliance requirements
- Audit trails

### Managed Identity

```sql
-- Managed Identity Usage

-- Workspace Managed Identity
-- Automatically created with workspace
-- Used for:
-- - Accessing ADLS
-- - Connecting to SQL pools
-- - Auth with Azure services

-- Example: Access ADLS with MI
CREATE EXTERNAL DATA SOURCE DataLake
WITH
(
    LOCATION = 'https://mystorage.dfs.core.windows.net/',
    CREDENTIAL = (IDENTITY = 'Managed Identity')
);

-- Assign MI to workspace in Azure Portal
-- Storage Blob Data Contributor role
```

### Access Control

```sql
-- Synapse Access Control

-- Workspace-level roles:
-- - Synapse Administrator
-- - Synapse Contributor
-- - Synapse Compute Contributor
-- - Synapse Artifact Publisher

-- SQL Pool roles:
-- - db_owner
-- - db_datareader
-- - db_datawriter
-- - db_ddladmin

-- Granting Permissions
GRANT SELECT ON SCHEMA::dbo TO [user@domain.com];
GRANT CREATE TABLE TO [user@domain.com];
GRANT ADMINISTER DATABASE BULK OPERATIONS TO [user@domain.com];
```

### Row-Level Security

```sql
-- Row-Level Security in Dedicated SQL Pool

-- Create function to filter rows
CREATE FUNCTION fn_SalesFilter(@UserID AS VARCHAR(50))
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN SELECT 1 AS fn_result
WHERE EXISTS (
    SELECT 1
    FROM dbo.Sales s
    JOIN dbo.UserRegions u ON s.RegionID = u.RegionID
    WHERE u.UserID = @UserID
    OR IS_ROLEMEMBER('SalesManager') = 1
);

-- Apply security policy
CREATE SECURITY POLICY SalesFilter
ADD FILTER PREDICATE dbo.fn_SalesFilter(CONNECTIONPROPERTY('UserID'))
ON dbo.Sales
WITH (STATE = ON);
```

---

## 8. Performance Optimization

### 📖 Performance in Synapse

Optimization involves:

- Table design (distribution, indexes)
- Query optimization
- Resource management
- Statistics maintenance

**Why is this important for Data Engineering?**
- Reduce costs
- Faster insights
- Better resource utilization

### Statistics Management

```sql
-- Statistics are critical for query optimization

-- Auto-create statistics (enabled by default)
-- Manual statistics for complex queries

-- Create statistics
CREATE STATISTICS Stats_CustomerID
ON dbo.FactSales (CustomerKey);

CREATE STATISTICS Stats_ProductDate
ON dbo.FactSales (ProductKey, SaleDate);

-- Update statistics
UPDATE STATISTICS dbo.FactSales (Stats_CustomerID);

-- Update all statistics
UPDATE STATISTICS dbo.FactSales;

-- Check statistics info
DBCC SHOW_STATISTICS ('dbo.FactSales', Stats_CustomerID);
```

### Query Optimization

```sql
-- Query Optimization Tips

-- 1. Use appropriate distribution
-- Bad: Joining on non-distribution key
SELECT * FROM FactSales f
JOIN DimCustomer c ON f.CustomerKey = c.CustomerKey
-- Good: Both distributed on CustomerKey

-- 2. Filter on distribution column
-- Bad: Filter on non-partition column
SELECT * FROM FactSales WHERE SalesAmount > 1000
-- Good: Filter on partition column
SELECT * FROM FactSales WHERE SaleDate = '2024-01-01'

-- 3. Select only needed columns
-- Bad: SELECT *
-- Good: SELECT CustomerKey, SaleDate, SalesAmount

-- 4. Use CTAS for complex queries
CREATE TABLE result_table
WITH (DISTRIBUTION = HASH(CustomerKey))
AS
SELECT CustomerKey, SUM(SalesAmount) AS Total
FROM FactSales
GROUP BY CustomerKey;

-- 5. Avoid functions on columns in WHERE
-- Bad: WHERE YEAR(SaleDate) = 2024
-- Good: WHERE SaleDate >= '2024-01-01' AND SaleDate < '2025-01-01'
```

### Workload Management

```sql
-- Workload Groups and Classification

-- Create workload group
CREATE WORKLOAD GROUP SalesGroup
WITH
(
    MIN_PERCENTAGE_RESOURCE = 20,
    REQUEST_MIN_RESOURCE_GRANT_PERCENT = 10,
    CAP_PERCENTAGE_RESOURCE = 40
);

-- Create classifier
CREATE WORKLOAD CLASSIFIER SalesClassifier
WITH
(
    WORKLOAD_GROUP = 'SalesGroup',
    MEMBERNAME = 'SalesTeam',
    IMPORTANCE = HIGH
);

-- Monitor workloads
SELECT * FROM sys.dm_pdw_workload_groups;
SELECT * FROM sys.dm_pdw_waits;
```

---

## 9. Quick Reference

### Common T-SQL Commands

| Command | Description |
|---------|-------------|
| `SELECT * FROM table` | Basic query |
| `CREATE TABLE ... WITH (...)` | Create distributed table |
| `COPY INTO table FROM ...` | Load data from lake |
| `CREATE STATISTICS` | Create query statistics |
| `DBCC SHOW_STATISTICS` | View statistics |
| `CREATE MATERIALIZED VIEW` | Create pre-computed view |
| `ALTER TABLE SWITCH PARTITION` | Fast partition move |

### Distribution Selection Guide

| Table Type | Recommended Distribution |
|------------|------------------------|
| Large fact table | Hash on frequently joined column |
| Small dimension | Replicate |
| Staging table | Round-robin |
| No join pattern | Round-robin |

### Serverless vs Dedicated Quick Reference

| Feature | Serverless | Dedicated |
|---------|-----------|-----------|
| **Cost** | Pay per TB processed | Pay per DWU |
| **Scale** | Auto | Manual |
| **Min Data** | Any | ~1GB |
| **Latency** | Higher | Lower |
| **Best For** | Ad-hoc, exploration | Production DW |

### Security Components

| Component | Purpose |
|-----------|---------|
| Managed Identity | Workload authentication |
| Private Endpoints | Network isolation |
| RBAC | Access management |
| SQL Permissions | Object-level security |
| Row-Level Security | Data filtering |
| Dynamic Data Masking | Sensitive data hiding |

---

**Happy Learning! Remember: Practice makes perfect.**
