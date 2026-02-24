# Azure Data Factory Practice Exercises

Practice your Azure Data Factory skills with these exercises.

---

## Setup - Sample Data

```json
// Sample Source Tables
// SQL Source: Azure SQL Database - salesdb
// Tables: customers, orders, products

// customers table
| customer_id | name | email | city | created_at |
|-------------|------|-------|------|------------|
| 1 | John | john@email.com | NYC | 2024-01-01 |
| 2 | Jane | jane@email.com | LA | 2024-01-02 |
| 3 | Bob | bob@email.com | Chicago | 2024-01-03 |

// orders table
| order_id | customer_id | amount | order_date | status |
|----------|-------------|--------|------------|--------|
| 101 | 1 | 150.00 | 2024-01-15 | completed |
| 102 | 2 | 200.00 | 2024-01-16 | pending |
| 103 | 1 | 75.00 | 2024-01-17 | completed |

// Sample Target: ADLS Gen2
// Container: datalake
// Folders: raw/, curated/
```

---

## Exercise Set 1: Linked Services

### Exercise 1.1: Create Azure SQL Linked Service
Create a linked service to connect to Azure SQL Database using Managed Identity.

```json
// YOUR CODE HERE:
{
  "name": "ls_azure_sql",
  // Add properties for Azure SQL with Managed Identity
}
```

### Exercise 1.2: Create ADLS Gen2 Linked Service
Create a linked service for ADLS Gen2 using SAS authentication.

```json
// YOUR CODE HERE:
{
  "name": "ls_adls_datalake",
  // Add properties
}
```

### Exercise 1.3: Create Key Vault Reference
Add password reference from Azure Key Vault to a linked service.

```json
// YOUR CODE HERE:
{
  "name": "ls_sql_with_keyvault",
  // Add Key Vault secret reference
}
```

### Exercise 1.4: Self-Hosted IR for On-Premises
Create a linked service for on-premises SQL Server using Self-hosted IR.

```json
// YOUR CODE HERE:
{
  "name": "ls_onprem_sql",
  // Add self-hosted IR reference
}
```

---

## Exercise Set 2: Datasets

### Exercise 2.1: Azure SQL Dataset
Create a dataset pointing to the customers table in Azure SQL.

```json
// YOUR CODE HERE:
{
  "name": "ds_sql_customers",
  // Add properties for Azure SQL table
}
```

### Exercise 2.2: Parquet Dataset
Create a dataset for reading Parquet files from ADLS.

```json
// YOUR CODE HERE:
{
  "name": "ds_adls_parquet",
  // Add Parquet file properties
}
```

### Exercise 2.3: Parameterized Dataset
Create a dataset with parameters for table name and folder path.

```json
// YOUR CODE HERE:
{
  "name": "ds_dynamic_parquet",
  "properties": {
    "parameters": {
      // Add tableName and partitionDate parameters
    },
    // Add typeProperties with dynamic expressions
  }
}
```

### Exercise 2.4: CSV Dataset with Schema
Create a CSV dataset with specified schema definition.

```json
// YOUR CODE HERE:
{
  "name": "ds_csv_orders",
  // Add CSV properties with schema
}
```

---

## Exercise Set 3: Basic Pipeline & Copy Activity

### Exercise 3.1: Simple Copy Pipeline
Create a pipeline that copies data from Azure SQL to ADLS.

```json
// YOUR CODE HERE:
{
  "name": "pl_copy_customers",
  "properties": {
    "activities": [
      {
        "name": "CopyCustomers",
        "type": "Copy",
        // Add source (Azure SQL) and sink (ADLS)
      }
    ]
  }
}
```

### Exercise 3.2: Copy with Query Filter
Copy only orders from the last 30 days using sqlReaderQuery.

```json
// YOUR CODE HERE:
{
  "name": "pl_copy_recent_orders",
  "properties": {
    "parameters": {
      "daysBack": {"type": "int", "defaultValue": 30}
    },
    "activities": [
      {
        "name": "CopyOrders",
        "type": "Copy",
        "typeProperties": {
          "source": {
            "type": "SqlSource",
            // Add sqlReaderQuery with parameter
          },
          "sink": {
            "type": "ParquetSink"
          }
        }
      }
    ]
  }
}
```

### Exercise 3.3: Copy with Column Mapping
Map source columns to different sink columns.

```json
// YOUR CODE HERE:
{
  "name": "pl_copy_with_mapping",
  "typeProperties": {
    "translator": {
      // Add column mapping
    }
  }
}
```

---

## Exercise Set 4: Control Flow - ForEach

### Exercise 4.1: ForEach Loop
Create a pipeline that loops through a list of tables and copies each.

```json
// YOUR CODE HERE:
{
  "name": "pl_copy_all_tables",
  "properties": {
    "activities": [
      {
        "name": "LookupTables",
        "type": "Lookup",
        // Return list of tables: ["customers", "orders", "products"]
      },
      {
        "name": "ForEachTable",
        "type": "ForEach",
        "dependsOn": [{"activity": "LookupTables", "dependencyConditions": ["Succeeded"]}],
        "typeProperties": {
          "items": {
            "value": "@activity('LookupTables').output.value",
            "type": "Expression"
          },
          "activities": [
            {
              "name": "CopyTable",
              "type": "Copy",
              // Use @item().tableName in dataset/query
            }
          ]
        }
      }
    ]
  }
}
```

### Exercise 4.2: Sequential ForEach
Modify the above to run sequentially (isSequential = true).

```json
// YOUR CODE HERE:


```

### Exercise 4.3: Parallel ForEach with Batch Count
Configure ForEach to run 5 batches in parallel.

```json
// YOUR CODE HERE:


```

---

## Exercise Set 5: Control Flow - If Condition

### Exercise 5.1: Simple If Condition
Create a pipeline that checks if the load type is "full" or "incremental".

```json
// YOUR CODE HERE:
{
  "name": "pl_conditional_load",
  "properties": {
    "parameters": {
      "loadType": {"type": "string"}
    },
    "activities": [
      {
        "name": "CheckLoadType",
        "type": "IfCondition",
        "typeProperties": {
          "expression": {
            "value": "@equals(pipeline().parameters.loadType, 'full')",
            "type": "Expression"
          },
          "ifTrueActivities": [
            // Full load activities
          ],
          "ifFalseActivities": [
            // Incremental load activities
          ]
        }
      }
    ]
  }
}
```

### Exercise 5.2: Nested Conditions
Add nested If Condition for status checking.

```json
// YOUR CODE HERE:


```

---

## Exercise Set 6: Lookup & Get Metadata

### Exercise 6.1: Lookup Activity
Use Lookup to read configuration from a metadata table.

```json
// YOUR CODE HERE:
{
  "name": "pl_with_lookup",
  "activities": [
    {
      "name": "GetConfig",
      "type": "Lookup",
      "typeProperties": {
        "source": {
          "type": "SqlSource",
          "sqlReaderQuery": "SELECT table_name, load_type, watermark_column FROM etl.config WHERE is_active = 1"
        },
        "dataset": {
          "referenceName": "ds_sql_config"
        },
        "firstRowOnly": false
      }
    }
  ]
}
```

### Exercise 6.2: Get Metadata Activity
Check if a file exists using GetMetadata.

```json
// YOUR CODE HERE:
{
  "name": "pl_check_file",
  "activities": [
    {
      "name": "GetFileInfo",
      "type": "GetMetadata",
      "typeProperties": {
        "dataset": {
          "referenceName": "ds_adls_file"
        },
        "fieldList": ["exists", "size", "lastModified"]
      }
    }
  ]
}
```

### Exercise 6.3: Branch Based on Metadata
Use GetMetadata output to decide next step.

```json
// YOUR CODE HERE:
{
  "name": "pl_file_check_branch",
  "typeProperties": {
    "expression": {
      "value": "@activity('GetFileInfo').output.exists",
      "type": "Expression"
    },
    // ifTrue: copy file
    // ifFalse: skip
  }
}
```

---

## Exercise Set 7: Parameters & Variables

### Exercise 7.1: Pipeline Parameters
Create a pipeline with parameters for source table and target folder.

```json
// YOUR CODE HERE:
{
  "name": "pl_parameterized",
  "properties": {
    "parameters": {
      "sourceTable": {"type": "string"},
      "targetFolder": {"type": "string"},
      "loadDate": {"type": "string"}
    }
  }
}
```

### Exercise 7.2: Set Variable
Use Set Variable activity to construct a dynamic path.

```json
// YOUR CODE HERE:
{
  "name": "pl_with_variables",
  "variables": {
    "targetPath": {"type": "string"}
  },
  "activities": [
    {
      "name": "SetTargetPath",
      "type": "SetVariable",
      "typeProperties": {
        "variableName": "targetPath",
        "value": {
          "value": "@concat('raw/', pipeline().parameters.sourceTable, '/dt=', pipeline().parameters.loadDate)",
          "type": "Expression"
        }
      }
    }
  ]
}
```

### Exercise 7.3: Append Variable
Use Append Variable inside ForEach to collect results.

```json
// YOUR CODE HERE:


```

---

## Exercise Set 8: Triggers

### Exercise 8.1: Schedule Trigger
Create a trigger that runs daily at 2 AM.

```json
// YOUR CODE HERE:
{
  "name": "trg_daily_2am",
  "properties": {
    // Add Schedule trigger configuration
  }
}
```

### Exercise 8.2: Tumbling Window Trigger
Create an hourly tumbling window trigger for processing.

```json
// YOUR CODE HERE:
{
  "name": "trg_hourly_window",
  "properties": {
    // Add Tumbling Window trigger with windowStart and windowEnd parameters
  }
}
```

### Exercise 8.3: Event Trigger
Create a trigger that fires when a blob is added to a container.

```json
// YOUR CODE HERE:
{
  "name": "trg_blob_arrival",
  "properties": {
    // Add Event trigger for blob created event
  }
}
```

---

## Exercise Set 9: Incremental Loading

### Exercise 9.1: Watermark Pattern
Implement the watermark pattern for incremental loading.

```json
// YOUR CODE HERE:
// Steps:
// 1. Lookup to get last watermark
// 2. Copy with watermark filter
// 3. Update watermark
{
  "name": "pl_incremental_watermark",
  "properties": {
    "activities": [
      {
        "name": "GetWatermark",
        "type": "Lookup",
        // SELECT max_timestamp FROM watermark_table WHERE table_name = 'orders'
      },
      {
        "name": "CopyIncremental",
        "type": "Copy",
        "typeProperties": {
          "source": {
            "type": "SqlSource",
            // Query: SELECT * FROM orders WHERE updated_at > @lastWatermark
          }
        }
      },
      {
        "name": "UpdateWatermark",
        "type": "SqlSink",
        // UPDATE watermark_table SET max_timestamp = @currentMax
      }
    ]
  }
}
```

### Exercise 9.2: Get Max Value as Watermark
Find the maximum timestamp from the source data.

```json
// YOUR CODE HERE:
{
  "name": "GetSourceMaxTimestamp",
  "type": "Lookup",
  "typeProperties": {
    "source": {
      "type": "SqlSource",
      "sqlReaderQuery": "SELECT MAX(updated_at) as max_ts FROM orders"
    },
    "firstRowOnly": true
  }
}
```

---

## Exercise Set 10: Error Handling & Retry

### Exercise 10.1: Retry Policy
Configure retry policy on an activity.

```json
// YOUR CODE HERE:
{
  "name": "pl_with_retry",
  "typeProperties": {
    "retryPolicy": {
      "intervalInSeconds": 30,
      "count": 3,
      "minimumWaitTime": "00:00:05"
    }
  }
}
```

### Exercise 10.2: On-Failure Path
Handle errors and send notification.

```json
// YOUR CODE HERE:
{
  "name": "pl_with_error_handling",
  "activities": [
    {
      "name": "MainActivity",
      "type": "Copy",
      "onError": [
        {
          "name": "SendFailureAlert",
          "type": "WebActivity",
          // Call Slack webhook
        }
      ]
    }
  ]
}
```

### Exercise 10.3: Skip Faulty Rows
Configure copy activity to skip rows with errors.

```json
// YOUR CODE HERE:
{
  "name": "CopyWithSkip",
  "typeProperties": {
    "redirectIncompatibleRowSettings": {
      "mode": "SkippedFile",
      "path": "error/skip/"
    }
  }
}
```

---

## Exercise Set 11: Mapping Data Flow (Conceptual)

### Exercise 11.1: Data Flow Source & Sink
Define a simple data flow that reads from source and writes to sink.

```json
// YOUR CODE HERE:
// Note: Data Flows are designed visually in ADF UI
// Describe the flow: Source -> Select -> Filter -> Sink
```

### Exercise 11.2: Join Transformation
Create a data flow that joins two datasets.

```
// Flow:
// orders_source (SQL) --> Join --> Derived Column --> sink (ADLS)
//           ^                               |
//           └── customers_source (SQL) ------+
```

### Exercise 11.3: Aggregate Transformation
Create an aggregation to calculate totals by category.

```
// Flow:
// products_source --> Aggregate (SUM by category) --> CategoryTotals
```

---

## Exercise Set 12: Monitoring & Alerts

### Exercise 12.1: View Pipeline Runs
Write a query to find all failed pipeline runs in the last 24 hours.

```python
# YOUR CODE HERE:
# Use Azure Monitor logs or ADF SDK
```

### Exercise 12.2: Create Alert
Configure an alert for pipeline failures.

```
# YOUR CODE HERE:
# Set up Azure Monitor alert with:
# - Condition: pipeline runs failed
# - Threshold: > 0
# - Action: Send email/webhook
```

---

## Challenge Exercises

### Challenge 1: Complete ETL Pipeline
Build a production-ready pipeline with:
1. Get metadata from source
2. Check if full or incremental load
3. If incremental, get watermark and copy only new data
4. Log results
5. Send success/failure notification

```json
// YOUR CODE HERE:



```

### Challenge 2: Multi-Table Loader
Create a metadata-driven pipeline that:
1. Reads table list from config
2. For each table, determines load type
3. Copies data to appropriate folder
4. Tracks load status

```json
// YOUR CODE HERE:



```

### Challenge 3: Event-Driven Processing
Create an event-driven pipeline that:
1. Triggered when file arrives in landing zone
2. Validates file format
3. Copies to raw zone with date partition
4. Calls Databricks for processing
5. Moves to curated zone on success

```json
// YOUR CODE HERE:



```

---

## Testing Your ADF Pipelines

### Debug Mode
Use "Debug" button in ADF UI to test pipelines with real data.

### Test Commands

```bash
# Using Azure CLI to trigger pipeline
az datafactory pipeline create-run \
  --resource-group myrg \
  --factory-name mydf \
  --name pl_copy_customers \
  --parameters sourceTable=customers

# Using ADF SDK in Python
from azure.mgmt.datafactory import DataFactoryManagementClient
client.pipeline_runs.create_run(...)
```

---

## Practice Complete!

After completing these exercises, you should be comfortable with:
- Creating and configuring Linked Services
- Defining Datasets (SQL, Parquet, CSV)
- Building Pipelines with Copy Activity
- Using Control Flow (ForEach, If Condition)
- Working with Parameters and Variables
- Configuring Triggers (Schedule, Tumbling Window, Event)
- Implementing Incremental Loading patterns
- Error handling and retry policies
- Monitoring and alerting

---

## Next Steps

1. Deploy these pipelines in Azure
2. Test with real data sources
3. Explore Mapping Data Flows visually
4. Set up CI/CD for ADF
5. Implement monitoring dashboards
