# PySpark for Data Engineering

## Spark Fundamentals
- What is Apache Spark?
- Spark Architecture (Driver, Executor, Cluster Manager)
- RDD vs DataFrame vs Dataset
- Lazy Evaluation
- Spark Session vs Spark Context
- DAG, stages, and tasks execution model
- Narrow vs wide transformations and shuffle boundaries
- Catalyst optimizer and Tungsten execution engine fundamentals

## PySpark Setup
- Installation & Configuration
- Creating SparkSession
- Local vs Cluster Mode
- Configuring Memory & Cores

## RDD (Resilient Distributed Dataset)
- Creating RDDs (parallelize, textFile)
- Transformations (map, filter, flatMap, reduceByKey)
- Actions (collect, count, first, take, reduce)
- RDD Persistence (cache, persist)
- Partitioning & Repartitioning

## DataFrames & Datasets
- Creating DataFrames (from RDD, from files)
- Schema Definition (StructType, StructField)
- select, selectExpr, withColumn, withColumnRenamed
- filter, where, drop, dropDuplicates
- sort, orderBy, limit
- groupBy, agg, pivot
- join (inner, left, right, outer, cross)
- union, unionByName

## Spark SQL
- Creating Temp Views
- Running SQL Queries
- Built-in Functions (pyspark.sql.functions)
- User Defined Functions (UDFs)
- Window Functions

## Data Types & Handling
- Data Types (String, Integer, Float, Date, Timestamp)
- Type Casting (cast function)
- Handling NULL Values (na.drop, na.fill, na.replace)
- String Manipulation
- Date & Timestamp Operations

## File Formats & I/O
- CSV (read/write, options)
- JSON (read/write, multiline)
- Parquet (read/write, partitionBy)
- Avro (read/write)
- Delta Lake (read/write)
- ORC Format
- Reading/Writing to Databases (JDBC)

## Performance Optimization
- Understanding Partitions
- repartition vs coalesce
- Broadcasting (broadcast join)
- Caching & Persistence
- Spark UI & Monitoring
- Explain Plan
- Adaptive Query Execution (AQE)
- Predicate pushdown and partition pruning
- Data skew detection and skew-mitigation strategies

## Advanced Topics
- Accumulators
- Broadcast Variables
- Custom Partitioners
- Structured Streaming
- Spark MLlib Basics
- Structured Streaming theory (event-time, watermarking, checkpointing)

## Integration
- PySpark with Delta Lake
- PySpark with AWS S3
- PySpark with Azure Blob Storage
- PySpark with Databricks

## Useful Resources
- Theory Notes: `./pyspark_theory.md`
- Official PySpark Docs: https://spark.apache.org/docs/latest/api/python/
- Databricks Academy: https://academy.databricks.com/
- PySpark Tutorial: https://sparkbyexamples.com/pyspark-tutorial/
- Book: "Learning Spark" by O'Reilly
