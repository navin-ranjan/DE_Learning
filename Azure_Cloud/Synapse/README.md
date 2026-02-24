# Azure Synapse Analytics

## Core Theory Concepts (Must Know)
- MPP architecture fundamentals and distributed query execution
- Compute/storage decoupling and workload isolation choices
- Dedicated vs serverless cost-performance tradeoffs
- Distribution strategy theory (hash, round-robin, replicate) and data movement
- Lakehouse and warehouse interoperability patterns
- Security layering (network, identity, object-level authorization)

## Fundamentals
- What is Azure Synapse Analytics?
- Synapse Architecture
- Synapse vs Traditional Data Warehouses
- Workspace Overview
- Components of Synapse

## Synapse Components

### Synapse SQL (Dedicated and Serverless SQL Pools)
- Dedicated SQL Pool (formerly SQL DW)
- Serverless SQL Pool (on-demand querying)
- Choosing Between Dedicated & Serverless
- Performance Tiers

### Synapse Spark
- Spark Pool Creation
- Spark Configuration
- Notebooks in Synapse
- Spark Job Definitions

### Synapse Pipelines
- Pipeline Activities
- Copy Activity
- Data Flows
- Triggers
- Integration Runtimes

### Synapse Studio
- Workspace Interface
- Data Hub
- Develop Hub
- Integrate Hub
- Monitor Hub
- Manage Hub

## Dedicated SQL Pool

### Architecture
- Control Node
- Compute Nodes
- Data Distribution (Hash, Round Robin, Replicated)
- MPP Architecture

### Table Design
- Clustered Columnstore Index
- Heap Tables
- Clustered Index
- Partitioning
- Distribution Methods
- Table Types (Fact, Dimension)

### Performance
- Query Performance Tuning
- Index Management
- Statistics
- Result Set Caching
- Materialized Views
- Workload management and resource classes

### Data Loading
- PolyBase
- COPY Statement
- CTAS (Create Table As Select)
- CETAS (Create External Table As Select)

## Serverless SQL Pool
- Query Files Directly
- OPENROWSET
- External Tables
- Views
- Data Lake Exploration
- CETAS in Serverless

## Spark Pool in Synapse
- Pool Configuration
- Auto-pause
- Autoscale
- Library Management
- Spark Notebooks
- Delta Lake Integration

## Data Integration
- Pipelines Overview
- Copy Data Tool
- Data Flows
- Mapping Data Flows
- Wrangling Data Flows
- Pipeline Parameters

## Security
- Workspace Managed Identity
- Managed VNet
- Private Endpoints
- Data Masking
- Row-Level Security
- Azure AD Integration
- Access Control

## Connectivity
- Linked Services
- External Data Sources
- Azure Integration Runtime
- Self-hosted Integration Runtime

## Monitoring & Optimization
- Synapse Monitor Hub
- Query Monitoring
- Pipeline Monitoring
- Spark Applications
- DMVs (Dynamic Management Views)
- Azure Monitor Integration
- Explain plans and query step analysis

## Common Workloads
- Data Warehousing
- Data Lake Analytics
- Real-time Analytics
- Data Science
- ETL/ELT Pipelines

## Integration with Other Services
- Synapse + ADLS Gen2
- Synapse + Power BI
- Synapse + Azure ML
- Synapse + Azure Data Factory
- Synapse + Azure Purview

## Best Practices
- Data Modeling
- Query Optimization
- Cost Management
- Security Best Practices
- CI/CD for Synapse

## Useful Resources
- Theory Notes: `./synapse_theory.md`
- Official Documentation: https://learn.microsoft.com/en-us/azure/synapse-analytics/
- Microsoft Learn: https://learn.microsoft.com/en-us/training/paths/data-engineer-azure-synapse-analytics/
- Synapse GitHub Samples: https://github.com/Azure-Samples/Synapse
