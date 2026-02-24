# Azure Data Factory Theory & Tutorial

## Table of Contents
1. [What is Azure Data Factory?](#1-what-is-azure-data-factory)
2. [Core Concepts](#2-core-concepts)
3. [Integration Runtime](#3-integration-runtime)
4. [Linked Services](#4-linked-services)
5. [Datasets](#5-datasets)
6. [Activities](#6-activities)
7. [Control Flow](#7-control-flow)
8. [Mapping Data Flows](#8-mapping-data-flows)
9. [Triggers](#9-triggers)
10. [Parameters & Variables](#10-parameters--variables)
11. [Incremental Loading Patterns](#11-incremental-loading-patterns)
12. [Monitoring & Debugging](#12-monitoring--debugging)
13. [CI/CD & Deployment](#13-cicd--deployment)
14. [Security Best Practices](#14-security-best-practices)
15. [Performance Optimization](#15-performance-optimization)
16. [Quick Reference](#16-quick-reference)

---

## 1. What is Azure Data Factory?

### 📖 What is Azure Data Factory?

**Azure Data Factory (ADF)** is a managed cloud service for data integration and orchestration. It is a serverless data integration service that enables you to create data-driven workflows for orchestrating data movement and transforming data at scale.

**Key Capabilities:**
- Connects to 90+ data sources (cloud and on-premises)
- Moves data reliably at scale between systems
- Runs scheduled and event-driven pipelines
- Coordinates external compute systems (Databricks, Synapse, HDInsight)
- Provides centralized monitoring and logging

### Core Terminology

| Term | Description |
|------|-------------|
| **Pipeline** | Logical grouping of activities that performs a unit of work |
| **Activity** | A single processing step in a pipeline (Copy, Lookup, etc.) |
| **Dataset** | Named view of data that points to the data to be used |
| **Linked Service** | Connection string defining connection info to external resources |
| **Integration Runtime** | The compute infrastructure for data movement and transformation |
| **Trigger** | Determines when a pipeline execution is kicked off |

### Why is this important for Data Engineering?
- Central orchestration hub for ETL/ELT pipelines
- Hybrid data integration (cloud + on-premises)
- Scalable data movement without managing infrastructure
- Integration with the full Azure data ecosystem
- Production-grade monitoring and reliability features

---

## 2. Core Concepts

### 2.1 Control Flow vs Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    CONTROL FLOW                              │
│  Orchestration logic: sequence, branch, loop, retries       │
│  Activities: ForEach, If, Wait, Lookup, Web, etc.           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     DATA FLOW                                │
│  Record-level transformation: join, filter, aggregate       │
│  Spark-backed engine for visual ETL                         │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Metadata-Driven Pipeline Design

Instead of creating one pipeline per table, create one generic pipeline driven by metadata.

**Benefits:**
- Lower maintenance overhead
- Faster onboarding for new data sources
- Consistent validation and logging across all entities

```json
{
  "source_system": "ERP",
  "source_schema": "sales",
  "source_table": "orders",
  "sink_path": "raw/sales/orders",
  "load_type": "incremental",
  "watermark_column": "updated_at"
}
```

### 2.3 Idempotency

**Idempotency** means rerunning a pipeline should not create duplicates or inconsistent state.

**Patterns:**
| Pattern | Use Case |
|---------|----------|
| Load to staging then merge | Data warehouse loads |
| Partition overwrite | Time-partitioned data lakes |
| Deterministic file paths | Raw zone ingestion |

---

## 3. Integration Runtime

### 📖 What is Integration Runtime?

**Integration Runtime (IR)** is the compute infrastructure used by Azure Data Factory to provide data integration capabilities. It determines where the activity executes.

### Types of Integration Runtime

| Type | Use Case | Location |
|------|----------|----------|
| **Azure IR** | Cloud-to-cloud data movement | Managed by Azure |
| **Self-hosted IR** | Access private/on-premises networks | Your VM/Server |
| **Azure-SSIS IR** | Execute SSIS packages in Azure | Managed by Azure |

### Azure Integration Runtime

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│  Azure SQL  │ ───▶ │  Azure IR   │ ───▶ │    ADLS     │
│  (Source)   │      │  (Managed)  │      │  (Target)   │
└─────────────┘      └─────────────┘      └─────────────┘
```

**When to use:**
- Cloud-native data sources
- Mapping data flows
- Most cloud-to-cloud scenarios

### Self-hosted Integration Runtime

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│ On-prem SQL │ ───▶ │ Self-hosted  │ ───▶ │    ADLS     │
│   Server    │      │     IR       │      │  (Azure)    │
└─────────────┘      │ (Your Server)│      └─────────────┘
                     └──────────────┘
```

**When to use:**
- On-premises data sources
- Private networks (VPN/VNet)
- Internal cloud services not publicly accessible

### IR Decision Matrix

| Scenario | Recommended IR |
|----------|---------------|
| Azure SQL to ADLS | Azure IR |
| On-prem SQL to ADLS | Self-hosted IR |
| AWS S3 to ADLS | Azure IR |
| Private REST API | Self-hosted IR |
| Execute SSIS packages | Azure-SSIS IR |

### Why is this important for Data Engineering?
- Determines connectivity options for data sources
- Affects performance and throughput
- Security boundary for private data sources
- Cost implications (self-hosted IR requires your own VM)

---

## 4. Linked Services

### 📖 What is a Linked Service?

**Linked Service** defines the connection information needed for Azure Data Factory to connect to external data stores or compute resources. Think of it as a connection string with authentication details.

### Common Linked Services

| Service Type | Example |
|-------------|---------|
| Storage | Azure Blob, ADLS Gen2, AWS S3 |
| Database | Azure SQL, Synapse, PostgreSQL, Oracle |
| Compute | Azure Databricks, HDInsight, Azure Functions |
| Generic | REST API, HTTP, OData |

### Authentication Options

| Method | Security Level | Use Case |
|--------|-----------------|----------|
| **Managed Identity** | Best | Azure resources (recommended) |
| **Service Principal** | Good | Automated processes |
| **SAS Token** | Good | Storage accounts |
| **Account Key** | Acceptable | Quick testing only |
| **Username/Password** | Avoid | Legacy systems only |

### Managed Identity Example

```json
{
  "name": "ls_adls_raw",
  "type": "AzureBlobFS",
  "typeProperties": {
    "url": "https://mystorage.dfs.core.windows.net"
  },
  "connectVia": {
    "referenceName": "AzureIntegrationRuntime",
    "type": "IntegrationRuntimeReference"
  }
}
```

### Key Vault Integration

```json
{
  "name": "ls_sql_source",
  "type": "AzureSqlDatabase",
  "typeProperties": {
    "connectionString": "@{linkedService().connectionString}",
    "password": {
      "type": "AzureKeyVaultSecret",
      "store": {
        "referenceName": "ls_keyvault",
        "type": "LinkedServiceReference"
      },
      "secretName": "sql-password"
    }
  }
}
```

### Why is this important for Data Engineering?
- Centralized connection management
- Security through credential separation
- Easy environment switching (dev/test/prod)
- Audit trail for data source access

---

## 5. Datasets

### 📖 What is a Dataset?

**Dataset** is a named view of data that simply points or references the data you want to use in your activities as inputs and outputs. Datasets identify data within different data stores.

### Dataset Types

| Type | Description |
|------|-------------|
| **File-based** | Parquet, CSV, JSON, Avro files |
| **Table-based** | SQL tables, views |
| **Binary** | Binary copy without parsing |
| **Azure Search Index** | For search operations |

### File-based Dataset Properties

```json
{
  "name": "ds_sales_parquet",
  "type": "Parquet",
  "linkedServiceName": {
    "referenceName": "ls_adls_raw",
    "type": "LinkedServiceReference"
  },
  "typeProperties": {
    "location": {
      "type": "AzureBlobFSLocation",
      "fileName": "sales.parquet",
      "folderPath": "raw/sales"
    },
    "compressionCodec": "snappy"
  },
  "schema": []
}
```

### Parameterized Datasets

```json
{
  "name": "ds_dynamic_parquet",
  "type": "Parquet",
  "properties": {
    "parameters": {
      "tableName": {
        "type": "string"
      },
      "partitionDate": {
        "type": "string"
      }
    },
    "typeProperties": {
      "location": {
        "type": "AzureBlobFSLocation",
        "folderPath": {
          "value": "@{concat('raw/', dataset().tableName, '/dt=', dataset().partitionDate)}",
          "type": "Expression"
        }
      }
    }
  }
}
```

### Why is this important for Data Engineering?
- Reusable data references across pipelines
- Schema enforcement options
- Partition and folder path patterns
- Format specification (CSV, Parquet, JSON, etc.)

---

## 6. Activities

### 📖 What is an Activity?

**Activities** are the processing steps in a pipeline. They define the actions to perform on your data, such as copying data, running a stored procedure, or executing a Databricks notebook.

### Activity Categories

| Category | Activities |
|----------|-----------|
| **Data Movement** | Copy, Delete |
| **Data Transformation** | Data Flow, Databricks Notebook, HDInsight |
| **Control** | ForEach, If Condition, Switch, Wait |
| **Metadata** | Lookup, Get Metadata |
| **External** | Web, Azure Function, Execute Pipeline |

### Copy Activity

```json
{
  "name": "CopySalesData",
  "type": "Copy",
  "inputs": [
    {
      "referenceName": "ds_sql_orders",
      "type": "DatasetReference"
    }
  ],
  "outputs": [
    {
      "referenceName": "ds_adls_orders",
      "type": "DatasetReference"
    }
  ],
  "typeProperties": {
    "source": {
      "type": "SqlSource",
      "sqlReaderQuery": "SELECT * FROM sales.orders WHERE updated_at > '@{pipeline().parameters.watermark}'"
    },
    "sink": {
      "type": "ParquetSink",
      "storeSettings": {
        "type": "AzureBlobFSWriteSettings"
      }
    },
    "enableStaging": false,
    "parallelCopies": 4
  }
}
```

### Lookup Activity

```json
{
  "name": "LookupConfig",
  "type": "Lookup",
  "typeProperties": {
    "source": {
      "type": "SqlSource",
      "sqlReaderQuery": "SELECT * FROM etl.metadata WHERE is_active = 1"
    },
    "dataset": {
      "referenceName": "ds_sql_metadata",
      "type": "DatasetReference"
    },
    "firstRowOnly": false
  }
}
```

### ForEach Activity

```json
{
  "name": "ForEachTable",
  "type": "ForEach",
  "dependsOn": [
    {
      "activity": "LookupConfig",
      "dependencyConditions": ["Succeeded"]
    }
  ],
  "typeProperties": {
    "items": {
      "value": "@activity('LookupConfig').output.value",
      "type": "Expression"
    },
    "isSequential": false,
    "batchCount": 5,
    "activities": [
      {
        "name": "CopyActivity",
        "type": "Copy",
        "typeProperties": {
          "source": {
            "type": "SqlSource",
            "sqlReaderQuery": {
              "value": "SELECT * FROM @{item().source_schema}.@{item().source_table}",
              "type": "Expression"
            }
          }
        }
      }
    ]
  }
}
```

### If Condition Activity

```json
{
  "name": "CheckLoadType",
  "type": "IfCondition",
  "typeProperties": {
    "expression": {
      "value": "@equals(pipeline().parameters.loadType, 'full')",
      "type": "Expression"
    },
    "ifTrueActivities": [
      {
        "name": "FullLoad",
        "type": "Copy"
      }
    ],
    "ifFalseActivities": [
      {
        "name": "IncrementalLoad",
        "type": "Copy"
      }
    ]
  }
}
```

### Web Activity (for notifications)

```json
{
  "name": "SendSuccessNotification",
  "type": "WebActivity",
  "typeProperties": {
    "url": "https://hooks.slack.com/services/xxx",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "text": "Pipeline completed successfully"
    }
  }
}
```

### Why is this important for Data Engineering?
- Building blocks of data pipelines
- Handle data movement, transformation, and orchestration
- Error handling and retry capabilities
- Integration with external systems

---

## 7. Control Flow

### 📖 What is Control Flow?

**Control Flow** is the orchestration logic that defines the sequence of activities, conditional branching, looping, and error handling in a pipeline.

### Control Flow Design Patterns

#### Pattern 1: Metadata-Driven Loop

```
Lookup (metadata) ──▶ ForEach ──▶ Copy Activity
                         │
                         ▼
                  Audit Logging
```

#### Pattern 2: Branch by Load Type

```
┌─────────────────┐
│  If Condition   │
│ loadType ==     │
│    'full'       │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌─────────┐
│ Full  │ │Incr.    │
│ Load  │ │Load     │
└───────┘ └─────────┘
```

#### Pattern 3: Parent-Child Pipeline

```
Parent Pipeline:
┌─────────────┐
│  Schedule   │
│  Trigger    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Lookup    │
│  Config     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   ForEach   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Execute    │──▶ Child Pipeline (per entity)
│  Pipeline   │
└─────────────┘
```

### Dependency Types

| Dependency | Meaning |
|------------|---------|
| **Succeeded** | Run after success |
| **Failed** | Run after failure |
| **Skipped** | Run after skip |
| **Completed** | Run after any completion state |

### Error Handling Pattern

```
Copy Activity
    │
    ├──▶ On Success ──▶ Success Notification
    │
    └──▶ On Failure ──▶ Log Error ──▶ Failure Notification
```

### Why is this important for Data Engineering?
- Orchestrate complex ETL workflows
- Handle dependencies between data loads
- Implement retry and error handling logic
- Scale processing through parallel execution

---

## 8. Mapping Data Flows

### 📖 What is Mapping Data Flow?

**Mapping Data Flows** are visually designed data transformations in Azure Data Factory. They provide a code-free way to transform data at scale using the Spark engine.

### When to Use Data Flows

| Use Case | Recommendation |
|----------|---------------|
| Multi-step visual transformations | Use Data Flow |
| Simple data movement | Use Copy Activity |
| Complex code-first logic | Use Databricks |

### Common Transformations

| Transformation | Purpose |
|----------------|---------|
| **Source** | Define input data |
| **Select** | Rename/select columns |
| **Filter** | Row filtering |
| **Join** | Combine datasets |
| **Aggregate** | Group and calculate |
| **Derived Column** | Add computed columns |
| **Lookup** | Dimension enrichment |
| **Conditional Split** | Route rows to outputs |
| **Union** | Combine row sets |
| **Pivot/Unpivot** | Reshape data |
| **Surrogate Key** | Generate sequence keys |

### Data Flow Chain Example

```
Source ──▶ Select ──▶ Filter ──▶ Join ──▶ Aggregate ──▶ Sink
  │                                    │
  │                                    ▼
  │                              Derived Column
  │                                    │
  └────────────────────────────────────┘
```

### Data Flow Performance Tips

1. **Filter early** - Reduce data volume early in the chain
2. **Limit wide transformations** - Minimize columns where possible
3. **Partition correctly** - Match source partitioning
4. **Avoid unnecessary caching** - Use only when needed

### Why is this important for Data Engineering?
- Code-free visual ETL development
- Spark-backed scalability
- Schema drift handling
- Real-time preview and debugging

---

## 9. Triggers

### 📖 What is a Trigger?

**Triggers** determine when a pipeline execution is kicked off. They represent the scheduling mechanism for pipelines.

### Trigger Types

| Trigger Type | Use Case | Best For |
|-------------|----------|----------|
| **Schedule** | Time-based execution | Daily/hourly batches |
| **Tumbling Window** | Backfill scenarios | Strict processing windows |
| **Event** | Blob arrival, custom events | Real-time ingestion |
| **Manual** | On-demand execution | Testing, reruns |

### Schedule Trigger

```json
{
  "name": "DailyScheduleTrigger",
  "properties": {
    "type": "ScheduleTrigger",
    "typeProperties": {
      "recurrence": {
        "frequency": "Day",
        "interval": 1,
        "startTime": "2024-01-01T00:00:00Z",
        "timeZone": "UTC"
      }
    },
    "pipeline": {
      "pipelineReference": {
        "type": "PipelineReference",
        "referenceName": "pl_daily_ingestion"
      },
      "parameters": {
        "date": "@formatDateTime(trigger().scheduledTime, 'yyyy-MM-dd')"
      }
    }
  }
}
```

### Tumbling Window Trigger

```json
{
  "name": "HourlyTumblingTrigger",
  "properties": {
    "type": "TumblingWindowTrigger",
    "typeProperties": {
      "frequency": "Hour",
      "interval": 1,
      "startTime": "2024-01-01T00:00:00Z",
      "endTime": "2024-12-31T00:00:00Z",
      "delay": "00:00:00",
      "maxConcurrency": 3,
      "retryPolicy": {
        "intervalInSeconds": 30,
        "count": 3
      }
    },
    "pipeline": {
      "pipelineReference": {
        "type": "PipelineReference",
        "referenceName": "pl_hourly_processing"
      },
      "parameters": {
        "windowStart": "@trigger().outputs.windowStartTime",
        "windowEnd": "@trigger().outputs.windowEndTime"
      }
    }
  }
}
```

### Trigger Comparison

| Feature | Schedule | Tumbling Window | Event |
|---------|----------|-----------------|-------|
| Periodic execution | Yes | Yes | No |
| Backfill support | No | Yes | No |
| Window state tracking | No | Yes | No |
| File arrival trigger | No | No | Yes |
| Chain dependencies | Limited | Yes | Limited |

### Why is this important for Data Engineering?
- Automate pipeline execution
- Handle batch processing schedules
- Enable event-driven architectures
- Support backfill and recovery scenarios

---

## 10. Parameters & Variables

### 📖 What are Parameters and Variables?

**Parameters** are input values passed to pipelines at execution start. They are immutable during pipeline execution.

**Variables** are mutable runtime values that can be set and modified during pipeline execution.

### Parameter Types

| Type | Description |
|------|-------------|
| **Pipeline Parameters** | Input values at pipeline start |
| **Dataset Parameters** | Reusable dataset configurations |
| **Global Parameters** | Factory-level constants |

### Variable Types

| Type | Scope | Mutable |
|------|-------|---------|
| **Pipeline Variables** | Within pipeline | Yes |
| **Activity Outputs** | Activity result | No (set by system) |

### Dynamic Expressions

```
@pipeline().parameters.tableName
@concat('raw/', pipeline().parameters.tableName, '/', formatDateTime(utcNow(), 'yyyy-MM-dd'))
@activity('LookupConfig').output.value
@item().source_table
@coalesce(variables('watermark'), '1900-01-01')
@formatDateTime(trigger().startTime, 'yyyy-MM-dd HH:mm:ss')
```

### Common Expression Functions

| Function | Example | Result |
|----------|---------|--------|
| `concat()` | `@concat('a', 'b')` | `ab` |
| `formatDateTime()` | `@formatDateTime(utcNow(), 'yyyy-MM')` | `2024-01` |
| `addDays()` | `@addDays(utcNow(), -1)` | Yesterday |
| `coalesce()` | `@coalesce(null, 'default')` | `default` |
| `equals()` | `@equals(1, 1)` | `true` |
| `greater()` | `@greater(5, 3)` | `true` |

### Why is this important for Data Engineering?
- Build reusable, generic pipelines
- Handle environment-specific configurations
- Enable metadata-driven processing
- Create dynamic paths and queries

---

## 11. Incremental Loading Patterns

### 📖 What is Incremental Loading?

**Incremental Loading** is the process of loading only new or changed data since the last run, rather than reloading the entire dataset.

### Patterns

| Pattern | Use Case | Complexity |
|---------|----------|------------|
| **Watermark** | Timestamp/ID-based incremental | Low |
| **CDC** | Change Data Capture | Medium |
| **Sliding Window** | Reprocess recent data | Low |

### Watermark Pattern

```sql
-- 1. Read previous watermark
SELECT MAX(updated_at) as watermark FROM audit.watermark WHERE table_name = 'orders';

-- 2. Extract new data
SELECT * FROM sales.orders
WHERE updated_at > @last_watermark
  AND updated_at <= @current_upper_bound;

-- 3. Load to target
-- 4. Update watermark
UPDATE audit.watermark SET watermark = @current_upper_bound WHERE table_name = 'orders';
```

### Pipeline Implementation

```
Lookup (get watermark)
    │
    ▼
Copy (extract with watermark filter)
    │
    ▼
Stored Procedure (update watermark)
```

### Idempotency Rules

1. **Never update watermark before successful load**
2. **Keep watermark updates in same transaction boundary as load**
3. **Store watermark per entity/table**
4. **Use merge/upsert for idempotent writes**

### Why is this important for Data Engineering?
- Reduces data movement and processing time
- Enables near real-time data pipelines
- Critical for large table processing
- Minimizes cost and resource usage

---

## 12. Monitoring & Debugging

### 📖 What is ADF Monitoring?

**Monitoring** provides visibility into pipeline execution, activity status, and system health through the ADF Studio and Azure Monitor.

### Monitoring Layers

| Layer | What to Monitor |
|-------|----------------|
| **Pipeline Run** | Success/failure, duration, parameters |
| **Activity Run** | Individual step results, error details |
| **Trigger Run** | Trigger execution history |

### Key Metrics

| Metric | Description |
|--------|-------------|
| Success Rate | Percentage of successful runs |
| Average Duration | Pipeline execution time |
| Retry Rate | How often retries occur |
| Data Volume | Amount of data moved |

### Debugging Sequence

1. Open failed activity output
2. Read connector/system error code
3. Verify linked service authentication
4. Verify network path and IR health
5. Re-run with same parameter set

### Alerting Strategy

| Alert Type | Trigger |
|------------|---------|
| Immediate | Any pipeline failure |
| Threshold | Consecutive failures (e.g., 3) |
| SLA | Duration exceeding threshold |

### Why is this important for Data Engineering?
- Ensure pipeline reliability
- Quickly identify and resolve issues
- Track data lineage and quality
- Meet SLAs and compliance requirements

---

## 13. CI/CD & Deployment

### 📖 What is ADF CI/CD?

**CI/CD (Continuous Integration/Continuous Deployment)** automates the testing and deployment of ADF pipelines across environments (dev/test/prod).

### Deployment Artifacts

| Artifact | Purpose |
|----------|---------|
| **ARM Templates** | Infrastructure as code for ADF |
| **Parameter Files** | Environment-specific values |
| **Git Integration** | Source control for pipelines |

### Branching Model

```
feature/user-branch ──▶ Pull Request ──▶ collaboration ──▶ Publish ──▶ ARM
                                                │                      Deployment
                                                │
                                                ▼
                                            dev ADF
```

### Environment Promotion

1. **Dev** - Authoring and debugging
2. **PR Review** - Code review process
3. **Publish** - Generate ARM templates
4. **QA** - Deploy to test environment
5. **Smoke Tests** - Validate deployment
6. **Prod** - Deploy to production

### Deployment Cautions

- Avoid direct manual prod edits
- Parameterize endpoints and secrets
- Keep release pipelines repeatable
- Use Azure DevOps or GitHub Actions

### Why is this important for Data Engineering?
- Production deployment safety
- Version control for pipelines
- Collaborative development
- Environment consistency

---

## 14. Security Best Practices

### 📖 What is ADF Security?

**Security** in ADF encompasses authentication, authorization, data encryption, and network protection for data integration workflows.

### Security Components

| Component | Best Practice |
|-----------|--------------|
| **Managed Identity** | Use for Azure resources |
| **Key Vault** | Store all secrets centrally |
| **RBAC** | Grant least privilege |
| **Private Endpoints** | For sensitive workloads |
| **Encryption** | At-rest and in-transit |

### Managed Identity Flow

```
1. Enable system-assigned managed identity on ADF
2. Grant storage/database access to ADF identity
3. Configure linked service to use managed identity
4. No credentials stored in ADF
```

### Key Vault Integration Pattern

```
ADF ──▶ Linked Service ──▶ Key Vault
                │
                ▼
           Secret Reference
                │
                ▼
           Target Resource
```

### Security Anti-patterns

| Anti-pattern | Solution |
|--------------|----------|
| Hardcoded keys in JSON | Use Key Vault references |
| Shared admin credentials | Use Managed Identity |
| Overprivileged identities | Grant minimal required access |
| Public endpoints for sensitive data | Use Private Link |

### Why is this important for Data Engineering?
- Protect sensitive data in transit and at rest
- Meet compliance requirements
- Prevent unauthorized access
- Audit data access patterns

---

## 15. Performance Optimization

### 📖 What is ADF Performance Optimization?

**Performance Optimization** involves tuning ADF pipelines to maximize throughput, minimize latency, and control costs.

### Copy Activity Optimization

| Setting | Recommendation |
|---------|---------------|
| **Parallel copies** | Increase when source/sink supports it |
| **Data Integration Units (DIU)** | Scale for cloud-to-cloud |
| **Partitioning** | Use for large table reads |
| **Push predicates** | Filter at source |

### Data Flow Optimization

1. Filter early to reduce data volume
2. Keep graph lean - minimize unnecessary transformations
3. Select efficient partitioning
4. Avoid keeping debug sessions active

### Cost Optimization Strategy

1. Use Copy activity for simple movement
2. Use Data Flow only where needed
3. Prefer incremental loads
4. Batch small files where possible
5. Tune trigger frequency by SLA

### Cost Hotspots

| Hotspot | Solution |
|---------|----------|
| Long-running data flows | Optimize transformations |
| Over-parallelized copies | Tune parallelism |
| Excessive trigger invocations | Batch where possible |

### Why is this important for Data Engineering?
- Control cloud costs
- Meet SLA requirements
- Handle growing data volumes
- Optimize resource utilization

---

## 16. Quick Reference

### Activity Quick Reference

| Activity | Purpose | Common Use |
|----------|---------|------------|
| Copy | Data movement | SQL to ADLS |
| Data Flow | Transform | Join, filter, aggregate |
| Lookup | Read config | Metadata table |
| Get Metadata | File properties | Check file exists |
| ForEach | Loop | Process multiple tables |
| If Condition | Branch | Full vs incremental |
| Web | API call | Slack notification |
| Wait | Pause | Delay execution |

### Integration Runtime Decision Tree

```
Data Source Location?
│
├── Azure (public)
│   └── Azure IR
│
├── On-premises / Private
│   └── Self-hosted IR
│
└── SSIS Packages
    └── Azure-SSIS IR
```

### Trigger Selection Guide

| Need | Use |
|------|-----|
| Daily refresh | Schedule Trigger |
| Strict hourly windows | Tumbling Window Trigger |
| File arrival | Event Trigger |
| Testing/rerun | Manual Trigger |

### Expression Quick Reference

```
@pipeline().parameters.paramName    - Parameter reference
@activity('ActivityName').output   - Activity output
@item().columnName                   - ForEach item property
@variables('varName')                - Variable reference
@utcNow()                            - Current UTC time
@formatDateTime(value, format)       - Format datetime
@concat('a', 'b')                    - Concatenate strings
@equals(a, b)                        - Equality check
@coalesce(value, default)            - Null handling
```

### Common File Paths Pattern

```
raw/{source}/{table}/dt={yyyy-MM-dd}/
curated/{domain}/{table}/dt={yyyy-MM-dd}/
error/{table}/dt={yyyy-MM-dd}/
```

---

**Happy Learning! Remember: Practice makes perfect.**
