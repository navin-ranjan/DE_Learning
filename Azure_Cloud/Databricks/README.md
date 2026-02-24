# Azure Databricks

## Core Theory Concepts (Must Know)
- Lakehouse architecture principles (warehouse reliability + lake flexibility)
- Separation of storage and compute with elastic clusters
- Delta transaction log internals and optimistic concurrency
- Medallion architecture objectives (data quality progression across layers)
- Batch vs streaming unification and incremental processing design
- Governance model in Unity Catalog (securables and privilege inheritance)

## Fundamentals
- What is Databricks?
- Databricks Architecture
- Workspace & Clusters
- Notebooks & Jobs
- Unity Catalog Overview
- Lakehouse Platform Overview

## Workspace & Environment
- Creating a Workspace
- Workspace Navigation
- Folders & Organization
- Repos (Git Integration)
- Secrets Management

## Clusters
- All-Purpose Clusters
- Job Clusters
- Cluster Configuration
- Autoscaling
- Cluster Policies
- Instance Pools
- Cluster Libraries
- Init Scripts

## Notebooks
- Creating Notebooks
- Notebook Languages (Python, SQL, Scala, R)
- Magic Commands (%python, %sql, %scala)
- Notebook Workflows (%run, dbutils.notebook.run)
- Markdown & Visualization
- Widgets (dbutils.widgets)
- Notebook Revision History

## Spark in Databricks
- Spark Configuration
- Spark UI
- Optimizations (Photon Engine)
- Cached Tables
- Spark Logs

## Delta Lake
- What is Delta Lake?
- ACID Transactions
- Delta Table Creation
- CRUD Operations
- Time Travel
- Vacuum (Cleanup)
- Delta History
- Schema Evolution
- MERGE Operations
- Delta Sharing

## Data Engineering on Databricks
- ETL Patterns
- Batch Processing
- Structured Streaming
- Incremental Processing
- Auto Loader
- Bronze-Silver-Gold Architecture
- Medallion Architecture
- Delta Live Tables (Lakeflow Declarative Pipelines) basics

## Jobs & Workflows
- Creating Jobs
- Job Clusters vs All-Purpose
- Task Dependencies
- Job Parameters
- Job Scheduling
- Job Alerts
- Job History & Monitoring

## Unity Catalog
- What is Unity Catalog?
- Metastore Setup
- Catalogs & Schemas
- Table Management
- Permissions & Access Control
- Data Lineage
- External Locations

## dbutils (Databricks Utilities)
- dbutils.fs (File System)
- dbutils.widgets (Parameters)
- dbutils.secrets (Secret Management)
- dbutils.library (Libraries)
- dbutils.notebook (Notebook Utilities)

## SQL Analytics
- SQL Warehouses
- SQL Queries & Dashboards
- Query Editor
- Visualizations
- Alerts

## MLflow Integration
- Experiment Tracking
- Model Registry
- Model Deployment

## Security & Governance
- IAM Roles
- Cluster Access Control
- Table Access Control
- Secrets Scopes
- Audit Logs

## Integration
- Databricks with ADF
- Databricks with Synapse
- Databricks with ADLS
- Databricks with Event Hubs

## Performance Tuning
- Cluster Sizing
- Spark Tuning
- Delta Lake Optimization (OPTIMIZE, ZORDER)
- Caching Strategies
- Partitioning
- Data skipping and file compaction strategy

## Best Practices
- Notebook Best Practices
- Production Job Design
- Cost Optimization
- Error Handling

## Useful Resources
- Theory Notes: `./databricks_theory.md`
- Official Documentation: https://docs.databricks.com/
- Databricks Academy: https://academy.databricks.com/
- Databricks Labs: https://github.com/databrickslabs
