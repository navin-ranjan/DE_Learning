# PySpark Theory & Tutorial

## Table of Contents
1. [Spark Fundamentals](#1-spark-fundamentals)
2. [PySpark Setup](#2-pyspark-setup)
3. [RDD (Resilient Distributed Dataset)](#3-rdd-resilient-distributed-dataset)
4. [DataFrames \& Datasets](#4-dataframes--datasets)
5. [Spark SQL](#5-spark-sql)
6. [Data Types \& Handling](#6-data-types--handling)
7. [File Formats \& I/O](#7-file-formats--io)
8. [Performance Optimization](#8-performance-optimization)
9. [Advanced Topics](#9-advanced-topics)
10. [Integration](#10-integration)

---

## 1. Spark Fundamentals

### What is Apache Spark?

**Apache Spark** is an open-source, distributed computing system designed for big data processing and analytics. It provides an interface for programming entire clusters with implicit data parallelism and fault tolerance.

**Key Characteristics:**
- **In-Memory Processing**: Stores data in RAM for faster processing compared to disk-based systems like Hadoop MapReduce
- **Distributed Computing**: Distributes data across multiple machines (nodes) in a cluster
- **Lazy Evaluation**: Transformations are not executed until an action is called
- **Fault Tolerance**: Automatically recovers from failures through RDD lineage
- **Multi-Language Support**: Supports Python (PySpark), Scala, Java, and R

**Why is this important for Data Engineering?**
- Processing large datasets that don't fit in memory on a single machine
- Building ETL pipelines for data warehouses
- Real-time stream processing
- Machine learning at scale

---

### Spark Architecture

Spark uses a **master-slave** architecture with the following components:

**1. Driver (Driver Program)**
- The main program that runs your Spark application
- Creates SparkContext which connects to the cluster manager
- Converts user code into tasks and schedules them for executors
- Coordinates task execution and collects results

**2. Executors**
- Worker nodes that run tasks assigned by the driver
- Each executor has its own JVM and manages data in memory/disk
- Stores computed results and broadcasts variables
- Reports status back to the driver

**3. Cluster Manager**
- Manages cluster resources (YARN, Mesos, Kubernetes, or Spark's standalone mode)
- Allocates resources to applications
- Monitors cluster health

**Execution Flow:**
```
User Code → Driver → Cluster Manager → Executors → Results
```

---

### RDD vs DataFrame vs Dataset

| Feature | RDD | DataFrame | Dataset |
|---------|-----|-----------|---------|
| **Type Safety** | Strong (Scala/Java) | Weak (runtime) | Strong (compile-time) |
| **Optimization** | None | Catalyst Optimizer | Catalyst Optimizer |
| **API** | Low-level | High-level | High-level |
| **Performance** | Slower | Faster | Fastest |
| **Schema** | Unknown until runtime | Known (schema) | Known (schema) |
| **Use Case** | Custom transformations | ETL, Analytics | Type-safe operations |

**When to use each:**
- **RDD**: When you need low-level control, custom partitioning, or older Spark code
- **DataFrame**: When performing ETL, SQL operations, and general data processing
- **Dataset**: When you need type safety in Scala/Java and better performance

---

### Lazy Evaluation

**Lazy Evaluation** means that Spark does not execute transformations immediately. Instead, it builds a **Directed Acyclic Graph (DAG)** of transformations and only executes them when an action is called.

**Transformations (Lazy):**
- map(), filter(), flatMap(), reduceByKey(), union(), join()
- These build the execution plan but don't execute

**Actions (Eager):**
- collect(), count(), first(), take(), saveAsTextFile()
- These trigger the actual computation

**Benefits:**
- Optimization opportunity for Spark to build efficient execution plans
- Reduced data movement - Spark can optimize the entire pipeline
- Memory efficiency - data is not materialized until needed

---

### Spark Session vs Spark Context

**SparkContext (Spark Core)**
- The entry point for Spark functionality in RDD era
- Created automatically when you start Spark shell
- Manages shared variables (broadcast, accumulators)
- Access to Spark services

```python
# Old way (Spark 1.x)
sc = SparkContext()
```

**SparkSession (Spark 2.x+)**
- Unified entry point for all Spark functionality
- Replaces SparkContext, SQLContext, HiveContext
- Provides DataFrame and Dataset APIs
- Supports Spark SQL, Hive, streaming

```python
# New way (Spark 2.x+)
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
```

**Key Differences:**
- SparkSession can create SparkContext, but not vice versa
- SparkSession includes SQL functionality
- SparkSession is the recommended approach for modern Spark applications

---

## 2. PySpark Setup

### Installation & Configuration

**Installation:**
```bash
pip install pyspark
```

**Python Version Support:**
- PySpark 3.5+ supports Python 3.9+

**Verifying Installation:**
```python
import pyspark
print(pyspark.__version__)
```

---

### Creating SparkSession

```python
from pyspark.sql import SparkSession

# Basic SparkSession
spark = SparkSession.builder \
    .appName("MyApplication") \
    .master("local[*]") \
    .getOrCreate()

# With configurations
spark = SparkSession.builder \
    .appName("DataEngineeringApp") \
    .master("spark://master:7077") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "2g") \
    .config("spark.sql.shuffle.partitions", "200") \
    .enableHiveSupport() \
    .getOrCreate()

# Stop SparkSession
spark.stop()
```

---

### Local vs Cluster Mode

**Local Mode:**
- Runs on a single machine
- Good for development and testing
- Uses all available cores with `local[*]`

```python
spark = SparkSession.builder \
    .master("local[4]") \
    .appName("LocalApp") \
    .getOrCreate()
```

**Cluster Mode:**
- Runs on multiple machines
- For production workloads
- Requires cluster manager (YARN, Mesos, Kubernetes, Standalone)

```python
# YARN cluster
spark = SparkSession.builder \
    .master("yarn") \
    .appName("YarnApp") \
    .getOrCreate()

# Standalone cluster
spark = SparkSession.builder \
    .master("spark://spark-master:7077") \
    .appName("StandaloneApp") \
    .getOrCreate()
```

---

### Configuring Memory & Cores

**Driver Settings:**
```python
.config("spark.driver.memory", "4g")      # Driver memory
.config("spark.driver.cores", "4")        # Driver cores
.config("spark.driver.maxResultSize", "2g")  # Max result size
```

**Executor Settings:**
```python
.config("spark.executor.memory", "4g")    # Executor memory
.config("spark.executor.cores", "4")      # Cores per executor
.config("spark.executor.instances", "10") # Number of executors
```

**Shuffle Settings:**
```python
.config("spark.sql.shuffle.partitions", "200")  # Default shuffle partitions
.config("spark.default.parallelism", "100")       # Default parallelism
```

---

## 3. RDD (Resilient Distributed Dataset)

### What is RDD?

**RDD (Resilient Distributed Dataset)** is the fundamental data structure in Spark. It represents an immutable, partitioned collection of elements that can be operated on in parallel.

**Characteristics:**
- **Resilient**: Can recover from failures automatically
- **Distributed**: Data is distributed across cluster nodes
- **Dataset**: Collection of partitioned data

---

### Creating RDDs

**From Python Collection (parallelize):**
```python
data = [1, 2, 3, 4, 5]
rdd = spark.sparkContext.parallelize(data)

# With partitions
rdd = spark.sparkContext.parallelize(data, numSlices=10)
```

**From External Files:**
```python
# Text file
rdd = spark.sparkContext.textFile("data.txt")
rdd = spark.sparkContext.wholeTextFiles("directory/")

# From multiple files
rdd = spark.sparkContext.textFile("data/*.txt")

# From other data sources
rdd = spark.sparkContext.sequenceFile("data.seq")
rdd = spark.sparkContext.hadoopRDD(...)
```

**From DataFrame:**
```python
rdd = df.rdd
```

---

### RDD Transformations

Transformations create a new RDD from an existing one (lazy evaluation). They are categorized into **Narrow Transformations** (no shuffle) and **Wide Transformations** (requires shuffle).

#### Narrow Transformations
These transformations do not require shuffling data across partitions.

**map(func)**
```python
rdd = spark.sparkContext.parallelize([1, 2, 3, 4])
rdd_squared = rdd.map(lambda x: x ** 2)  # [1, 4, 9, 16]
```

**filter(func)**
```python
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
rdd_even = rdd.filter(lambda x: x % 2 == 0)  # [2, 4]
```

**flatMap(func)**
```python
rdd = spark.sparkContext.parallelize(["hello world", "spark is great"])
rdd_words = rdd.flatMap(lambda x: x.split(" "))  # ["hello", "world", "spark", "is", "great"]
```

**mapPartitions(func)**
```python
# Process each partition as an iterator
rdd = rdd.mapPartitions(lambda iter: [sum(iter)])
```

**mapPartitionsWithIndex(func)**
```python
# Similar to mapPartitions but provides partition index
def partition_index(partition_index, iterator):
    for item in iterator:
        yield (partition_index, item)

rdd_with_index = rdd.mapPartitionsWithIndex(partition_index)
```

**glom()**
```python
# Convert each partition into a single list
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5], 2)
rdd_glommed = rdd.glom()  # [[1, 2], [3, 4, 5]]
```

**sample(withReplacement, fraction, seed)**
```python
# Sample data from RDD
rdd_sampled = rdd.sample(withReplacement=False, fraction=0.5, seed=42)
```

---

#### Wide Transformations
These transformations require shuffling data across partitions.

**distinct()**
```python
rdd = spark.sparkContext.parallelize([1, 1, 2, 2, 3])
rdd_distinct = rdd.distinct()  # [1, 2, 3]
```

**union, intersection, subtract**
```python
rdd1 = spark.sparkContext.parallelize([1, 2, 3])
rdd2 = spark.sparkContext.parallelize([3, 4, 5])

union_rdd = rdd1.union(rdd2)           # [1, 2, 3, 3, 4, 5]
intersect_rdd = rdd1.intersection(rdd2) # [3]
subtract_rdd = rdd1.subtract(rdd2)      # [1, 2]
```

**reduceByKey(func)**
```python
rdd = spark.sparkContext.parallelize([("a", 1), ("b", 1), ("a", 1), ("b", 1)])
rdd_reduced = rdd.reduceByKey(lambda x, y: x + y)  # [("a", 2), ("b", 2)]
```

**groupByKey vs reduceByKey**
```python
# groupByKey - less efficient (shuffles all values)
rdd.groupByKey().mapValues(sum)

# reduceByKey - more efficient (combines before shuffle)
rdd.reduceByKey(lambda x, y: x + y)
```

**aggregateByKey(zeroValue, seqOp, combOp)**
```python
rdd = spark.sparkContext.parallelize([("a", 1), ("a", 2), ("b", 1)])
result = rdd.aggregateByKey(
    (0, 0),  # (sum, count)
    lambda acc, val: (acc[0] + val, acc[1] + 1),
    lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1])
)  # [("a", (3, 2)), ("b", (1, 1))]
```

**foldByKey(zeroValue, func)**
```python
rdd = spark.sparkContext.parallelize([("a", 1), ("a", 2), ("b", 1)])
result = rdd.foldByKey(0, lambda x, y: x + y)  # [("a", 3), ("b", 1)]
```

**sortByKey(ascending)**
```python
rdd = spark.sparkContext.parallelize([(3, "c"), (1, "a"), (2, "b")])
rdd_sorted = rdd.sortByKey()  # [(1, "a"), (2, "b"), (3, "c")]
```

**keys, values**
```python
rdd = spark.sparkContext.parallelize([("a", 1), ("b", 2)])
keys_rdd = rdd.keys()    # ["a", "b"]
values_rdd = rdd.values()  # [1, 2]
```

**join, leftOuterJoin, rightOuterJoin, fullOuterJoin**
```python
rdd1 = spark.sparkContext.parallelize([(1, "a"), (2, "b")])
rdd2 = spark.sparkContext.parallelize([(1, "x"), (3, "z")])

# Inner Join
joined = rdd1.join(rdd2)  # [(1, ("a", "x"))]

# Left Outer Join
left_joined = rdd1.leftOuterJoin(rdd2)  # [(1, ("a", "x")), (2, ("b", None))]

# Right Outer Join
right_joined = rdd1.rightOuterJoin(rdd2)  # [(1, ("a", "x")), (3, (None, "z"))]

# Full Outer Join
full_joined = rdd1.fullOuterJoin(rdd2)  # [(1, ("a", "x")), (2, ("b", None)), (3, (None, "z"))]
```

**cartesian(otherRDD)**
```python
# Cartesian product of two RDDs
rdd1 = spark.sparkContext.parallelize([1, 2])
rdd2 = spark.sparkContext.parallelize(["a", "b"])
cartesian_rdd = rdd1.cartesian(rdd2)  # [(1, "a"), (1, "b"), (2, "a"), (2, "b")]
```

**coalesce(numPartitions)**
```python
# Decrease partitions (no shuffle)
rdd_coalesced = rdd.coalesce(10)
```

**repartition(numPartitions)**
```python
# Increase or decrease partitions (shuffles)
rdd_repartitioned = rdd.repartition(100)
```

**partitionBy(numPartitions, partitionFunc)**
```python
rdd = spark.sparkContext.parallelize([(1, "a"), (2, "b"), (3, "c")])
rdd_partitioned = rdd.partitionBy(2)  # Hash partition by key
```

---

### RDD Actions

Actions return values or write data to external storage (triggers execution). They force the evaluation of RDD transformations.

#### Basic Actions

**collect()**
```python
rdd = spark.sparkContext.parallelize([1, 2, 3, 4])
result = rdd.collect()  # [1, 2, 3, 4] - returns to driver
```

**count()**
```python
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
count = rdd.count()  # 5
```

**first()**
```python
rdd.first()  # Returns first element
```

**take(n)**
```python
rdd.take(3)  # Returns first n elements
```

**takeSample(withReplacement, num, seed)**
```python
# Returns a random sample of n elements
sample = rdd.takeSample(withReplacement=False, num=3, seed=42)
```

**takeOrdered(n, key)**
```python
# Returns first n elements in ascending order
rdd = spark.sparkContext.parallelize([5, 2, 1, 4, 3])
rdd.takeOrdered(3)  # [1, 2, 3]

# With custom ordering
rdd.takeOrdered(3, key=lambda x: -x)  # [5, 4, 3]
```

**top(n)**
```python
# Returns top n elements in descending order
rdd = spark.sparkContext.parallelize([5, 2, 1, 4, 3])
rdd.top(3)  # [5, 4, 3]
```

---

#### Reduction Actions

**reduce(func)**
```python
rdd = spark.sparkContext.parallelize([1, 2, 3, 4])
result = rdd.reduce(lambda x, y: x + y)  # 10
```

**fold(zeroValue, func)**
```python
# Like reduce but with initial value
rdd.fold(0, lambda x, y: x + y)
```

**aggregate(zeroValue, seqOp, combOp)**
```python
rdd = spark.sparkContext.parallelize([1, 2, 3, 4])
result = rdd.aggregate(
    (0, 0),  # (sum, count)
    lambda acc, val: (acc[0] + val, acc[1] + 1),
    lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1])
)  # (10, 4) - returns (sum, count)
```

**countByKey()**
```python
rdd = spark.sparkContext.parallelize([("a", 1), ("b", 1), ("a", 1)])
result = rdd.countByKey()  # {"a": 2, "b": 1}
```

**countByValue()**
```python
rdd = spark.sparkContext.parallelize([1, 2, 2, 3, 3, 3])
result = rdd.countByValue()  # {1: 1, 2: 2, 3: 3}
```

**foreach(func)**
```python
# Apply function to each element (runs on executors)
rdd.foreach(lambda x: print(x))

# Using accumulator
acc = spark.sparkContext.accumulator(0)
rdd.foreach(lambda x: acc.add(x))
print(acc.value)
```

**foreachPartition(func)**
```python
# Apply function to each partition
def process_partition(partition):
    total = sum(partition)
    print(f"Partition sum: {total}")

rdd.foreachPartition(process_partition)
```

---

#### File Output Actions

**saveAsTextFile(path)**
```python
rdd.saveAsTextFile("output/path")
```

**saveAsSequenceFile(path)**
```python
# Save as Hadoop sequence file
rdd.saveAsSequenceFile("output/path")
```

**saveAsObjectFile(path)**
```python
# Save using Java serialization
rdd.saveAsObjectFile("output/path")
```

---

#### Debugging Actions

**getNumPartitions()**
```python
rdd.getNumPartitions()  # Returns number of partitions
```

**id()**
```python
rdd.id()  # Returns unique ID for this RDD
```

**name()**
```python
rdd.name()  # Returns name of RDD
```

**toDebugString()**
```python
# Returns execution plan (lineage)
print(rdd.toDebugString())
```

**toLocalIterator()**
```python
# Returns iterator over all elements
for item in rdd.toLocalIterator():
    print(item)
```

---

### RDD Persistence (cache, persist)

**Why Cache?**
- Reuse intermediate results across multiple actions
- Avoid recomputation

**cache()**
```python
rdd = rdd.filter(lambda x: x > 10).cache()
# Now rdd will be cached in memory after first action
```

**persist(storageLevel)**
```python
from pyspark.storagelevel import StorageLevel

rdd = rdd.persist(StorageLevel.MEMORY_AND_DISK)
rdd = rdd.persist(StorageLevel.MEMORY_ONLY)
rdd = rdd.persist(StorageLevel.DISK_ONLY)
```

**unpersist()**
```python
rdd.unpersist()  # Remove from cache
```

---

### Partitioning & Repartitioning

**What is Partitioning?**
- Data is divided into partitions, each processed by one task
- Default: number of cores available

**repartition(numPartitions)**
```python
# Increase or decrease partitions (shuffles data)
rdd_repartitioned = rdd.repartition(100)
```

**coalesce(numPartitions)**
```python
# Decrease partitions only (no shuffle)
rdd_coalesced = rdd.coalesce(10)
```

**getNumPartitions()**
```python
rdd.getNumPartitions()  # Returns number of partitions
```

**partitionBy(numPartitions, partitionFunc)**
```python
rdd = spark.sparkContext.parallelize([(1, "a"), (2, "b"), (3, "c")])
rdd_partitioned = rdd.partitionBy(2)  # Hash partition by key
```

---

## 4. DataFrames & Datasets

### What is a DataFrame?

A **DataFrame** is a distributed collection of data organized into named columns, similar to a table in a relational database or a DataFrame in Pandas.

**Key Features:**
- Schema is known (column names and types)
- Optimized by Catalyst Optimizer
- Supports SQL-like operations
- Can be created from various data sources

---

### Creating DataFrames

**From RDD with Schema:**
```python
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.getOrCreate()

# Define schema
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# Create from RDD
rdd = spark.sparkContext.parallelize([(1, "John", 30), (2, "Jane", 25)])
df = spark.createDataFrame(rdd, schema)
```

**From Python List/List of Tuples:**
```python
data = [("John", 30), ("Jane", 25), ("Bob", 35)]
df = spark.createDataFrame(data, ["name", "age"])

# With schema
data = [("John", 30), ("Jane", 25)]
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])
df = spark.createDataFrame(data, schema)
```

**From CSV:**
```python
df = spark.read.csv("data.csv", header=True, inferSchema=True)
df = spark.read.format("csv").option("header", "true").load("data.csv")
```

**From JSON:**
```python
df = spark.read.json("data.json")
df = spark.read.format("json").load("data.json")
```

**From Parquet:**
```python
df = spark.read.parquet("data.parquet")
```

**From JDBC/Database:**
```python
df = spark.read.format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/mydb") \
    .option("dbtable", "employees") \
    .option("user", "username") \
    .option("password", "password") \
    .load()
```

---

### Schema Definition

**StructType and StructField:**
```python
from pyspark.sql.types import *

schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), True),
    StructField("email", StringType(), False),
    StructField("age", IntegerType(), True),
    StructField("salary", DoubleType(), True)
])

df = spark.createDataFrame(rdd, schema)
```

**Common Data Types:**
```python
from pyspark.sql.types import *

StringType()      # VARCHAR
IntegerType()     # INT
LongType()        # BIGINT
DoubleType()      # DOUBLE
FloatType()       # FLOAT
BooleanType()     # BOOLEAN
DateType()        # DATE
TimestampType()   # TIMESTAMP
ArrayType(StringType())  # ARRAY
MapType(StringType(), IntegerType())  # MAP
StructType([...]) # STRUCT
```

**printSchema()**
```python
df.printSchema()
# root
#  |-- id: integer (nullable = true)
#  |-- name: string (nullable = true)
```

---

### DataFrame Operations

**select - Select Columns:**
```python
df.select("name", "age")
df.select(df.name, df.age + 1)
df.selectExpr("name", "age as new_age", "upper(name)")
```

**withColumn - Add/Modify Column:**
```python
from pyspark.sql.functions import col, upper

df = df.withColumn("name_upper", upper(col("name")))
df = df.withColumn("age_double", col("age") * 2)
df = df.withColumn("new_col", lit("constant_value"))
```

**withColumnRenamed - Rename Column:**
```python
df = df.withColumnRenamed("old_name", "new_name")
```

**drop - Remove Column:**
```python
df.drop("unwanted_column")
df.drop("col1", "col2")
```

**filter / where - Filter Rows:**
```python
df.filter(col("age") > 25)
df.filter((col("age") > 25) & (col("name") == "John"))
df.where("age > 25")
```

**dropDuplicates - Remove Duplicates:**
```python
df.dropDuplicates()
df.dropDuplicates(["name"])  # Based on specific columns
```

**sort / orderBy - Sorting:**
```python
df.sort("age", ascending=False)
df.orderBy(col("age").desc())
df.sortWithinPartitions("age")  # Sort within each partition
```

**limit - Select Top N:**
```python
df.limit(10)
```

---

### GroupBy & Aggregation

**groupBy:**
```python
df.groupBy("department").count()
df.groupBy("department").sum("salary")
df.groupBy("department").avg("age")
df.groupBy("department").min("salary")
df.groupBy("department").max("salary")
```

**agg - Multiple Aggregations:**
```python
from pyspark.sql.functions import sum, avg, min, max, count, countDistinct

df.groupBy("department").agg(
    count("*").alias("total_count"),
    sum("salary").alias("total_salary"),
    avg("salary").alias("avg_salary"),
    min("salary").alias("min_salary"),
    max("salary").alias("max_salary")
)
```

**pivot:**
```python
df.groupBy("year").pivot("quarter").sum("sales")
```

---

### Joins

```python
# Define DataFrames
emp_df = spark.createDataFrame([(1, "John", 10), (2, "Jane", 20)], ["id", "name", "dept_id"])
dept_df = spark.createDataFrame([(10, "IT"), (20, "HR")], ["dept_id", "dept_name"])

# Inner Join
emp_df.join(dept_df, "dept_id")
emp_df.join(dept_df, emp_df.dept_id == dept_df.dept_id, "inner")

# Left Join
emp_df.join(dept_df, "dept_id", "left")

# Right Join
emp_df.join(dept_df, "dept_id", "right")

# Outer Join (Full)
emp_df.join(dept_df, "dept_id", "outer")

# Cross Join (Cartesian)
emp_df.crossJoin(dept_df)

# Broadcast Join (for small tables)
from pyspark.sql.functions import broadcast
emp_df.join(broadcast(dept_df), "dept_id")
```

---

### Union

```python
df1 = spark.createDataFrame([(1, "a")], ["id", "val"])
df2 = spark.createDataFrame([(2, "b")], ["id", "val"])

# union - keeps duplicates (PySpark 3.x uses unionByName)
df_combined = df1.union(df2)

# unionByName - union by column names (recommended)
df_combined = df1.unionByName(df2)

# unionAll (deprecated, use union)
df_combined = df1.unionAll(df2)
```

---

## 5. Spark SQL

### Creating Temp Views

**createOrReplaceTempView:**
```python
df.createOrReplaceTempView("employees")

# Query with SQL
result = spark.sql("SELECT * FROM employees WHERE age > 30")
```

**createGlobalTempView:**
```python
df.createGlobalTempView("global_employees")

# Access with database prefix
result = spark.sql("SELECT * FROM global_temp.global_employees")
```

**createOrReplaceGlobalTempView:**
```python
df.createOrReplaceGlobalTempView("global_employees")
```

---

### Running SQL Queries

```python
# Create temporary view
df.createOrReplaceTempView("sales")

# Simple queries
spark.sql("SELECT * FROM sales").show()
spark.sql("SELECT COUNT(*) FROM sales").show()
spark.sql("SELECT department, AVG(salary) FROM sales GROUP BY department").show()

# Complex queries
query = """
    SELECT
        year,
        month,
        SUM(amount) as total_sales,
        AVG(amount) as avg_sales
    FROM sales
    WHERE status = 'completed'
    GROUP BY year, month
    ORDER BY year, month
"""
result = spark.sql(query)
```

**spark.sql() configurations:**
```python
spark.conf.set("spark.sql.shuffle.partitions", "100")
spark.sql("SET -v").show(n=100, truncate=False)
```

---

### Built-in Functions (pyspark.sql.functions)

**Import:**
```python
from pyspark.sql import functions as F
# or
from pyspark.sql.functions import col, sum, avg, when, lit
```

**String Functions:**
```python
from pyspark.sql.functions import upper, lower, trim, substring, concat, length

df.select(upper("name"), lower("city")).show()
df.select(concat("first_name", "last_name")).show()
df.select(substring("name", 1, 3)).show()
```

**Numeric Functions:**
```python
from pyspark.sql.functions import abs, ceil, floor, round, sqrt, pow

df.select(abs("negative_col"), round("salary")).show()
```

**Date Functions:**
```python
from pyspark.sql.functions import current_date, current_timestamp, year, month, dayofmonth, date_add, datediff

df.select(current_date(), current_timestamp()).show()
df.select(year("hire_date"), month("hire_date")).show()
df.select(datediff(current_date(), "hire_date")).show()
```

**Conditional Functions:**
```python
from pyspark.sql.functions import when, coalesce, lit

df.select(
    "name",
    "salary",
    when(col("salary") > 50000, "High").otherwise("Low").alias("salary_level")
).show()

df.select(coalesce(col("phone"), col("mobile"), lit("N/A"))).show()
```

**Aggregation Functions:**
```python
from pyspark.sql.functions import sum, avg, count, countDistinct, min, max

df.agg(sum("salary"), avg("age"), count("*")).show()
```

**Window Functions:**
```python
from pyspark.sql.functions import row_number, rank, dense_rank, lag, lead, sum over window

from pyspark.sql.window import Window

window_spec = Window.partitionBy("department").orderBy("salary")

df.withColumn("row_number", row_number().over(window_spec)) \
  .withColumn("rank", rank().over(window_spec)) \
  .withColumn("lag_salary", lag("salary", 1).over(window_spec)) \
  .withColumn("lead_salary", lead("salary", 1).over(window_spec)) \
  .show()
```

---

### User Defined Functions (UDFs)

**Python UDF:**
```python
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Define function
def categorize_age(age):
    if age < 30:
        return "Young"
    elif age < 50:
        return "Middle"
    else:
        return "Senior"

# Create UDF
categorize_age_udf = udf(categorize_age, StringType())

# Use UDF
df.select("name", "age", categorize_age_udf("age").alias("category")).show()

# Register as SQL function
spark.udf.register("categorize_age", categorize_age, StringType())
spark.sql("SELECT name, age, categorize_age(age) FROM employees").show()
```

**Using @pandas_udf (Vectorized UDF - Faster):**
```python
from pyspark.sql.functions import pandas_udf
import pandas as pd

@pandas_udf("double")
def sum_udf(s1: pd.Series, s2: pd.Series) -> pd.Series:
    return s1 + s2

df.select(sum_udf(col("a"), col("b"))).show()
```

---

## 6. Data Types & Handling

### Data Types

**Common PySpark Data Types:**
```python
from pyspark.sql.types import *

StringType()       # "hello"
IntegerType()      # 42
LongType()         # 42L
DoubleType()       # 3.14
FloatType()        # 3.14f
BooleanType()      # True/False
DateType()         # 2024-01-01
TimestampType()    # 2024-01-01 12:00:00
ArrayType(StringType())    # ["a", "b", "c"]
MapType(StringType(), IntegerType())  # {"a": 1, "b": 2}
StructType([
    StructField("name", StringType()),
    StructField("age", IntegerType())
])  # {"name": "John", "age": 30}
```

---

### Type Casting

```python
from pyspark.sql.functions import col, cast

# Cast column type
df.select(col("salary").cast("double")).show()
df.select(col("salary").cast(DoubleType())).show()

# Using withColumn
df = df.withColumn("salary", col("salary").cast("double"))
df = df.withColumn("year", col("year").cast(IntegerType()))

# String to Date
df = df.withColumn("date", col("date_string").cast(DateType()))

# Date to String
df = df.withColumn("date_string", col("date").cast(StringType()))
```

---

### Handling NULL Values

**Check for NULL:**
```python
df.filter(col("name").isNull()).show()
df.filter(col("name").isNotNull()).show()
```

**Drop rows with NULL:**
```python
df.na.drop()                    # Drop any row with NULL
df.na.drop(how="all")           # Drop only if all values are NULL
df.na.drop(thresh=2)            # Drop if less than 2 non-null values
df.na.drop(subset=["name", "age"])  # Drop if NULL in specific columns
```

**Fill NULL values:**
```python
df.na.fill("Unknown")                   # Fill all NULL strings
df.na.fill(0)                           # Fill all NULL numbers
df.na.fill({"name": "Unknown", "age": 0})  # Fill specific columns
```

**Replace values:**
```python
df.na.replace(["NA", "N/A"], ["Unknown", "Unknown"], ["name"])
```

**Handle NULL in expressions:**
```python
from pyspark.sql.functions import coalesce, lit

# Return first non-null
df.select(coalesce(col("phone"), col("mobile"), lit("No phone"))).show()

# IFNULL equivalent
df.select(when(col("name").isNull(), "Unknown").otherwise(col("name"))).show()
```

---

### String Manipulation

```python
from pyspark.sql.functions import *

# Trim
df.select(trim(col("name")), ltrim(col("name")), rtrim(col("name"))).show()

# Case conversion
df.select(upper("name"), lower("email")).show()

# Substring
df.select(substring("name", 1, 3)).show()

# Replace
df.select(regexp_replace("name", "John", "Jonathan")).show()

# Split
df.select(split("name", " ")).show()

# Concatenate
df.select(concat("first_name", lit(" "), "last_name")).show()

# Length
df.select(length("name")).show()

# Contains
df.filter(col("name").contains("John")).show()

# StartsWith / EndsWith
df.filter(col("name").startswith("J")).show()
df.filter(col("name").endsWith("n")).show()
```

---

### Date & Timestamp Operations

```python
from pyspark.sql.functions import *

# Current date/time
df.select(current_date(), current_timestamp()).show()

# Extract year, month, day
df.select(year("date"), month("date"), dayofmonth("date")).show()

# Date arithmetic
df.select(date_add("date", 5), date_sub("date", 5)).show()
df.select(datediff("end_date", "start_date")).show()

# Format
df.select(date_format("timestamp", "yyyy-MM-dd")).show()

# To timestamp
df.select(to_timestamp("date_string", "yyyy-MM-dd")).show()

# To date
df.select(to_date("date_string", "yyyy-MM-dd")).show()

# Truncate
df.select(trunc("date", "year"), trunc("date", "month")).show()
```

---

## 7. File Formats & I/O

### CSV

**Reading CSV:**
```python
df = spark.read.csv("data.csv")
df = spark.read.csv("data.csv", header=True)
df = spark.read.csv("data.csv", header=True, inferSchema=True)
df = spark.read.csv("data.csv", header=True, schema=my_schema)

# Options
df = spark.read.csv(
    "data.csv",
    header=True,
    inferSchema=True,
    sep=",",
    quote='"',
    escape='\\',
    encoding="UTF-8"
)
```

**Writing CSV:**
```python
df.write.csv("output/path")
df.write.csv("output/path", header=True)
df.write.mode("overwrite").csv("output/path", header=True)
```

**Modes:**
```python
df.write.mode("overwrite").csv("path")      # Overwrite
df.write.mode("append").csv("path")          # Append
df.write.mode("ignore").csv("path")          # Ignore if exists
df.write.mode("error").csv("path")           # Error if exists
```

---

### JSON

**Reading JSON:**
```python
df = spark.read.json("data.json")
df = spark.read.json("data.json", multiLine=True)
df = spark.read.format("json").load("data.json")
```

**Writing JSON:**
```python
df.write.json("output/path")
df.write.mode("overwrite").json("output/path")
```

---

### Parquet

**Reading Parquet:**
```python
df = spark.read.parquet("data.parquet")
df = spark.read.format("parquet").load("data.parquet")
```

**Writing Parquet:**
```python
df.write.parquet("output/path")
df.write.partitionBy("year", "month").parquet("output/path")
df.write.mode("overwrite").parquet("output/path")
```

**Benefits of Parquet:**
- Columnar format (better compression)
- Schema preservation
- Predicate pushdown (filter during read)
- Faster query performance

---

### Delta Lake

**Reading Delta Lake:**
```python
df = spark.read.format("delta").load("delta-table-path")
```

**Writing Delta Lake:**
```python
df.write.format("delta").mode("overwrite").save("delta-table-path")

# With partition
df.write.format("delta").partitionBy("year").save("delta-table-path")
```

**Delta Lake Operations:**
```python
# Update
from delta.tables import DeltaTable

deltaTable = DeltaTable.forPath(spark, "delta-table-path")
deltaTable.update(
    condition="status = 'inactive'",
    set={"status": "'active'"}
)

# Delete
deltaTable.delete("status = 'inactive'")

# Merge (Upsert)
deltaTable.merge(
    source="updates",
    condition="t.id = s.id",
    whenMatchedUpdate(set={"name": "s.name"}),
    whenNotMatchedInsert(values={"id": "s.id", "name": "s.name"})
)
```

---

### Avro

**Reading Avro:**
```python
df = spark.read.format("avro").load("data.avro")
```

**Writing Avro:**
```python
df.write.format("avro").mode("overwrite").save("output/path")
```

---

### JDBC (Databases)

**Reading from Database:**
```python
df = spark.read.format("jdbc") \
    .option("url", "jdbc:postgresql://host:5432/database") \
    .option("dbtable", "tablename") \
    .option("user", "username") \
    .option("password", "password") \
    .load()

# With query
df = spark.read.format("jdbc") \
    .option("url", "jdbc:mysql://host:3306/database") \
    .option("query", "SELECT * FROM table WHERE id > 10") \
    .option("user", "username") \
    .option("password", "password") \
    .load()
```

**Writing to Database:**
```python
df.write.format("jdbc") \
    .option("url", "jdbc:postgresql://host:5432/database") \
    .option("dbtable", "tablename") \
    .option("user", "username") \
    .option("password", "password") \
    .save()
```

---

## 8. Performance Optimization

### Understanding Partitions

**What are partitions?**
- Data is split into chunks (partitions) across the cluster
- Each partition is processed by one task
- Number of partitions affects parallelism

**Checking partitions:**
```python
df.rdd.getNumPartitions()
df.explain(True)  # Shows partition info in plan
```

**Partition best practices:**
- Too few: Under-utilization of cluster
- Too many: Overhead of task scheduling
- Rule of thumb: 2-3x number of cores

---

### repartition vs coalesce

**repartition(numPartitions)**
- Can increase or decrease partitions
- Triggers full shuffle (expensive)
- Used when significantly changing partition count

```python
df_repartitioned = df.repartition(100)
df_repartitioned = df.repartition("department")  # Partition by column
```

**coalesce(numPartitions)**
- Can only decrease partitions
- No shuffle (or minimal shuffle) - faster
- Used to reduce partitions before writing

```python
df_coalesced = df.coalesce(10)  # Reduce from 100 to 10
```

---

### Broadcasting (broadcast join)

**When to use:**
- One table is small enough to fit in memory
- Avoid shuffling large table

```python
from pyspark.sql.functions import broadcast

# Broadcast join
result = df_large.join(broadcast(df_small), "key")

# Example
employees = spark.read.parquet("employees.parquet")
departments = spark.read.parquet("departments_small.parquet")

result = employees.join(broadcast(departments), "dept_id")
```

---

### Caching & Persistence

**cache()**
```python
df_cached = df.filter(...).cache()
# Now cached in memory after first action
```

**persist()**
```python
from pyspark.storagelevel import StorageLevel

df.persist(StorageLevel.MEMORY_AND_DISK)
df.persist(StorageLevel.MEMORY_ONLY)
df.persist(StorageLevel.DISK_ONLY)
```

**unpersist()**
```python
df.unpersist()
```

**Check cached:**
```python
spark.catalog.isCached("tableName")
spark.catalog.cacheTable("tableName")
spark.catalog.uncacheTable("tableName")
```

---

### Spark UI & Monitoring

**Spark UI:**
- Accessible at http://driver:4040
- Shows:
  - Jobs, Stages, Tasks
  - Executors
  - Storage
  - Environment

**Programmatically:**
```python
# Get Spark UI URL
spark.sparkContext.uiWebUrl

# Get executor info
spark.sparkContext._jsc.sc().getExecutorMemoryStatus()

# Application ID
spark.sparkContext.applicationId
```

**Logging:**
```python
spark.sparkContext.setLogLevel("INFO")  # DEBUG, INFO, WARN, ERROR
```

---

### Explain Plan

**explain()**
```python
df.explain()
df.explain(True)  # Extended plan
```

**Output shows:**
- Parsed Logical Plan
- Analyzed Logical Plan
- Optimized Logical Plan
- Physical Plan

```python
df.select("name", "salary").where(col("salary") > 50000).explain(True)
```

---

### Adaptive Query Execution (AQE)

**What is AQE?**
- Dynamic query optimization at runtime
- Enabled by default in Spark 3.2+

**Key features:**
- Dynamic partition coalescing
- Dynamic conversion of sort-merge join to broadcast join
- Dynamic switch between broadcast and shuffle joins
- Runtime row-level filter pruning

**Configuration:**
```python
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
```

---

## 9. Advanced Topics

### Accumulators

**What are Accumulators?**
- Shared variables for aggregating values across tasks
- Only driver can read the final value
- Tasks can only add to accumulator

**Using Accumulators:**
```python
# Create accumulator
acc = spark.sparkContext.accumulator(0)

# Use in transformation
def add_to_accumulator(x):
    global acc
    acc.add(x)
    return x

rdd.foreach(add_to_accumulator)

# Get value (only on driver)
print(acc.value)
```

**Named Accumulators:**
```python
acc = spark.sparkContext.accumulator(0, "myAccumulator")
rdd.foreach(lambda x: acc.add(x))
print(acc.value)
```

---

### Broadcast Variables

**What are Broadcast Variables?**
- Read-only shared variables cached on each executor
- Efficient for joining small datasets
- Avoids sending data with every task

**Using Broadcast:**
```python
# Create broadcast variable
broadcast_var = spark.sparkContext.broadcast({"key": "value"})

# Use in RDD
rdd.map(lambda x: broadcast_var.value[x])

# Use in DataFrame
df.select(col("key"), lit(broadcast_var.value["key"])).show()

# Get value
broadcast_var.unpersist()  # Release when done
```

---

### Structured Streaming

**What is Structured Streaming?**
- Streaming API built on Spark SQL
- DataFrame/Dataset API for streams
- Fault-tolerant exactly-once semantics

**Basic Example:**
```python
# Read from socket
streaming_df = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

# Process
result = streaming_df.groupBy("value").count()

# Write to console
query = result.writeStream \
    .format("console") \
    .start()

query.awaitTermination()
```

**Sources and Sinks:**
```python
# Kafka
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "topic").load()

df.writeStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "output").start()

# File
df = spark.readStream.format("text").load("input/")

df.writeStream.format("parquet") \
    .option("path", "output/") \
    .option("checkpointLocation", "checkpoint/") \
    .start()
```

---

### Spark MLlib Basics

**Basic ML Pipeline:**
```python
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression

# Prepare data
indexer = StringIndexer(inputCol="category", outputCol="category_index")
assembler = VectorAssembler(inputCols=["features"], outputCol="features_vec")
lr = LogisticRegression(featuresCol="features_vec", labelCol="label")

# Build pipeline
pipeline = Pipeline(stages=[indexer, assembler, lr])

# Train
model = pipeline.fit(training_df)

# Predict
predictions = model.transform(test_df)
```

---

## 10. Integration

### PySpark with Delta Lake

**Setup:**
```bash
pip install delta-spark
```

**Configuration:**
```python
from delta import configure_spark_with_delta_p.builder

spark = configure_spark_with_delta_p.builder \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    .getOrCreate()
```

---

### PySpark with AWS S3

**Configuration:**
```python
spark = SparkSession.builder \
    .config("spark.hadoop.fs.s3a.access.key", "YOUR_ACCESS_KEY") \
    .config("spark.hadoop.fs.s3a.secret.key", "YOUR_SECRET_KEY") \
    .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
    .getOrCreate()

# Read from S3
df = spark.read.parquet("s3a://bucket-name/path/")

# Write to S3
df.write.parquet("s3a://bucket-name/output/")
```

---

### PySpark with Azure Blob Storage

**Configuration:**
```python
spark = SparkSession.builder \
    .config("fs.azure.account.key.YOUR_ACCOUNT.blob.core.windows.net", "YOUR_KEY") \
    .getOrCreate()

# Read
df = spark.read.parquet("wasbs://container@account.blob.core.windows.net/path/")

# Write
df.write.parquet("wasbs://container@account.blob.core.windows.net/output/")
```

---

### PySpark with Databricks

**Using Databricks:**
- Create cluster in Databricks
- Attach notebook
- Run PySpark code directly

**Key Features:**
- Managed Spark environment
- Built-in Delta Lake
- Collaborative notebooks

---

## Quick Reference

### Spark DataFrame Cheat Sheet

| Operation | Code |
|-----------|------|
| Create DataFrame | `spark.createDataFrame(data, schema)` |
| Read CSV | `spark.read.csv("file.csv", header=True, inferSchema=True)` |
| Read JSON | `spark.read.json("file.json")` |
| Read Parquet | `spark.read.parquet("file.parquet")` |
| Select columns | `df.select("col1", "col2")` |
| Filter | `df.filter(col("age") > 25)` |
| Group by | `df.groupBy("dept").agg({"salary": "sum"})` |
| Join | `df1.join(df2, "key")` |
| Create temp view | `df.createOrReplaceTempView("name")` |
| Run SQL | `spark.sql("SELECT * FROM name")` |
| Write CSV | `df.write.csv("path", header=True)` |
| Write Parquet | `df.write.parquet("path")` |

### Common Functions

| Category | Functions |
|----------|-----------|
| String | upper, lower, trim, substring, concat, split |
| Date | current_date, year, month, date_add, datediff |
| Math | abs, round, ceil, floor, sqrt, pow |
| Aggregate | sum, avg, count, min, max |
| Window | row_number, rank, lag, lead |

---

**Happy Learning!**
