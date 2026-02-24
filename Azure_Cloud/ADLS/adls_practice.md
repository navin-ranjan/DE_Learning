# Azure Data Lake Storage Practice Exercises

Practice your Azure Data Lake Storage (ADLS Gen2) skills with these exercises.

---

## Setup - Sample Environment

```python
# Configuration for ADLS
storage_account_name = "mystorageaccount"
container_name = "datalake"
connection_string = "DefaultEndpointsProtocol=https;AccountName=...;AccountKey=...;EndpointSuffix=core.windows.net"

# ABFSS URL format
abfss_path = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/"
```

---

## Exercise Set 1: Storage Account & Container

### Exercise 1.1: Create Storage Account
Create a storage account with hierarchical namespace enabled using Azure CLI.

```bash
# YOUR CODE HERE:
# Create storage account with ADLS Gen2 enabled
```

### Exercise 1.2: Create Container (File System)
Create a container named "raw" in the storage account.

```bash
# YOUR CODE HERE:
```

### Exercise 1.3: Create Multiple Containers
Create three containers: raw, silver, gold.

```bash
# YOUR CODE HERE:
```

### Exercise 1.4: Configure Redundancy
Create a storage account with GRS (Geo-Redundant Storage) redundancy.

```bash
# YOUR CODE HERE:
```

---

## Exercise Set 2: Directory & File Operations

### Exercise 2.1: Create Directory Structure
Create the following directory structure:
```
/raw/
  /customer/
    /dt=2024-01-01/
  /orders/
/silver/
  /customer/
/gold/
  /analytics/
```

```python
# YOUR CODE HERE:
from azure.storage.filedatalake import DataLakeServiceClient

# Connect and create directories
```

### Exercise 2.2: Upload File to ADLS
Upload a local CSV file to the raw/customer folder.

```python
# YOUR CODE HERE:
# Use DataLakeServiceClient to upload a file
```

### Exercise 2.3: Download File from ADLS
Download a file from ADLS to local storage.

```python
# YOUR CODE HERE:
```

### Exercise 2.4: List Files in Directory
List all files in the /raw/customer/dt=2024-01-01/ directory.

```python
# YOUR CODE HERE:
```

### Exercise 2.5: Delete File
Delete a file from ADLS.

```python
# YOUR CODE HERE:
```

---

## Exercise Set 3: PySpark Integration

### Exercise 3.1: Configure Spark for ADLS
Set up Spark configuration to connect to ADLS using OAuth.

```python
# YOUR CODE HERE:
# Set account auth type, OAuth provider, client ID, secret, and endpoint
```

### Exercise 3.2: Read Parquet from ADLS
Read a Parquet file from ADLS into a Spark DataFrame.

```python
# YOUR CODE HERE:
# Read from: abfss://raw@storage.dfs.core.windows.net/customer/data.parquet
```

### Exercise 3.3: Write DataFrame to ADLS
Write a Spark DataFrame to ADLS in Parquet format.

```python
# YOUR CODE HERE:
# Write to: abfss://silver@storage.dfs.core.windows.net/customer/output/
```

### Exercise 3.4: Partitioned Write
Write data with partition by date and region.

```python
# YOUR CODE HERE:
# Partition by "dt" and "region" columns
```

### Exercise 3.5: Read Partitioned Data
Read partitioned Parquet files with partition discovery.

```python
# YOUR CODE HERE:
# Use partition discovery to read partitioned data
```

---

## Exercise Set 4: File Formats

### Exercise 4.1: Read CSV with Schema
Read a CSV file from ADLS with explicit schema definition.

```python
# YOUR CODE HERE:
# Define schema and read CSV
```

### Exercise 4.2: Write Parquet with Compression
Write data to Parquet with Snappy compression.

```python
# YOUR CODE HERE:
# Use compression codec snappy
```

### Exercise 4.3: Read JSON Files
Read JSON files from ADLS with nested structure.

```python
# YOUR CODE HERE:
# Read multi-line JSON
```

### Exercise 4.4: Convert CSV to Parquet
Read CSV from raw zone and write as Parquet to silver zone.

```python
# YOUR CODE HERE:
# ETL: CSV -> Parquet
```

---

## Exercise Set 5: Delta Lake

### Exercise 5.1: Write Delta Table
Write data to Delta format on ADLS.

```python
# YOUR CODE HERE:
# Write in delta format
```

### Exercise 5.2: Read Delta Table
Read data from a Delta table.

```python
# YOUR CODE HERE:
```

### Exercise 5.3: Delta Merge (Upsert)
Perform MERGE operation to insert/update records.

```python
# YOUR CODE HERE:
# Use Delta merge for incremental updates
```

### Exercise 5.4: Time Travel
Read a previous version of the Delta table.

```python
# YOUR CODE HERE:
# Use versionAsOf or timestampAsOf
```

### Exercise 5.5: Delta Optimize
Optimize Delta table to reduce small files.

```python
# YOUR CODE HERE:
# Use optimize and Z-order by
```

---

## Exercise Set 6: Security & Access Control

### Exercise 6.1: Generate SAS Token
Generate a SAS token for read access to a container.

```python
# YOUR CODE HERE:
# Use generate_file_system_sas
```

### Exercise 6.2: Set ACL on Directory
Set ACL permissions on a directory (rwx for owner, r-x for group).

```python
# YOUR CODE HERE:
# Use set_access_control_recursive
```

### Exercise 6.3: Configure RBAC Role
Assign "Storage Blob Data Contributor" role to a user.

```bash
# YOUR CODE HERE:
# Use az role assignment create
```

### Exercise 6.4: Use Managed Identity
Configure a service (e.g., Databricks) to access ADLS using Managed Identity.

```python
# YOUR CODE HERE:
# Configure spark to use managed identity
```

### Exercise 6.5: Key Vault Secret for Connection
Store the storage account key in Key Vault and reference it.

```python
# YOUR CODE HERE:
# Use Azure Key Vault to store and retrieve secrets
```

---

## Exercise Set 7: Performance Optimization

### Exercise 7.1: Repartition Data
Repartition data to optimal number of files before writing.

```python
# YOUR CODE HERE:
# Use repartition() to control file count
```

### Exercise 7.2: Coalesce Files
Reduce number of files after aggregation using coalesce.

```python
# YOUR CODE HERE:
```

### Exercise 7.3: Configure Spark Partition Size
Set optimal partition byte size for file reading.

```python
# YOUR CODE HERE:
# Set spark.sql.files.maxPartitionBytes
```

### Exercise 7.4: Parallel Read Configuration
Configure number of partitions for reads.

```python
# YOUR CODE HERE:
# Set spark.sql.shuffle.partitions
```

### Exercise 7.5: Cache Frequently Accessed Data
Cache a DataFrame for repeated access.

```python
# YOUR CODE HERE:
# Use df.cache() or df.persist()
```

---

## Exercise Set 8: Lifecycle Management

### Exercise 8.1: Create Lifecycle Policy
Create a lifecycle policy to move blobs from Hot to Cool after 30 days.

```json
// YOUR CODE HERE:
{
  "rules": [
    {
      "name": "moveToCool",
      "enabled": true,
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": ["blockBlob"],
          "prefixMatch": ["raw/"]
        },
        "actions": {
          "baseBlob": {
            "tierToCool": {"daysAfterModificationGreaterThan": 30}
          }
        }
      }
    }
  ]
}
```

### Exercise 8.2: Archive Old Data
Create policy to move data to Archive tier after 90 days.

```json
// YOUR CODE HERE:
```

### Exercise 8.3: Delete Expired Data
Create policy to delete data older than 7 years.

```json
// YOUR CODE HERE:
```

---

## Exercise Set 9: Data Organization

### Exercise 9.1: Implement Date Partitioning
Create folder structure with date partitioning: /raw/table/dt=YYYY-MM-DD/

```python
# YOUR CODE HERE:
# Write with partitionBy("dt")
```

### Exercise 9.2: Multi-Level Partitioning
Create partitioning by region and date: /sales/region=US/dt=2024-01-01/

```python
# YOUR CODE HERE:
```

### Exercise 9.3: Fix Small Files Problem
Address the small file problem by compacting files.

```python
# YOUR CODE HERE:
# Read all small files, repartition, and write back
```

### Exercise 9.4: Implement Proper Naming Convention
Create a function to generate standardized folder paths.

```python
# YOUR CODE HERE:
# zone/source/entity/partition=value/
```

---

## Exercise Set 10: Monitoring & Diagnostics

### Exercise 10.1: Enable Diagnostic Logs
Enable storage analytics to log read/write operations.

```bash
# YOUR CODE HERE:
# Use az monitor diagnostic-settings create
```

### Exercise 10.2: Check Metrics
Query for storage metrics (transactions, egress, latency).

```python
# YOUR CODE HERE:
# Use Azure Monitor SDK to query metrics
```

### Exercise 10.3: Analyze Access Patterns
List files that were accessed in the last 7 days.

```python
# YOUR CODE HERE:
# Use get_paths with modified since filter
```

---

## Exercise Set 11: Integration with Azure Services

### Exercise 11.1: Mount ADLS in Databricks
Mount ADLS container to Databricks.

```python
# YOUR CODE HERE:
# Use dbutils.fs.mount()
```

### Exercise 11.2: ADF Copy to ADLS
Configure ADF to copy data from SQL to ADLS.

```json
// YOUR CODE HERE:
// Create linked service and dataset for ADLS
```

### Exercise 11.3: Event Grid Trigger
Set up Event Grid to trigger a function when a blob is created.

```python
# YOUR CODE HERE:
# Configure Event Grid subscription
```

---

## Challenge Exercises

### Challenge 1: Build Bronze-Silver-Gold Pipeline
Create a complete pipeline:
1. Read raw CSV from /raw/
2. Clean and transform data (silver)
3. Aggregate to gold layer

```python
# YOUR CODE HERE:



```

### Challenge 2: Incremental Data Loading
Implement incremental loading with Delta Lake:
1. Track watermark
2. Read new data only
3. Merge into existing table

```python
# YOUR CODE HERE:



```

### Challenge 3: Secure Multi-Tenant Access
Create secure access for multiple teams:
1. Team A: Access only /raw/sales/
2. Team B: Access only /silver/marketing/
3. Use ACLs for separation

```python
# YOUR CODE HERE:



```

---

## Testing Your ADLS Code

### Common Commands

```bash
# Azure CLI - List containers
az storage container list --account-name mystorage

# Azure CLI - Upload file
az storage fs file upload --file-system raw --path data/file.csv --source ./file.csv

# Azure CLI - Download file
az storage fs file download --file-system raw --path data/file.csv --destination ./download.csv

# Azure CLI - Set ACL
az storage fs access set --file-system raw --path data --acl "user::rwx,group::r-x,other::---"

# PySpark - Test read
df = spark.read.parquet("abfss://raw@storage.dfs.core.windows.net/data/")
df.show()
```

---

## Practice Complete!

After completing these exercises, you should be comfortable with:
- Creating and configuring ADLS storage accounts
- Managing directories and files
- Integrating ADLS with PySpark
- Working with different file formats (CSV, Parquet, JSON)
- Using Delta Lake for ACID transactions
- Managing security with RBAC and ACLs
- Optimizing performance
- Implementing lifecycle management
- Monitoring and diagnostics

---

## Next Steps

1. Deploy these solutions in Azure
2. Integrate with Azure Data Factory pipelines
3. Set up Databricks for data processing
4. Implement proper security governance
5. Set up monitoring dashboards
