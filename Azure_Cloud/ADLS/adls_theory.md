# Azure Data Lake Storage Theory & Tutorial

## Table of Contents
1. [What is ADLS Gen2?](#1-what-is-adls-gen2)
2. [ADLS vs Blob Storage](#2-adls-vs-blob-storage)
3. [Core Concepts](#3-core-concepts)
4. [Data Lake Zones](#4-data-lake-zones)
5. [Security Model](#5-security-model)
6. [Access Control](#6-access-control)
7. [Data Organization](#7-data-organization)
8. [File Formats](#8-file-formats)
9. [Working with ADLS](#9-working-with-adls)
10. [Performance Optimization](#10-performance-optimization)
11. [Lifecycle Management](#11-lifecycle-management)
12. [Integration with Services](#12-integration-with-services)
13. [Monitoring & Logging](#13-monitoring--logging)
14. [Best Practices](#14-best-practices)
15. [Quick Reference](#15-quick-reference)

---

## 1. What is ADLS Gen2?

### 📖 What is Azure Data Lake Storage Gen2?

**Azure Data Lake Storage Gen2 (ADLS Gen2)** is a set of capabilities dedicated to big data analytics, built on top of Azure Blob Storage. It combines the scalability and cost-effectiveness of object storage with the performance and management features of a hierarchical file system.

**Key Capabilities:**
- Hierarchical namespace for file and directory operations
- Compatible with Hadoop Distributed File System (HDFS)
- Scalable to petabytes of data
- Low-cost storage with tiering options
- Enterprise-grade security (RBAC + ACLs)
- High-performance analytics workloads

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    ADLS Gen2 Architecture                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │ Analytics   │    │ Analytics   │    │ Analytics   │     │
│  │ Databricks  │    │ Synapse     │    │ HDInsight   │     │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘     │
│         │                  │                  │              │
│         └──────────────────┼──────────────────┘              │
│                            │                                │
│                            ▼                                │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              HDFS-compatible Interface               │    │
│  │              (abfss://, wasb://, webhdfs://)        │    │
│  └────────────────────────┬────────────────────────────┘    │
│                         │                                   │
│  ┌──────────────────────┴──────────────────────────────┐    │
│  │         Hierarchical Namespace (Flat)              │    │
│  │              /raw/customer/dt=2024-01-01/          │    │
│  │              /curated/sales/region=US/             │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                   │
│  ┌──────────────────────┴──────────────────────────────┐    │
│  │              Azure Blob Storage Foundation         │    │
│  │         (Redundancy, Encryption, Durability)         │    │
│  └──────────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Why is this important for Data Engineering?
- **Decoupled storage and compute** - Use any analytics tool without data movement
- **Cost-effective** - Pay only for storage and transactions used
- **Scalable** - Handle terabytes to petabytes without architecture changes
- **Secure** - Enterprise-grade security for sensitive data
- **Compatible** - Works with existing Hadoop/Spark tools

---

## 2. ADLS vs Blob Storage

### 📖 What is the difference?

| Feature | Blob Storage | ADLS Gen2 |
|---------|--------------|-----------|
| **Namespace** | Flat (container/blob) | Hierarchical (directory/file) |
| **HDFS Compatible** | No | Yes |
| **Analytics Workloads** | Limited | Optimized |
| **Performance** | General purpose | High-throughput analytics |
| **Cost** | Lower base cost | Same + namespace cost |
| **Use Case** | General storage, backups | Big data analytics |

### Storage Account Types

| Type | Best For | Limitations |
|------|----------|-------------|
| **Standard (GPv2)** | General purpose, ADLS Gen2 | None |
| **Premium Block Blob** | Low latency, high transaction rates | Higher cost |

### Hierarchical Namespace

```
Without Hierarchical Namespace (Flat):
┌────────────────────────────────────────────────┐
│ Container: mycontainer                         │
│   - raw/customer/data.parquet                  │
│   - raw/sales/data.parquet                     │
│   - curated/report/output.csv                  │
└────────────────────────────────────────────────┘

With Hierarchical Namespace (ADLS Gen2):
┌────────────────────────────────────────────────┐
│ Container: mycontainer                         │
│   /raw/                                        │
│     /customer/                                 │
│       - data.parquet                           │
│     /sales/                                    │
│       - data.parquet                           │
│   /curated/                                    │
│     /report/                                   │
│       - output.csv                             │
└────────────────────────────────────────────────┘
```

### Why is this important for Data Engineering?
- Hierarchical namespace enables efficient directory operations
- Better performance for analytics workloads
- Compatible with existing big data tools
- More intuitive organization for data lakes

---

## 3. Core Concepts

### 📖 What are the core ADLS concepts?

### Storage Account

A **Storage Account** is the top-level resource that contains all your Azure Storage data objects.

```
Storage Account
├── Containers (File Systems)
│   ├── Directories
│   │   └── Files/Blobs
│   └── Files/Blobs
├── Tables
├── Queues
└── File Shares
```

**Key Properties:**
- Globally unique name (3-24 lowercase letters/numbers)
- Performance tier: Standard or Premium
- Redundancy: LRS, ZRS, GRS, GZRS
- Region: Geographic location

### Container (File System)

A **Container** organizes a set of objects (files/directories). In ADLS Gen2, containers are often called **File Systems**.

```python
# Container characteristics
- Root of the file system
- Holds directories and files
- No nesting of containers
- Unique name within storage account
```

### Directory

**Directories** organize files in a hierarchical structure, similar to traditional file systems.

```
/raw/
  /customer/
    /dt=2024-01-01/
      - part-001.parquet
      - part-002.parquet
    /dt=2024-01-02/
      - part-001.parquet
```

### Blob Types

| Type | Use Case | Characteristics |
|------|----------|-----------------|
| **Block Blob** | General purpose | Up to 190.7 TiB, committed in blocks |
| **Append Blob** | Logging | Optimized for append operations |
| **Page Blob** | VMs, random access | Up to 8 TiB, 512-byte pages |

### Access Tiers

| Tier | Access Frequency | Storage Cost | Access Cost |
|------|------------------|--------------|-------------|
| **Hot** | Frequent | Higher | Lower |
| **Cool** | Infrequent (30+ days) | Lower | Higher |
| **Archive** | Rare (180+ days) | Lowest | Highest |

### Why is this important for Data Engineering?
- Proper account setup affects performance and cost
- Choosing the right tier saves money
- Hierarchical organization improves data discovery
- Understanding blob types optimizes storage

---

## 4. Data Lake Zones

### 📖 What are Data Lake Zones?

**Data Lake Zones** are logical layers in a data lake that represent different stages of data refinement, from raw ingestion to curated business-ready data.

### Zone Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Data Lake Zones                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐     │
│  │     RAW / BRONZE (Landing Zone)                     │     │
│  │  ┌──────────────────────────────────────────────┐   │     │
│  │  │  - Source system data (as-is)              │   │     │
│  │  │  - No transformations                        │   │     │
│  │  │  - Schema-on-read                          │   │     │
│  │  │  - Retention: Long-term                      │   │     │
│  │  └──────────────────────────────────────────────┘   │     │
│  └──────────────────────────┬──────────────────────────┘     │
│                             │                                │
│                             ▼                                │
│  ┌─────────────────────────────────────────────────────┐     │
│  │     SILVER (Cleansed Zone)                          │     │
│  │  ┌──────────────────────────────────────────────┐   │     │
│  │  │  - Cleaned data                            │   │     │
│  │  │  - Deduplicated                            │   │     │
│  │  │  - Schema enforced                         │   │     │
│  │  │  - Delta format                            │   │     │
│  │  └──────────────────────────────────────────────┘   │     │
│  └──────────────────────────┬──────────────────────────┘     │
│                             │                                │
│                             ▼                                │
│  ┌─────────────────────────────────────────────────────┐     │
│  │     GOLD (Curated Zone)                             │     │
│  │  ┌──────────────────────────────────────────────┐   │     │
│  │  │  - Business aggregates                       │   │     │
│  │  │  - Report-ready tables                     │   │     │
│  │  │  - Optimized for querying                    │   │     │
│  │  │  - Star schema / denormalized              │   │     │
│  │  └──────────────────────────────────────────────┘   │     │
│  └─────────────────────────────────────────────────────┘     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Zone Details

| Zone | Also Called | Purpose | Retention |
|------|-------------|---------|-----------|
| **Raw** | Bronze, Landing | Store data exactly as received | Indefinite |
| **Silver** | Cleansed, Standardized | Cleaned, deduplicated, conformed | Years |
| **Gold** | Curated, Consumption | Business-ready aggregates | Months-Years |

### Folder Structure Example

```
/raw/
  /source_system_a/
    /table_name/
      /dt=2024-01-01/
        - part-001.parquet
        - part-002.parquet

/silver/
  /domain_name/
    /table_name/
      /dt=2024-01-01/
        - data.delta

/gold/
  /analytics/
    /report_name/
      /aggregate_name/
        - data.delta
```

### Why is this important for Data Engineering?
- Clear data lineage and governance
- Supports "schema-on-read" flexibility
- Enables incremental data refinement
- Facilitates data quality at each layer
- Supports different access patterns per zone

---

## 5. Security Model

### 📖 What is the ADLS Security Model?

**ADLS Security** uses a layered approach combining Azure RBAC, POSIX-style ACLs, and network controls to protect data at every level.

### Security Layers

```
┌─────────────────────────────────────────────────────────────┐
│                  ADLS Security Layers                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Layer 1: Network Controls                                   │
│  ├── Private Endpoints                                       │
│  ├── Service Endpoints                                       │
│  ├── Firewall Rules                                          │
│  └── Virtual Network Integration                             │
│                                                             │
│  Layer 2: Identity & Access                                 │
│  ├── Azure RBAC (Subscription/Resource level)                │
│  └── Shared Key / SAS Tokens                                 │
│                                                             │
│  Layer 3: Data Access (ACLs)                                 │
│  ├── Access Control Lists (ACLs)                             │
│  ├── Owner, Group, Other permissions                         │
│  └── Default ACLs (inheritance)                              │
│                                                             │
│  Layer 4: Data Protection                                    │
│  ├── Encryption at Rest (Azure-managed keys)                 │
│  ├── Encryption in Transit (TLS 1.2)                       │
│  ├── Customer-managed keys (CMK)                           │
│  └── Immutable storage (WORM)                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### RBAC vs ACL

| Control | Scope | Use Case |
|---------|-------|----------|
| **RBAC** | Storage account, container | Management operations |
| **ACL** | Directory, file | Data access operations |

### RBAC Roles for ADLS

| Role | Purpose |
|------|---------|
| **Storage Blob Data Owner** | Full control including ACL management |
| **Storage Blob Data Contributor** | Read, write, delete (no ACL management) |
| **Storage Blob Data Reader** | Read-only access |
| **Storage Account Contributor** | Account management (not data access) |

### Why is this important for Data Engineering?
- Protect sensitive data at multiple levels
- Implement least-privilege access
- Meet compliance requirements
- Enable secure multi-team collaboration

---

## 6. Access Control

### 📖 How does Access Control work?

### Access Control Lists (ACLs)

**ACLs** are POSIX-style permissions assigned to files and directories.

```
Permission Structure:
┌──────────┬──────────┬──────────┐
│  Owner   │  Group   │  Other   │
├──────────┼──────────┼──────────┤
│  rwx     │  rwx     │  rwx     │
└──────────┴──────────┴──────────┘

r = read (4)
w = write (2)
x = execute (1) - required for directory traversal

Examples:
755 = rwxr-xr-x (Owner full, others read+execute)
700 = rwx------ (Owner only)
```

### ACL Types

| Type | Purpose | Behavior |
|------|---------|----------|
| **Access ACL** | Controls access to object | Applies to file/directory |
| **Default ACL** | Template for child objects | Only on directories |

### Setting ACLs

```python
# Azure SDK for Python example
from azure.storage.filedatalake import DataLakeServiceClient

service_client = DataLakeServiceClient(
    account_url="https://mystorage.dfs.core.windows.net",
    credential=credential
)

file_system_client = service_client.get_file_system_client("mycontainer")

directory_client = file_system_client.get_directory_client("/raw/customer")

# Set ACL
directory_client.set_access_control_recursive(
    acl="user::rwx,group::r-x,other::---"
)

# Set ACL for specific user
directory_client.set_access_control_recursive(
    acl="user:object_id:rwx,default:user:object_id:rwx"
)
```

### Authentication Methods

| Method | Use Case | Security Level |
|--------|----------|----------------|
| **Managed Identity** | Azure services | Best |
| **Service Principal** | Automated processes | Good |
| **SAS Token** | Time-limited access | Good |
| **Account Key** | Testing only | Avoid in production |

### SAS Token Example

```python
from azure.storage.filedatalake import generate_file_system_sas
from azure.storage.filedatalake import FileSystemSasPermissions
from datetime import datetime, timedelta

sas_token = generate_file_system_sas(
    account_name="mystorage",
    file_system_name="mycontainer",
    account_key=account_key,
    permission=FileSystemSasPermissions(read=True, write=True),
    expiry=datetime.utcnow() + timedelta(hours=1)
)

# URL: https://mystorage.dfs.core.windows.net/mycontainer?sas_token
```

### Why is this important for Data Engineering?
- Fine-grained access control per folder/file
- Support for multi-tenant data lakes
- Audit and compliance tracking
- Secure data sharing with SAS tokens

---

## 7. Data Organization

### 📖 How to organize data in ADLS?

### Partitioning Strategies

| Strategy | Pattern | Best For |
|----------|---------|----------|
| **Date** | `/dt=2024-01-01/` | Time-series data |
| **Region** | `/region=US/` | Geographic data |
| **Category** | `/category=electronics/` | Categorical data |
| **Combined** | `/region=US/dt=2024-01-01/` | Complex queries |

### Folder Naming Conventions

```
Good:
/raw/source_system/table_name/dt=2024-01-01/
/silver/domain/entity/region=US/dt=2024-01-01/

Avoid:
/raw/Table Name/2024/01/01/ (spaces, deep nesting)
/RAW/SYSTEM/TABLE/ (inconsistent casing)
```

### File Size Recommendations

| Format | Recommended Size | Why |
|--------|------------------|-----|
| **Parquet** | 128 MB - 1 GB | Optimal for columnar reads |
| **CSV** | 64 MB - 256 MB | Balance between overhead and parallelism |
| **Delta** | 1 GB - 4 GB | Transaction efficiency |
| **JSON** | 64 MB - 128 MB | Parsing efficiency |

### Small File Problem

**Problem:** Too many small files hurt query performance

**Solutions:**
- Use coalesce() or repartition() in Spark
- Enable file compaction (Delta Lake auto-optimize)
- Batch writes instead of streaming
- Use optimal partition sizes

```python
# Spark - Fix small files
df.coalesce(10).write.parquet("path")  # Reduce to 10 files

# Delta Lake - Auto-optimize
spark.conf.set("spark.databricks.delta.autoCompact.enabled", "true")
spark.conf.set("spark.databricks.delta.optimizeWrite.enabled", "true")
```

### Why is this important for Data Engineering?
- Proper organization improves query performance
- Partitioning enables partition pruning
- Naming conventions support automation
- File sizing affects distributed processing

---

## 8. File Formats

### 📖 What file formats work best with ADLS?

### Format Comparison

| Format | Structure | Compression | Best For |
|--------|-----------|-------------|----------|
| **Parquet** | Columnar | Built-in | Analytics, DW |
| **Delta** | Columnar + transactions | Built-in | Lakehouse |
| **Avro** | Row-based | Built-in | Streaming, Kafka |
| **ORC** | Columnar | Built-in | Hive workloads |
| **JSON** | Semi-structured | Gzip | APIs, nested data |
| **CSV** | Row-based | Gzip | Simple interchange |

### Parquet Example

```python
# Read Parquet from ADLS
spark.read.parquet("abfss://container@storage.dfs.core.windows.net/raw/data.parquet")

# Write optimized Parquet
df.write \
  .option("parquet.block.size", 134217728) \  # 128 MB
  .parquet("abfss://.../curated/data.parquet")
```

### Delta Lake on ADLS

```python
# Read Delta table
df = spark.read.format("delta").load(
    "abfss://container@storage.dfs.core.windows.net/silver/customer"
)

# Write to Delta with merge
df.write \
  .format("delta") \
  .mode("overwrite") \
  .save("abfss://.../silver/customer")

# Time travel
spark.read \
  .format("delta") \
  .option("versionAsOf", 0) \
  .load("abfss://.../silver/customer")
```

### Format Selection Guide

```
Need transactions? ──Yes──▶ Delta
             │
             No
             │
             ▼
Columnar query ──Yes──▶ Parquet
             │
             No
             │
             ▼
Streaming? ──Yes──▶ Avro
             │
             No
             │
             ▼
        CSV/JSON (simple)
```

### Why is this important for Data Engineering?
- Columnar formats reduce I/O for analytics
- Compression saves storage costs
- Format choice affects query performance
- Delta Lake enables ACID transactions

---

## 9. Working with ADLS

### 📖 How to work with ADLS programmatically?

### Connection Strings

**ABFSS (Azure Blob File System Secure)**
```
abfss://container@storageaccount.dfs.core.windows.net/path
```

**WASB (Legacy)**
```
wasb://container@storageaccount.blob.core.windows.net/path
```

### Python - Azure SDK

```python
from azure.storage.filedatalake import DataLakeServiceClient
from azure.identity import DefaultAzureCredential

# Authenticate
credential = DefaultAzureCredential()
service_client = DataLakeServiceClient(
    account_url="https://mystorage.dfs.core.windows.net",
    credential=credential
)

# Create file system
file_system_client = service_client.create_file_system("raw")

# Create directory
directory_client = file_system_client.create_directory("customer")

# Upload file
file_client = directory_client.get_file_client("data.parquet")
with open("local_file.parquet", "rb") as data:
    file_client.upload_data(data, overwrite=True)

# List files
paths = file_system_client.get_paths(path="/customer")
for path in paths:
    print(path.name)

# Download file
with open("download.parquet", "wb") as file:
    downloader = file_client.download_file()
    file.write(downloader.readall())

# Delete file
file_client.delete_file()
```

### PySpark

```python
# Configuration
spark.conf.set("fs.azure.account.auth.type.mystorage.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.mystorage.dfs.core.windows.net",
               "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.mystorage.dfs.core.windows.net",
               "<client-id>")
spark.conf.set("fs.azure.account.oauth2.client.secret.mystorage.dfs.core.windows.net",
               "<secret>")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.mystorage.dfs.core.windows.net",
               "https://login.microsoftonline.com/<tenant-id>/oauth2/token")

# Read
df = spark.read.parquet("abfss://raw@mystorage.dfs.core.windows.net/customer/data.parquet")

# Write
df.write \
  .mode("overwrite") \
  .parquet("abfss://curated@mystorage.dfs.core.windows.net/customer/output.parquet")

# Partitioned write
df.write \
  .partitionBy("dt", "region") \
  .parquet("abfss://raw@mystorage.dfs.core.windows.net/sales/")
```

### Azure CLI

```bash
# Create storage account
az storage account create \
  --name mystorage \
  --resource-group myrg \
  --location eastus \
  --sku Standard_LRS \
  --enable-hierarchical-namespace true

# Create container
az storage fs create \
  --name raw \
  --account-name mystorage

# Upload file
az storage fs file upload \
  --file-system raw \
  --path customer/data.parquet \
  --source ./data.parquet \
  --account-name mystorage

# List files
az storage fs file list \
  --file-system raw \
  --path customer \
  --account-name mystorage

# Set ACL
az storage fs access set \
  --file-system raw \
  --path customer \
  --acl "user::rwx,group::r-x,other::---" \
  --account-name mystorage
```

### Why is this important for Data Engineering?
- Automate data ingestion and extraction
- Integrate with ETL pipelines
- Enable programmatic access control
- Support CI/CD for infrastructure

---

## 10. Performance Optimization

### 📖 How to optimize ADLS performance?

### Throughput Factors

| Factor | Impact | Recommendation |
|--------|--------|----------------|
| **File size** | High | 128 MB - 1 GB |
| **Parallelism** | High | Match compute cores |
| **Partitioning** | Medium | Align with query patterns |
| **Compression** | Medium | Use Snappy or Zstd |
| **Network** | Low-Medium | Use same region |

### Spark + ADLS Optimization

```python
# Optimal settings for ADLS
spark.conf.set("spark.sql.files.maxPartitionBytes", "134217728")  # 128 MB
spark.conf.set("spark.sql.shuffle.partitions", "200")

# Read with partitioning
df = spark.read.parquet("abfss://.../raw/data/")

# Repartition for optimal write
df.repartition(10).write.parquet("abfss://.../curated/data/")

# Coalesce for fewer files (after aggregation)
df.coalesce(5).write.parquet("abfss://.../output/")
```

### Caching Strategies

| Strategy | Use Case | Considerations |
|----------|----------|----------------|
| **Spark Cache** | Repeated reads | Memory usage |
| **Delta Cache** | Databricks | Automatic optimization |
| **CDN** | Global access | Additional cost |

### Why is this important for Data Engineering?
- Reduces query latency
- Maximizes throughput
- Controls compute costs
- Improves user experience

---

## 11. Lifecycle Management

### 📖 What is Lifecycle Management?

**Lifecycle Management Policies** automatically manage data throughout its lifecycle, moving data between access tiers or deleting it based on rules.

### Policy Rules

| Rule Action | Use Case | Example |
|-------------|----------|---------|
| **Tier to Cool** | Data not accessed recently | After 30 days in Hot |
| **Tier to Archive** | Long-term retention | After 180 days in Cool |
| **Delete** | Data expiration | After 2555 days |

### JSON Policy Example

```json
{
  "rules": [
    {
      "name": "rawToCool",
      "enabled": true,
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": ["blockBlob"],
          "prefixMatch": ["raw/"]
        },
        "actions": {
          "baseBlob": {
            "tierToCool": { "daysAfterModificationGreaterThan": 30 },
            "tierToArchive": { "daysAfterModificationGreaterThan": 90 },
            "delete": { "daysAfterModificationGreaterThan": 2555 }
          }
        }
      }
    }
  ]
}
```

### Azure CLI

```bash
# Set lifecycle policy
az storage account management-policy create \
  --account-name mystorage \
  --policy @policy.json

# Show policy
az storage account management-policy show \
  --account-name mystorage
```

### Why is this important for Data Engineering?
- Automatic cost optimization
- Compliance with retention policies
- Reduces manual data management
- Supports data governance

---

## 12. Integration with Services

### 📖 How does ADLS integrate with other services?

### Integration Architecture

```
                    ┌─────────────────────────────────┐
                    │         ADLS Gen2               │
                    │    (Central Storage Layer)      │
                    └───────────────┬─────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────┐         ┌───────────────┐         ┌───────────────┐
│  Azure Data   │         │  Azure        │         │  Azure        │
│  Factory      │         │  Databricks   │         │  Synapse      │
│               │         │               │         │  Analytics    │
│ Orchestration │         │ Processing    │         │ Warehousing   │
│ Movement      │         │ ML/AI         │         │ SQL Analytics │
└───────────────┘         └───────────────┘         └───────────────┘
```

### Integration Patterns

| Service | Pattern | Protocol |
|---------|---------|----------|
| **ADF** | Orchestration + Copy | abfss:// |
| **Databricks** | Processing + ML | dbfs:/mnt/ |
| **Synapse** | SQL analytics | abfss:// |
| **Event Grid** | Event-driven | HTTPS |
| **Functions** | Serverless processing | SDK |

### Databricks Mount Example

```python
# Mount ADLS to Databricks
dbutils.fs.mount(
  source = "abfss://raw@mystorage.dfs.core.windows.net",
  mount_point = "/mnt/raw",
  extra_configs = configs
)

# Access as local path
df = spark.read.parquet("/mnt/raw/customer/data.parquet")
```

### Event Grid Integration

```python
# Trigger on blob creation
# Event Grid subscription -> Event Hub/Function -> Process

{
  "topic": "/subscriptions/.../resourceGroups/.../providers/Microsoft.Storage/storageAccounts/mystorage",
  "subject": "/blobServices/default/containers/raw/blobs/customer/data.parquet",
  "eventType": "Microsoft.Storage.BlobCreated",
  "eventTime": "2024-01-01T00:00:00.000Z",
  "data": {
    "api": "PutBlob",
    "url": "https://mystorage.blob.core.windows.net/raw/customer/data.parquet"
  }
}
```

### Why is this important for Data Engineering?
- Central storage for data platform
- Decouples storage from compute
- Enables best-of-breed analytics tools
- Supports event-driven architectures

---

## 13. Monitoring & Logging

### 📖 How to monitor ADLS?

### Monitoring Tools

| Tool | Purpose | Data Retained |
|------|---------|---------------|
| **Azure Monitor** | Metrics, alerts | 93 days |
| **Diagnostic Logs** | Detailed operations | Configurable |
| **Storage Analytics** | Legacy logging | Configurable |

### Key Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| **Transactions** | Request count | Baseline + 50% |
| **Ingress** | Data uploaded | None |
| **Egress** | Data downloaded | Budget-based |
| **Availability** | Service health | < 99.9% |
| **Latency** | Response time | > 100ms |

### Diagnostic Settings

```json
{
  "logs": [
    {
      "category": "StorageRead",
      "enabled": true,
      "retentionPolicy": { "days": 30 }
    },
    {
      "category": "StorageWrite",
      "enabled": true,
      "retentionPolicy": { "days": 30 }
    }
  ],
  "metrics": [
    {
      "category": "Transaction",
      "enabled": true
    }
  ]
}
```

### Why is this important for Data Engineering?
- Track data access patterns
- Detect security anomalies
- Optimize costs
- Troubleshoot performance issues

---

## 14. Best Practices

### 📖 What are ADLS best practices?

### Security

| Practice | Implementation |
|----------|---------------|
| Use Managed Identity | Enable on services, grant minimal RBAC |
| Enable firewall | Restrict to VNet/service endpoints |
| Private endpoints | For sensitive data access |
| Soft delete | Enable for accidental deletion recovery |
| Encryption | Use customer-managed keys for compliance |

### Organization

| Practice | Implementation |
|----------|---------------|
| Naming convention | lowercase-with-hyphens |
| Folder structure | zone/source/entity/partition |
| Metadata tagging | Use Azure tags for classification |
| Versioning | Use Delta Lake for table versioning |

### Performance

| Practice | Implementation |
|----------|---------------|
| File size | Target 128 MB - 1 GB |
| Compression | Snappy for Parquet |
| Partitioning | Date-based for time-series |
| Co-location | Storage and compute in same region |

### Cost

| Practice | Implementation |
|----------|---------------|
| Tiering | Lifecycle policies for archival |
| Reserved capacity | For predictable workloads |
| Transaction batching | Reduce API calls |
| Cleanup | Remove temporary files |

### Why is this important for Data Engineering?
- Reduces operational overhead
- Ensures security compliance
- Optimizes costs
- Improves reliability

---

## 15. Quick Reference

### URL Formats

| Protocol | Format |
|----------|--------|
| ABFSS | `abfss://container@account.dfs.core.windows.net/path` |
| WASB | `wasb://container@account.blob.core.windows.net/path` |
| Blob | `https://account.blob.core.windows.net/container/path` |
| DFS | `https://account.dfs.core.windows.net/container/path` |

### RBAC Permissions

| Permission | Read | Write | Full |
|------------|------|-------|------|
| Read data | ✓ | ✓ | ✓ |
| Write data | ✗ | ✓ | ✓ |
| Modify ACLs | ✗ | ✗ | ✓ |

### ACL Reference

| Octal | Symbolic | Meaning |
|-------|----------|---------|
| 7 | rwx | Full |
| 6 | rw- | Read + Write |
| 5 | r-x | Read + Execute |
| 4 | r-- | Read only |
| 0 | --- | No access |

### Storage Tiers Cost Comparison

| Tier | Storage Cost | Access Cost | Best For |
|------|--------------|-------------|----------|
| Hot | $$$ | $ | Active data |
| Cool | $$ | $$ | 30+ days |
| Archive | $ | $$$ | 180+ days |

### File Size Guidelines

| Data Volume | Target Files | File Size |
|-------------|--------------|-----------|
| < 1 GB | 4-8 | 128-256 MB |
| 1-100 GB | 10-100 | 128 MB - 1 GB |
| > 100 GB | 100+ | 1 GB |

### Common Commands

```bash
# Azure CLI
az storage fs create --name raw --account-name mystorage
az storage fs file upload --file-system raw --path file --source local
az storage fs file list --file-system raw --account-name mystorage

# Python
service_client = DataLakeServiceClient(account_url, credential)
file_client = service_client.get_file_client(container, path)
file_client.upload_data(data, overwrite=True)

# PySpark
df.write.parquet("abfss://container@account.dfs.core.windows.net/path")
```

---

**Happy Learning! Remember: Practice makes perfect.**
