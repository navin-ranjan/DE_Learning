# Azure Data Factory (ADF)

## Core Theory Concepts (Must Know)
- Control flow vs data flow separation in pipeline design
- Metadata-driven pipelines and parameterization patterns
- Incremental loading patterns (watermarks and CDC basics)
- Idempotency and retry-safe pipeline behavior
- Orchestration latency vs throughput tradeoffs
- Cost and performance tradeoffs across Integration Runtime choices

## Fundamentals
- What is Azure Data Factory?
- ADF Architecture
- Integration Runtimes (Azure, Self-hosted, SSIS)
- Pipelines, Activities, Datasets, Linked Services

## Core Components
- Pipelines
- Activities
- Datasets
- Linked Services
- Triggers
- Data Flows
- Integration Runtimes

## Linked Services
- Azure Blob Storage
- Azure Data Lake Storage (ADLS)
- Azure SQL Database
- Azure Synapse Analytics
- Azure Databricks
- AWS S3
- On-premises SQL Server
- REST API

## Activities
- Copy Activity (Data Movement)
- Data Flow Activity
- Databricks Notebook Activity
- Stored Procedure Activity
- Lookup Activity
- Get Metadata Activity
- Filter Activity
- ForEach Activity
- If Condition Activity
- Switch Activity
- Wait Activity
- Web Activity
- Set Variable Activity

## Data Flows (Mapping)
- Source & Sink Transformations
- Select Transformation
- Filter Transformation
- Join Transformation
- Aggregate Transformation
- Derived Columns
- Lookup Transformation
- Conditional Split
- Union Transformation
- Pivot & Unpivot
- Surrogate Key
- Schema drift handling

## Triggers
- Schedule Trigger
- Tumbling Window Trigger
- Event Trigger (Blob, Custom)
- Manual Execution

## Parameters & Variables
- Pipeline Parameters
- Pipeline Variables
- Global Parameters
- Expressions & Dynamic Content

## Monitoring & Management
- Pipeline Monitoring
- Debug Mode
- Activity Runs
- Trigger Runs
- Alerts & Metrics
- Azure Monitor Integration

## CI/CD & Deployment
- ARM Templates
- Azure DevOps Integration
- GitHub Integration
- Publishing Pipelines
- Deployment Best Practices

## Best Practices
- Naming Conventions
- Parameterization
- Error Handling
- Performance Optimization
- Cost Optimization
- Security (Managed Identity, Key Vault)
- Metadata-driven framework design

## Integration with Other Services
- ADF + Azure Databricks
- ADF + Azure Synapse
- ADF + Azure Functions
- ADF + Azure Key Vault

## Useful Resources
- Theory Notes: `./adf_theory.md`
- Official Documentation: https://learn.microsoft.com/en-us/azure/data-factory/
- Microsoft Learn: https://learn.microsoft.com/en-us/training/paths/data-integration-azure-data-factory/
